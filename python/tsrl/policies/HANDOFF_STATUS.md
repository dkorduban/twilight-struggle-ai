state: completed
iteration: 20260327_iter9_influence_bonus_v2
baseline_log_dir: /home/dkord/code/twilight-struggle-ai/.claude/worktrees/heuristic-policy-worker/python/tsrl/policies/rollout_logs/20260327_iter8_coup_milops_urgency_v2
baseline_modes: influence=456,coup=214,event=100
baseline_end_reasons: turn_limit=5
baseline_blind_spots: non_coup_milops_penalty=391,offside_ops_penalty=267,control_break=231
change: influence_mode_bonus 6.0->5.0
new_log_dir: /home/dkord/code/twilight-struggle-ai/.claude/worktrees/heuristic-policy-worker/python/tsrl/policies/rollout_logs/20260327_iter9_influence_bonus_v2
new_modes: coup=307,influence=262,event=88,space=3
new_end_reasons: turn_limit=4,europe_control=1
new_blind_spots: milops_urgency=302,coup_access_open=236,offside_ops_penalty=206,non_coup_milops_penalty=206
benchmark_chunks: seed_20260500 old=12.0 new=8.0 draws=2; seed_20260510 old=11.0 new=9.0 draws=0; seed_20260520 old=9.5 new=10.5 draws=1; seed_20260530 old=11.0 new=9.0 draws=0; seed_20260540 old=9.5 new=10.5 draws=1; seed_20260550 old=8.0 new=12.0 draws=0; seed_20260560 old=12.0 new=8.0 draws=0; seed_20260570 old=12.5 new=7.5 draws=1; seed_20260580 old=8.5 new=11.5 draws=1; seed_20260590 old=7.0 new=13.0 draws=0
benchmark_aggregate: total_games=200,draws=6,old_points=101.0,new_points=99.0,old_wr=50.50,new_wr=49.50,delta=-1.00
checks_run: uv run pytest -n 0 test_policy_prefers_friendly_ops_card_over_offside_ops_card PASS; uv run pytest -n 0 test_policy_uses_coup_when_milops_shortfall_is_urgent PASS; uv run pytest -n 0 test_policy_avoids_defcon3_battleground_coup_without_milops_urgency PASS; uv run python -m tsrl.policies.generate_minimal_hybrid_rollout_logs attempted; uv run python fallback log generation for 5 seeds PASS; uv run python -m tsrl.policies.benchmark_winrate_symmetric chunked across 100 paired seeds PASS
next_step: iteration 5 should start from /home/dkord/code/twilight-struggle-ai/.claude/worktrees/heuristic-policy-worker/python/tsrl/policies/rollout_logs/20260327_iter9_influence_bonus_v2; top blind spot is now milops_urgency=302, followed by coup_access_open=236 and offside_ops_penalty/non_coup_milops_penalty tie at 206
