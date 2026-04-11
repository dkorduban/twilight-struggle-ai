"""Country-attention prototypes with merged-region neighborhood sparsity.

This module is intentionally standalone and does not modify the production
policy stack. It prototypes a region-neighbor block attention pattern where
each country can attend to:

1. all countries in its own region
2. all countries in directly adjacent regions

For this prototype, Southeast Asia is merged into Asia.
"""

from __future__ import annotations

import csv
import pathlib
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F

NUM_COUNTRIES = 86
INFLUENCE_DIM = NUM_COUNTRIES * 2
INFLUENCE_HIDDEN = 128
SPEC_DIR = pathlib.Path(__file__).resolve().parents[4] / "data" / "spec"
MERGED_REGIONS = (
    "Europe",
    "Asia",
    "MiddleEast",
    "Africa",
    "CentralAmerica",
    "SouthAmerica",
)
_REGION_TO_INDEX = {name: idx for idx, name in enumerate(MERGED_REGIONS)}


@dataclass(frozen=True)
class RegionNeighborMetadata:
    """Static country-region structure for the merged-region prototype."""

    region_names: tuple[str, ...]
    country_static: torch.Tensor
    region_pool_indices: tuple[torch.Tensor, ...]
    block_query_indices: tuple[torch.Tensor, ...]
    block_kv_indices: tuple[torch.Tensor, ...]
    dense_mask_bias: torch.Tensor
    dense_pairs: int
    sparse_pairs: int


def _iter_country_rows(path: pathlib.Path) -> list[dict[str, str]]:
    with open(path, newline="") as handle:
        rows = [
            line
            for line in handle
            if line.strip() and not line.lstrip().startswith("#")
        ]
    return list(csv.DictReader(rows))


def _load_country_regions() -> tuple[list[str], torch.Tensor]:
    rows = _iter_country_rows(SPEC_DIR / "countries.csv")
    region_by_country = [""] * NUM_COUNTRIES
    feats = torch.zeros(NUM_COUNTRIES, 10, dtype=torch.float32)
    for row in rows:
        cid = int(row["country_id"])
        if cid < 0 or cid >= NUM_COUNTRIES:
            continue
        region = row["region"].strip()
        if region == "SoutheastAsia":
            region = "Asia"
        region_by_country[cid] = region
        feats[cid, 0] = float(row["stability"]) / 4.0
        feats[cid, 1] = 1.0 if row["is_battleground"].strip().lower() == "true" else 0.0
        feats[cid, 2 + _REGION_TO_INDEX[region]] = 1.0
        feats[cid, 8] = min(float(row["us_start_influence"]) / 3.0, 1.0)
        feats[cid, 9] = min(float(row["ussr_start_influence"]) / 3.0, 1.0)
    return region_by_country, feats


def _load_country_adjacency() -> list[set[int]]:
    adjacency: list[set[int]] = [set() for _ in range(NUM_COUNTRIES)]
    with open(SPEC_DIR / "adjacency.csv", newline="") as handle:
        reader = csv.reader(handle)
        for raw in reader:
            row = [cell.split("#")[0].strip() for cell in raw]
            if not row or row[0] == "" or row[0].startswith("#") or row[0] == "country_a":
                continue
            a, b = int(row[0]), int(row[1])
            if 0 <= a < NUM_COUNTRIES and 0 <= b < NUM_COUNTRIES:
                adjacency[a].add(b)
                adjacency[b].add(a)
    return adjacency


