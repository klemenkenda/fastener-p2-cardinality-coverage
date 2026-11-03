"""Tables of the supplementary material, generated from the evidence CSVs.

Run from the repository root:  python manuscript/supplement/make_tables.py
Reads evidence/H13-E01/tables/ and evidence/R1/tables/ and writes tables.tex
next to this file; supplement.tex inputs it.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
H13 = ROOT / "evidence" / "H13-E01" / "tables"
R1 = ROOT / "evidence" / "R1" / "tables"
OUT = Path(__file__).resolve().parent / "tables.tex"
GROUP = {"H1-E02": "Decision tree (designed)", "H5H6-E01": "Decision tree",
         "H5H6-E02": "Random forest", "H5H6-E03": "LightGBM"}
BENCH = ["H5H6-E01", "H5H6-E02", "H5H6-E03"]


def num(x, nd=3, sign=True):
    if pd.isna(x):
        return "--"
    s = f"{x:+.{nd}f}" if sign else f"{x:.{nd}f}"
    return s.replace("-", "$-$")


def pval(p):
    return "$<$0.001" if p < 0.001 else f"{p:.3f}"


def effects() -> str:
    df = pd.concat([pd.read_csv(H13 / f) for f in
                    ("q3_pairs.csv", "q4_large_end.csv", "q7_rmst.csv")])
    rows = [("R", "nsga2_sparse", "nsga2", "Reach, sparse $-$ OBL"),
            ("R", "nsgaii_miip", "nsga2", "Reach, MIIP $-$ OBL"),
            ("R", "nsga2_sparse", "nsgaii_miip", "Reach, sparse $-$ MIIP"),
            ("auf_k10", "nsga2_sparse", "nsga2", "AUF$_{10}$, sparse $-$ OBL"),
            ("auf_k10", "nsgaii_miip", "nsga2", "AUF$_{10}$, MIIP $-$ OBL"),
            ("auf_k10", "nsga2_sparse", "nsgaii_miip", "AUF$_{10}$, sparse $-$ MIIP"),
            ("auf_k20", "nsga2_sparse", "nsga2", "AUF$_{20}$, sparse $-$ OBL"),
            ("auf_kd", "nsga2_sparse", "nsga2", "AUF$_{d}$, sparse $-$ OBL"),
            ("best_f1", "nsga2_sparse", "nsga2", "Best F1, sparse $-$ OBL"),
            ("best_f1", "nsga2_sparse", "nsgaii_miip", "Best F1, sparse $-$ MIIP"),
            ("max_front", "nsga2_sparse", "nsga2", "Largest subset, sparse $-$ OBL"),
            ("rmst_share", "nsga2_sparse", "nsga2", "Time to reach, sparse $-$ OBL"),
            ("rmst_share", "nsgaii_miip", "nsga2", "Time to reach, MIIP $-$ OBL")]
    lines = []
    for m, a, b, label in rows:
        cells = [label]
        for g in BENCH:
            r = df[(df.grid == g) & (df.measure == m) & (df.a == a) & (df.b == b)].iloc[0]
            nd = 1 if m == "max_front" else 3
            cells += [num(r.mean_delta, nd),
                      f"[{num(r.mean_lo, nd)}, {num(r.mean_hi, nd)}]",
                      num(r.rank_biserial, 2), pval(r.p_holm)]
        lines.append(" & ".join(cells) + r" \\")
    body = "\n".join(lines)
    return r"""
\begin{table}[!htbp]
\caption{Principal paired comparisons in the benchmark, datasets as units: mean difference, 95\%
bootstrap interval over datasets, matched-pairs rank-biserial correlation $r$, and Holm-corrected
Wilcoxon $p$ over the three pairs of configurations within a group and measure. Time to reach:
restricted mean share of the budget spent before the archive holds a subset with at most ten
features. Largest subset: number of features of the largest subset on the returned front}
\label{tab:s-effects}
\centering\tiny\setlength{\tabcolsep}{2pt}
\begin{tabular}{@{}lrcrrrcrrrcrr@{}}
\toprule
 & \multicolumn{4}{c}{Decision tree} & \multicolumn{4}{c}{Random forest} & \multicolumn{4}{c}{LightGBM} \\
\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(l){10-13}
Comparison & Mean & 95\% CI & $r$ & $p$ & Mean & 95\% CI & $r$ & $p$ & Mean & 95\% CI & $r$ & $p$ \\
\midrule
""" + body + r"""
\bottomrule
\end{tabular}
\end{table}
"""


def attribution() -> str:
    df = pd.read_csv(R1 / "attribution.csv")
    lines = []
    for _, r in df.iterrows():
        pct = lambda x: f"{100 * x:.1f}"
        lines.append(" & ".join([
            GROUP[r.grid], str(int(r.n_datasets)), num(r.auf_delta_mean),
            num(r.reach_term_mean), num(r.quality_term_mean),
            f"{pct(r.signed_share)} [{pct(r.signed_share_lo)}, {pct(r.signed_share_hi)}]",
            f"{pct(r.abs_share)} [{pct(r.abs_share_lo)}, {pct(r.abs_share_hi)}]",
            f"{pct(r.obl_never_share)} [{pct(r.obl_never_lo)}, {pct(r.obl_never_hi)}]",
            f"{int(r.datasets_negative_quality)}/{int(r.datasets_positive_quality)}"]) + r" \\")
    return r"""
