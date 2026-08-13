"""Paths, constants, and modeling knobs for Assignment 4 — Model Monitoring."""

from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_CSV = DATA_DIR / "cancer_reg.csv"

TEST_ORIGINAL_CSV = DATA_DIR / "test_original.csv"
TEST_SCENARIO_A_CSV = DATA_DIR / "test_scenario_A.csv"
TEST_SCENARIO_AB_CSV = DATA_DIR / "test_scenario_AB.csv"
TEST_SCENARIO_ABC_CSV = DATA_DIR / "test_scenario_ABC.csv"

MODELS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODELS_DIR / "cancer_rf_pipeline.joblib"

REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
EVIDENTLY_DIR = REPORTS_DIR / "evidently"
METRICS_SUMMARY_CSV = REPORTS_DIR / "metrics_summary.csv"

# Reproducibility
SEED = 42
TEST_SIZE = 0.2

# Target (CSV name; assignment text uses target_deathrate)
TARGET = "TARGET_deathRate"

# Scenario mutation columns (CSV names; assignment text uses lowercase aliases)
COL_MEDIAN_INCOME = "medIncome"
COL_POVERTY = "povertyPercent"
COL_AVG_HH_SIZE = "AvgHouseholdSize"

SCENARIO_A_INCOME_DELTA = -40_000
SCENARIO_B_POVERTY_DELTA = 20
SCENARIO_C_HH_SIZE_DELTA = 2

# Columns excluded from modeling
EXCLUDE_COLUMNS = [
    "Geography",  # high-cardinality county identifier
    "binnedInc",  # redundant with medIncome
    "PctSomeCol18_24",  # ~75% missing
]

# Columns with invalid values to nullify before imputation
MEDIAN_AGE_COL = "MedianAge"
MEDIAN_AGE_MAX_VALID = 100

# Encoding for cancer_reg.csv (contains non-UTF8 characters in Geography)
CSV_ENCODING = "latin-1"

# Random Forest hyperparameters
RF_N_ESTIMATORS = 200
RF_MAX_DEPTH = 16
RF_MIN_SAMPLES_LEAF = 2
RF_N_JOBS = -1