def build_region_neighbor_metadata() -> RegionNeighborMetadata:
    """Build merged-region attention metadata from canonical country specs."""

    region_by_country, country_static = _load_country_regions()
    adjacency = _load_country_adjacency()

    region_country_lists: list[list[int]] = [[] for _ in MERGED_REGIONS]
    for country_id, region_name in enumerate(region_by_country):
        if not region_name:
            continue
        region_country_lists[_REGION_TO_INDEX[region_name]].append(country_id)

    region_neighbor_regions: list[set[int]] = [set() for _ in MERGED_REGIONS]
    for a in range(NUM_COUNTRIES):
        if not region_by_country[a]:
            continue
        ra = _REGION_TO_INDEX[region_by_country[a]]
        for b in adjacency[a]:
            if not region_by_country[b]:
                continue
            rb = _REGION_TO_INDEX[region_by_country[b]]
            if ra != rb:
                region_neighbor_regions[ra].add(rb)

    region_pool_indices: list[torch.Tensor] = []
    block_query_indices: list[torch.Tensor] = []
    block_kv_indices: list[torch.Tensor] = []
    dense_mask_bias = torch.full((NUM_COUNTRIES, NUM_COUNTRIES), float("-inf"))

    for region_idx in range(len(MERGED_REGIONS)):
        query_ids = torch.tensor(region_country_lists[region_idx], dtype=torch.long)
        allowed_regions = {region_idx, *region_neighbor_regions[region_idx]}
        allowed_countries = sorted(
            country_id
            for ridx in allowed_regions
            for country_id in region_country_lists[ridx]
        )
        kv_ids = torch.tensor(allowed_countries, dtype=torch.long)
        region_pool_indices.append(query_ids)
        block_query_indices.append(query_ids)
        block_kv_indices.append(kv_ids)
        dense_mask_bias[query_ids.unsqueeze(1), kv_ids.unsqueeze(0)] = 0.0

    orphan_ids = [
        country_id
        for country_id, region_name in enumerate(region_by_country)
        if not region_name
    ]
    for orphan_id in orphan_ids:
        orphan_tensor = torch.tensor([orphan_id], dtype=torch.long)
        block_query_indices.append(orphan_tensor)
        block_kv_indices.append(orphan_tensor)
        dense_mask_bias[orphan_id, orphan_id] = 0.0

    dense_pairs = NUM_COUNTRIES * NUM_COUNTRIES
    sparse_pairs = int((dense_mask_bias == 0.0).sum().item())
    return RegionNeighborMetadata(
        region_names=MERGED_REGIONS,
        country_static=country_static,
        region_pool_indices=tuple(region_pool_indices),
        block_query_indices=tuple(block_query_indices),
        block_kv_indices=tuple(block_kv_indices),
        dense_mask_bias=dense_mask_bias,
        dense_pairs=dense_pairs,
        sparse_pairs=sparse_pairs,
    )


class _BaseCountryAttnPrototype(nn.Module):
    """Shared encoder scaffolding for dense/masked/block attention prototypes."""

    embed_dim = 64
    num_heads = 4

    def __init__(self) -> None:
        super().__init__()
        metadata = build_region_neighbor_metadata()
        self.region_names = metadata.region_names
        self.num_regions = len(self.region_names)
        self.num_blocks = len(metadata.block_query_indices)

        self.register_buffer("country_static", metadata.country_static.clone())
        self.register_buffer("dense_mask_bias", metadata.dense_mask_bias.clone())

        for idx, country_ids in enumerate(metadata.region_pool_indices):
            self.register_buffer(f"region_country_idx_{idx}", country_ids.clone())
        for idx, country_ids in enumerate(metadata.block_query_indices):
            self.register_buffer(f"block_query_idx_{idx}", country_ids.clone())
        for idx, country_ids in enumerate(metadata.block_kv_indices):
            self.register_buffer(f"block_kv_idx_{idx}", country_ids.clone())

        self.country_proj = nn.Linear(metadata.country_static.shape[1] + 2, self.embed_dim)
        self.qkv_proj = nn.Linear(self.embed_dim, 3 * self.embed_dim)
        self.attn_out_proj = nn.Linear(self.embed_dim, self.embed_dim)
        self.out_proj = nn.Linear((1 + self.num_regions) * self.embed_dim, INFLUENCE_HIDDEN)

    def _region_country_idx(self, region_idx: int) -> torch.Tensor:
        return getattr(self, f"region_country_idx_{region_idx}")

    def _region_kv_idx(self, region_idx: int) -> torch.Tensor:
        return getattr(self, f"block_kv_idx_{region_idx}")

    def _block_query_idx(self, block_idx: int) -> torch.Tensor:
        return getattr(self, f"block_query_idx_{block_idx}")

    def _block_kv_idx(self, block_idx: int) -> torch.Tensor:
        return getattr(self, f"block_kv_idx_{block_idx}")

    def encode_tokens(self, influence: torch.Tensor) -> torch.Tensor:
        batch_size = influence.shape[0]
        ussr_inf = influence[:, :NUM_COUNTRIES] / 10.0
        us_inf = influence[:, NUM_COUNTRIES:] / 10.0
        static = self.country_static.unsqueeze(0).expand(batch_size, -1, -1)
        dyn = torch.stack([ussr_inf, us_inf], dim=-1)
        per_country_feats = torch.cat([dyn, static], dim=-1)
        return torch.relu(self.country_proj(per_country_feats))

    def project_qkv(
        self, tokens: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        batch_size, seq_len, embed_dim = tokens.shape
        head_dim = embed_dim // self.num_heads
        qkv = self.qkv_proj(tokens)
        q, k, v = qkv.chunk(3, dim=-1)
        q = q.view(batch_size, seq_len, self.num_heads, head_dim).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.num_heads, head_dim).transpose(1, 2)
        v = v.view(batch_size, seq_len, self.num_heads, head_dim).transpose(1, 2)
        return q, k, v

    def pool_output(self, attn_out: torch.Tensor) -> torch.Tensor:
        pools = [attn_out.mean(dim=1)]
        for region_idx in range(self.num_regions):
            country_ids = self._region_country_idx(region_idx)
            pools.append(attn_out.index_select(1, country_ids).mean(dim=1))
        concat = torch.cat(pools, dim=-1)
        return torch.relu(self.out_proj(concat))


