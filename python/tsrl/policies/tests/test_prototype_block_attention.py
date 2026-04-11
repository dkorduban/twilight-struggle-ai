from __future__ import annotations

import torch
from tsrl.policies.prototypes.country_block_attention import (
    INFLUENCE_DIM,
    BlockRegionNeighborCountryAttnEncoder,
    MaskedRegionNeighborCountryAttnEncoder,
    build_region_neighbor_metadata,
)


def test_region_neighbor_metadata_pair_count() -> None:
    metadata = build_region_neighbor_metadata()
    assert metadata.dense_pairs == 86 * 86
    assert metadata.sparse_pairs == 4582


def test_block_matches_masked_dense_forward() -> None:
    torch.manual_seed(0)
    masked = MaskedRegionNeighborCountryAttnEncoder()
    block = BlockRegionNeighborCountryAttnEncoder()
    block.load_state_dict(masked.state_dict())

    influence = torch.randn(4, INFLUENCE_DIM)
    masked_out = masked(influence)
    block_out = block(influence)

    assert torch.allclose(block_out, masked_out, atol=1e-5, rtol=1e-5)


def test_block_matches_masked_dense_input_grad() -> None:
    torch.manual_seed(1)
    masked = MaskedRegionNeighborCountryAttnEncoder()
    block = BlockRegionNeighborCountryAttnEncoder()
    block.load_state_dict(masked.state_dict())

    influence_masked = torch.randn(2, INFLUENCE_DIM, requires_grad=True)
    influence_block = influence_masked.detach().clone().requires_grad_(True)

    masked_loss = masked(influence_masked).square().mean()
    block_loss = block(influence_block).square().mean()
    masked_loss.backward()
    block_loss.backward()

    assert torch.allclose(
        influence_block.grad,
        influence_masked.grad,
        atol=1e-5,
        rtol=1e-5,
    )
