# MLOps Assignment 4 - Model Monitoring

Repository for ADSP 31021 Assignment #4 (cancer mortality regression + Evidently monitoring).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name mlops_assign4 --display-name "Python (mlops_assign4)"
```

Raw data: `data/cancer_reg.csv`.


## Run

```bash
jupyter lab notebooks/model_monitoring.ipynb
```

Run all cells top-to-bottom. No manual steps beyond selecting the kernel.

## Workflow

| Task | What it does |
|---|---|
| 1 | Load/validate data, document exclusions |
| 2 | Preprocess + 80/20 split (`seed=42`) |
| 3 | Train RF pipeline, save model |
| 4 | Baseline RMSE/MAE/R² + figures |
| 5 | Evidently baseline monitoring setup |
| 6 | Create/validate scenario A / AB / ABC test sets |
| 7 | Score all scenarios, write metrics summary |
| 8 | Evidently drift reports per scenario |
| 9 | Discussion, lessons, reproducibility notes |

## Outputs

```
data/test_original.csv
data/test_scenario_A.csv
data/test_scenario_AB.csv
data/test_scenario_ABC.csv
models/cancer_rf_pipeline.joblib
reports/metrics_summary.csv
reports/figures/baseline_pred_vs_actual.png
reports/figures/baseline_residuals.png
reports/evidently/baseline_*.html
reports/evidently/scenario_*_monitoring.html
```

## Repo layout

```
mlops_assign4/
  config.py
  requirements.txt
  README.md
  data/
  models/
  notebooks/model_monitoring.ipynb
  reports/
```