class DenseCountryAttnPrototype(_BaseCountryAttnPrototype):
    """Full dense self-attention over all 86 countries."""

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        tokens = self.encode_tokens(influence)
        q, k, v = self.project_qkv(tokens)
        attn_out = F.scaled_dot_product_attention(q, k, v)
        attn_out = attn_out.transpose(1, 2).contiguous().view(
            influence.shape[0], NUM_COUNTRIES, self.embed_dim
        )
        attn_out = self.attn_out_proj(attn_out)
        return self.pool_output(attn_out)


class MaskedRegionNeighborCountryAttnEncoder(_BaseCountryAttnPrototype):
    """Dense attention with a region-neighbor mask."""

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        tokens = self.encode_tokens(influence)
        q, k, v = self.project_qkv(tokens)
        attn_mask = self.dense_mask_bias.to(device=q.device, dtype=q.dtype)
        attn_out = F.scaled_dot_product_attention(q, k, v, attn_mask=attn_mask)
        attn_out = attn_out.transpose(1, 2).contiguous().view(
            influence.shape[0], NUM_COUNTRIES, self.embed_dim
        )
        attn_out = self.attn_out_proj(attn_out)
        return self.pool_output(attn_out)


class BlockRegionNeighborCountryAttnEncoder(_BaseCountryAttnPrototype):
    """Block attention over merged-region query blocks and neighbor-region keys."""

    def forward(self, influence: torch.Tensor) -> torch.Tensor:
        tokens = self.encode_tokens(influence)
        q, k, v = self.project_qkv(tokens)
        batch_size = influence.shape[0]
        head_dim = self.embed_dim // self.num_heads
        attn_out = torch.empty(
            (batch_size, self.num_heads, NUM_COUNTRIES, head_dim),
            device=q.device,
            dtype=q.dtype,
        )

        for block_idx in range(self.num_blocks):
            query_ids = self._block_query_idx(block_idx)
            kv_ids = self._block_kv_idx(block_idx)
            q_block = q.index_select(2, query_ids)
            k_block = k.index_select(2, kv_ids)
            v_block = v.index_select(2, kv_ids)
            block_out = F.scaled_dot_product_attention(q_block, k_block, v_block)
            attn_out.index_copy_(2, query_ids, block_out)

        attn_out = attn_out.transpose(1, 2).contiguous().view(
            batch_size, NUM_COUNTRIES, self.embed_dim
        )
        attn_out = self.attn_out_proj(attn_out)
        return self.pool_output(attn_out)
