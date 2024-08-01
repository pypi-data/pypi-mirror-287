# costa-utils

This repo contains some personal utilities to do quick things. Currently we have



## dev note

```bash
python costa_utils/hf_viz.py \
    --preference HuggingFaceH4/ultrafeedback_binarized \
    --split train_prefs \
    --preference_chosen_column_name chosen \
    --preference_rejected_column_name rejected
```