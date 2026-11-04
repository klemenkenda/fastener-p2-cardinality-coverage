# Reproducing the numbers in the paper

*Cardinality Coverage in Evolutionary Feature Selection: A Budget-Aware Study of Initialization and Search Operators*

The paper has three layers, each reproducible from the one below it:

1. **Runs.** The NSGA-II searches were run in [`fastener-experiments`](https://github.com/klemenkenda/fastener-experiments), with the FASTENER components in [`FASTENER`](https://github.com/klemenkenda/FASTENER). Each run's log is distilled into `experiments/distilled_logs/<experiment>/{runs,records,curves,jobs}.csv.xz`. A log holds the returned front, the archive after every generation, fits, generations, the stopping cause, the time, and the commit.
2. **Analysis tables.** `h13_report.py`, `h14_report.py` and `h15_report.py` in `fastener-experiments` compute the tables from the distilled logs. The tables used by the paper are copied unchanged into [`evidence/`](evidence/), with SHA-256 manifests. The first-revision statistics in [`evidence/R1/`](evidence/R1/) are computed by [`review_supplement.py`](evidence/R1/review_supplement.py), and the H15-E02 numbers that its report gives only in prose (the slope pooled with H14-E02, ratios, correlations) by [`h15_summary.py`](evidence/H15-E02/derived/h15_summary.py) from the copied tables.
3. **Paper.** The figures come from [`manuscript/figures/make_figures.py`](manuscript/figures/make_figures.py), the supplementary tables from [`manuscript/supplement/make_tables.py`](manuscript/supplement/make_tables.py), and the PDFs from `latexmk`.

No new model fits are needed for layers 2 and 3.

## Commits

| What | Repository | Commit | Notes |
|---|---|---|---|
| Distilled logs, H14-E02 report, R1 statistics | fastener-experiments | `e44fd74` | `evidence/H14-E02/`, `evidence/R1/` |
| H13-E01 report with the 50-test-row tables (DEC-57) | fastener-experiments | `354c307` | `evidence/H13-E01/` |
| H15-E02 report (confirmatory test, DEC-59, DEC-60) and its distilled logs | fastener-experiments | `aa909ee` | `evidence/H15-E02/` |
| FASTENER components read by the analysis | FASTENER | `047e1fb` | needed by `_bootstrap.py` |
| Designed experiment (H1-E02) | fastener-experiments + FASTENER | `c142251` + `08e6acd` | recorded per run |
| Decision-tree benchmark (H5H6-E01) | fastener-experiments + FASTENER | `33fa95e`, `2e7a100`, `d2102c5` + `3be5697` | recorded per run |
| Random-forest benchmark (H5H6-E02) | fastener-experiments | `5efd5a3`, `f3eb230` | **not recorded**: reconstructed from the cluster clone's history (DEC-43) |
| LightGBM benchmark (H5H6-E03) | fastener-experiments + FASTENER | `fbbecfe` + `3be5697` | recorded per run |
| Pilot (H14-E02) | fastener-experiments + FASTENER | `75e638d` + `047e1fb` | recorded per run |
| Confirmatory test (H15-E02) | fastener-experiments + FASTENER | `f47c368` + `047e1fb` | recorded per run, `code_dirty: false` |

Runs started with `--experiment` refuse a working tree with uncommitted code; no algorithm ID of the analyzed runs carries the `-dirty` suffix. The runs' `dirty` flag also counts non-code paths such as results and reports, so it is set for some runs whose code was clean.

## Data and splits

- The datasets are downloaded with the `download_*.py` scripts of `fastener-experiments` and listed in Table 2 of the paper.
- Every dataset is split once into stratified training, validation, and test parts in the proportions 60/20/20 (`datasets.py`: `VAL_FRACTION = TEST_FRACTION = 0.20`, `SPLIT_SEED = 20200`). The split is the same for every seed and configuration.
- Time series archives merge their own train and test parts before the split. Multivariate series are flattened channel by channel. Nothing is scaled, and rows with missing values are dropped.
- EOData, and crop_mapping and volkert in the confirmatory test, are cut to a fixed stratified sample of 50,000 rows with the same seed (`protocol.ROW_CAP`).
- Classifiers use `random_state = 20200` (`protocol.MODEL_SEED`). Search seeds are 2020–2024, 2025–2029 in the pilot, and 2030–2034 in the confirmatory test. The budget calibration used seed 1999 (`calibrate_budget.py`).

## Environment

Library versions are not stored per run. The experiment records give:

- Python 3.11 and NumPy 2;
- scikit-learn 1.9.0 on the workstation (designed experiment, decision-tree benchmark, pilot) and 1.9.1 on the Vega cluster (random forest, LightGBM);
- LightGBM ≥ 4.0 as required by `requirements.txt`; the exact version is not recorded.

The analysis layer was rerun on 3 November 2026 with Python 3.13.2, NumPy 2.4.2, pandas 3.0.3, SciPy 1.18.1, and scikit-learn 1.9.1. It gave the tables in `evidence/` to floating-point precision.

## Commands

```text
git clone https://github.com/klemenkenda/fastener-experiments FX
git -C FX checkout e44fd74
git clone https://github.com/klemenkenda/FASTENER FX/fastener
git -C FX/fastener checkout 047e1fb
pip install -r FX/requirements.txt

# layer 2: analysis tables (written under FX/experiments/reports/)
python FX/experiments/h13_report.py
python FX/experiments/h13_report.py --min-test-rows 50   # exploratory check (DEC-57)
python FX/experiments/h14_report.py

# layer 2: first-revision statistics (written to evidence/R1/tables/)
python evidence/R1/review_supplement.py --fx FX

# layer 2: confirmatory test (H15-E02), from the later commit
git -C FX checkout aa909ee
python FX/experiments/h15_report.py
python evidence/H15-E02/derived/h15_summary.py   # reads evidence/ only

# layer 3: figures, supplementary tables, PDFs
python manuscript/figures/make_figures.py
python manuscript/supplement/make_tables.py
cd manuscript && latexmk main.tex
cd supplement && pdflatex supplement.tex
```

To check copied tables against their sources, compare their SHA-256 hashes with the `PROVENANCE.json` file in each `evidence/` subfolder.

## Known gaps

- The commits of the random-forest runs are reconstructed, not recorded.
- Exact library versions, including LightGBM's, are not stored per run.
- The NSGAII-MIIP implementation is a Python port of the authors' MATLAB code. Its outputs were not compared with those of the original code, which needs MATLAB and Weka.
- The pilot's subset logs do not store the sizes of mutated children, so Fig. 9 uses the median size of newly evaluated subsets as an approximation.
