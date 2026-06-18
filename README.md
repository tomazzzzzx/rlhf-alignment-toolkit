# RLHF Alignment Toolkit

RLHF and DPO training toolkit for aligning LLMs with human preferences.

## Methods
- PPO with KL penalty
- DPO (Direct Preference Optimization)
- ORPO (Odds Ratio Preference Optimization)
- Reward model training with pairwise loss

## Pipeline
1. Train reward model on human preferences
2. Generate responses with SFT model
3. Optimize policy with PPO/DPO
4. Evaluate on MT-Bench, AlpacaEval

## License: MIT
