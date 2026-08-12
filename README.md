# MLOps Assignment 4 - Model Monitoring

Repository for ADSP 31021 Assignment #4 (cancer mortality regression + Evidently monitoring).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name mlops_assign4 --display-name "Python (mlops_assign4)"
```

`cancer_reg.csv` should already be under `data/`.

**Important:** Task 5 uses Evidently `0.4.40` (classic API). Select the **`Python (mlops_assign4)`** kernel in Jupyter — not `mlops_assign3` (Evidently 0.7.x has a different API and will fail on `ColumnMapping`).

## Run

```bash
jupyter lab notebooks/model_monitoring.ipynb
```

## Status

- **Task 1** — Dataset loading and data understanding
- **Task 2** — Preprocessing and train/test split
- **Task 3** — Baseline Random Forest model
- **Task 4** — Baseline evaluation (metrics + figures)
- **Task 5** — Evidently monitoring setup
- **Task 6** — Modified test datasets
- **Task 7** — Scenario scoring + metrics summary
- Tasks 8–9 — pending
