"""Numbers the P2 manuscript quotes from H15-E02 that its copied tables give only in prose.

Reads the copied tables in evidence/H15-E02/tables/ and evidence/H14-E02/tables/ only:

    python evidence/H15-E02/derived/h15_summary.py

The slopes use the bootstrap of `experiments/h15_report.py::slope` (datasets resampled
10,000 times, seed 20200), so the H15-only row matches tables/slope.csv.
Writes evidence/H15-E02/derived/summary.csv.
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parents[1]
N_BOOT, BOOT_SEED = 10_000, 20200


def slope(d, fits) -> tuple[float, float, float]:
    x, y = np.log(np.asarray(d, float)), np.log(np.asarray(fits, float))
    b = float(np.polyfit(x, y, 1)[0])
    rng = np.random.default_rng(BOOT_SEED)
    bs = []
    for _ in range(N_BOOT):
        i = rng.integers(0, len(x), len(x))
        if len(set(x[i])) < 2:
            continue
        bs.append(np.polyfit(x[i], y[i], 1)[0])
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return b, float(lo), float(hi)


def main() -> None:
    per = pd.read_csv(EVIDENCE / "H15-E02" / "tables" / "per_dataset.csv")
    runs = pd.read_csv(EVIDENCE / "H15-E02" / "tables" / "runs.csv")
    h14 = pd.read_csv(EVIDENCE / "H14-E02" / "tables" / "run_measures.csv")
    h14 = h14[(h14.method == "p2_obl_b10") & h14.ttr_reached]
    h14_med = h14.groupby("dataset").agg(d=("d", "first"), fits=("ttr_fits", "median"))
    pred = dict(zip(per.dataset, per.predicted))
    runs["ratio"] = runs.ttr_fits / runs.dataset.map(pred)

    rows = []
    for name, d, fits in [
        ("slope_h15_medians", per.d, per.median_fits_to_reach),
        ("slope_h15_seeds", runs.d, runs.ttr_fits),
        ("slope_h14_h15_medians", list(h14_med.d) + list(per.d),
         list(h14_med.fits) + list(per.median_fits_to_reach)),
    ]:
        b, lo, hi = slope(d, fits)
        rows.append({"quantity": name, "value": b, "lo": lo, "hi": hi, "n": len(d)})
    rows += [
        {"quantity": "geomean_ratio_datasets", "value": float(np.exp(per.log_ratio.mean())),
         "n": len(per)},
        {"quantity": "seed_ratio_min", "value": float(runs.ratio.min()), "n": len(runs)},
        {"quantity": "seed_ratio_max", "value": float(runs.ratio.max()), "n": len(runs)},
        {"quantity": "seeds_outside_factor2", "value": int((np.abs(np.log(runs.ratio)) > np.log(2)).sum()),
         "n": len(runs)},
        {"quantity": "max_share_of_cap", "value": float((runs.fits / runs.cap).max()), "n": len(runs)},
        {"quantity": "spearman_ratio_d", "value": float(spearmanr(per.d, per.ratio)[0]), "n": len(per)},
        {"quantity": "spearman_ratio_train_rows",
         "value": float(spearmanr(per.n_train, per.ratio)[0]), "n": len(per)},
    ]
    keys = ["quantity", "value", "lo", "hi", "n"]
    with open(HERE / "summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{r[k]:.6g}" if isinstance(r.get(k), float) else r.get(k, ""))
                        for k in keys})
    print(f"wrote {HERE / 'summary.csv'} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
