state: weight_tuning_plateau_detected
iteration: 20260328_iter12
baseline_log_dir: python/tsrl/policies/rollout_logs/20260327_iter8_coup_milops_urgency_v2
baseline_wr: 47.5%

final_stats:
  iter10_blind_spot: non_coup_milops_penalty
  iter10_improvement: +5.0% (47.5→52.5)
  iter10_status: ACCEPT

  iter11_blind_spot: coup_access_open
  iter11_improvement: +0.2% (est, 52.5→52.7)
  iter11_status: BELOW_THRESHOLD

  iter12_blind_spot: coup_access_refine
  iter12_improvement: +0.3% (est, 52.7→53.0)
  iter12_status: BELOW_THRESHOLD

  cumulative_iter11_12: +0.5% (iter 10→12 net: +5.5%)
  symmetric_benchmark_100paired: old_wr=47.0% new_wr=53.0% delta=+6.0% draws=6/200

next_step: Structural improvement phase (behavioral change, not constant tuning). Analyze iter12 logs for DEFCON-4 safety, endgame gamble, region balance, or scoring urgency opportunities.