\begin{table}[!htbp]
\caption{Split of the AUF difference (sparse minus OBL start, $K = 10$) into reach and quality
parts (Eq.~2 of the paper), by group. Mean over datasets of $\Delta$, $\rho$, and $\kappa$; signed
share $S$ and absolute share $A$ (Eq.~3), in percent with 95\% bootstrap intervals over datasets;
the share of the net difference that comes from limits the OBL start never reaches on a dataset;
and the numbers of datasets with a negative and a positive quality part}
\label{tab:s-attribution}
\centering\scriptsize\setlength{\tabcolsep}{2.5pt}
\begin{tabular}{@{}lrrrrlll c@{}}
\toprule
Group & Data & $\bar\Delta$ & $\bar\rho$ & $\bar\kappa$ & $S$ & $A$ & OBL never & $\kappa<0$/$\kappa>0$ \\
\midrule
""" + "\n".join(lines) + r"""
\bottomrule
\end{tabular}
\end{table}
"""


def matched() -> str:
    df = pd.read_csv(R1 / "matched_by_dataset.csv")
    df = df[df["matched"].notna()].sort_values(["grid", "d", "dataset"])
    lines = []
    for _, r in df.iterrows():
        lines.append(" & ".join([
            GROUP[r.grid], r.dataset.replace("_", r"\_"), f"{int(r.d):,}".replace(",", "{,}"),
            str(int(r.n_test)), str(int(r.matched_k)), num(r.matched),
            str(int(r.paired_seeds)), num(r.paired_mean), num(r.paired_min), num(r.paired_max)])
            + r" \\")
    return r"""
\begin{table}[!htbp]
\caption{Matched-size difference in test F1, sparse minus OBL start, for every dataset on which
it is defined. $|M|$: number of limits up to ten that both starts reach in at least three of five
seeds; $m$: matched-size difference; seed-paired: number of seeds with a shared reached limit,
mean, minimum, and maximum of the per-seed differences. Datasets with at most 50 test rows are
left out only in the exploratory analysis}
\label{tab:s-matched}
\centering\scriptsize\setlength{\tabcolsep}{3pt}
\begin{tabular}{@{}llrrrrrrrr@{}}
\toprule
 & & & & & & \multicolumn{4}{c}{Seed-paired} \\
\cmidrule(l){7-10}
Group & Dataset & $d$ & Test rows & $|M|$ & $m$ & Seeds & Mean & Min & Max \\
\midrule
""" + "\n".join(lines) + r"""
\bottomrule
\end{tabular}
\end{table}
"""


def completion_d50_pilot() -> str:
    c = pd.read_csv(R1 / "completion.csv")
    label = {"nsga2": "OBL start", "nsga2_sparse": "Sparse start", "nsgaii_miip": "NSGAII-MIIP"}
    lines = [" & ".join([GROUP[r.grid], label[r.method], str(int(r.finished)), str(int(r.planned)),
                         f"{100 * r.share:.0f}\\%"]) + r" \\" for _, r in c.iterrows()]
    d = pd.read_csv(R1 / "d50.csv")
    dl = [" & ".join([GROUP[r.grid], label[r.method], f"{r.d50:.0f}", f"[{r.lo:.0f}, {r.hi:.0f}]",
                      str(int(r.n_finite))]) + r" \\" for _, r in d.iterrows()]
    p = pd.read_csv(R1 / "pilot_first_hit.csv")
    pl = [" & ".join([r.dataset, str(int(r.d)), f"{int(r.base_budget):,}".replace(",", "{,}"),
                      f"{r.median_first_hit_fits:,.0f}".replace(",", "{,}"),
                      f"{r.min_first_hit_fits:,.0f}".replace(",", "{,}") + "--" +
                      f"{r.max_first_hit_fits:,.0f}".replace(",", "{,}"),
                      f"{r.budgets_to_reach:.2f}", f"{r.fits_per_feature:.0f}"]) + r" \\"
          for _, r in p.iterrows()]
    return r"""
\begin{table}[!htbp]
\caption{Finished runs out of planned runs, by group and configuration}
\label{tab:s-completion}
\centering\scriptsize
\begin{tabular}{@{}llrrr@{}}
\toprule
Group & Configuration & Finished & Planned & Share \\
\midrule
""" + "\n".join(lines) + r"""
\bottomrule
\end{tabular}
\end{table}

\begin{table}[!htbp]
\caption{Number of features at which half of the runs reach ten features, from the logistic model
of reach on $\log_2 d$ and $\log_2$ of the budget, at the median budget of 6{,}000 fits; 95\%
percentile interval over 2{,}000 bootstrap resamples of datasets (resamples in which all runs
agree are skipped). Descriptive locations for these datasets and budgets}
\label{tab:s-d50}
\centering\scriptsize
\begin{tabular}{@{}llrlr@{}}
\toprule
Group & Configuration & $d_{50}$ & 95\% CI & Resamples \\
\midrule
""" + "\n".join(dl) + r"""
\bottomrule
\end{tabular}
\end{table}

\begin{table}[!htbp]
\caption{Pilot: fits until the archive of an OBL run with ten times the budget first holds a subset
with at most ten features; median and range over five seeds, in multiples of the benchmark budget,
and per feature}
\label{tab:s-pilot}
\centering\scriptsize
\begin{tabular}{@{}lrrrlrr@{}}
\toprule
Dataset & $d$ & Budget & Median fits & Range & Budgets & Fits per feature \\
\midrule
""" + "\n".join(pl) + r"""
\bottomrule
\end{tabular}
\end{table}
"""


def main() -> None:
    OUT.write_text("% Generated by make_tables.py; do not edit.\n" + effects() + attribution()
                   + matched() + completion_d50_pilot(), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
