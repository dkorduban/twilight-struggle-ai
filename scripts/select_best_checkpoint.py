#!/usr/bin/env python3
"""
Benchmark iter checkpoints from a PPO run and promote the best to ppo_best.pt.
Usage: uv run python scripts/select_best_checkpoint.py <out_dir> [--n-games N]
"""
import sys, os, shutil, argparse, glob, time
sys.path.insert(0, 'build-ninja/bindings')
import tscore


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('out_dir', help='PPO output directory (e.g. results/ppo_gnn_card_attn_v1)')
    parser.add_argument('--n-games', type=int, default=150, help='Games per side per checkpoint')
    parser.add_argument('--every', type=int, default=10, help='Evaluate every N checkpoints (step)')
    parser.add_argument('--min-iter', type=int, default=100, help='Skip checkpoints before this iter')
    parser.add_argument('--dry-run', action='store_true', help='Print results but do not copy')
    args = parser.parse_args()

    pattern = os.path.join(args.out_dir, '*_scripted.pt')
    all_ckpts = sorted(glob.glob(pattern))

    # Filter to iter checkpoints (not ppo_best_scripted, ppo_running_best_scripted, etc.)
    iter_ckpts = []
    for c in all_ckpts:
        basename = os.path.basename(c)
        if 'iter' in basename and 'scripted' in basename:
            # Extract iter number
            try:
                parts = basename.split('iter')
                iter_num = int(parts[-1].replace('_scripted.pt', ''))
                if iter_num >= args.min_iter:
                    iter_ckpts.append((iter_num, c))
            except ValueError:
                pass

    # Apply every-N step filter
    iter_ckpts = [(n, c) for n, c in iter_ckpts if n % args.every == 0]
    iter_ckpts.sort()

    if not iter_ckpts:
        print(f"No iter checkpoints found in {args.out_dir} (min_iter={args.min_iter}, every={args.every})")
        sys.exit(1)

    print(f"Benchmarking {len(iter_ckpts)} checkpoints, N={args.n_games}/side")
    print(f"  {[n for n, _ in iter_ckpts]}")

    best_combined = -1.0
    best_ckpt = None

    for iter_num, ckpt in iter_ckpts:
        t0 = time.perf_counter()
        ru = tscore.benchmark_batched(ckpt, tscore.Side.USSR, args.n_games, seed=50000)
        rr = tscore.benchmark_batched(ckpt, tscore.Side.US, args.n_games, seed=50500)
        wr_u = sum(1 for x in ru if x.winner == tscore.Side.USSR) / args.n_games
        wr_r = sum(1 for x in rr if x.winner == tscore.Side.US) / args.n_games
        comb = (wr_u + wr_r) / 2
        elapsed = time.perf_counter() - t0
        star = ' ← BEST' if comb > best_combined else ''
        print(f"  iter{iter_num:04d}: USSR={wr_u:.3f} US={wr_r:.3f} combined={comb:.3f}  ({elapsed:.0f}s){star}", flush=True)
        if comb > best_combined:
            best_combined = comb
            best_ckpt = ckpt

    print(f"\nBest: {os.path.basename(best_ckpt)} combined={best_combined:.3f}")

    if args.dry_run:
        print("(dry-run: not copying)")
        return

    # Promote to ppo_best.pt
    best_pt = best_ckpt.replace('_scripted.pt', '.pt')
    dst_scripted = os.path.join(args.out_dir, 'ppo_best_scripted.pt')
    dst_pt = os.path.join(args.out_dir, 'ppo_best.pt')

    if os.path.exists(best_ckpt):
        shutil.copy2(best_ckpt, dst_scripted)
        print(f"Copied {best_ckpt} → {dst_scripted}")
    if os.path.exists(best_pt):
        shutil.copy2(best_pt, dst_pt)
        print(f"Copied {best_pt} → {dst_pt}")

    print(f"ppo_best.pt promoted from iter{[n for n, c in iter_ckpts if c == best_ckpt][0]:04d} (combined={best_combined:.3f})")


if __name__ == '__main__':
    main()
