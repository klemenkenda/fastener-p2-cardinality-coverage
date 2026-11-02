"""Figures for the P2 manuscript, drawn from the copied H13-E01 tables.

Run from the repository root:  python manuscript/figures/make_figures.py
Reads evidence/H13-E01/tables/ only and writes vector PDFs next to this file.
Every style value is in STYLE, CONFIG and GRIDS; see manuscript/FIGURE-STYLE.md.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "evidence" / "H13-E01" / "tables"
OUT = Path(__file__).resolve().parent

MM = 1 / 25.4
FULL_WIDTH = 125 * MM

STYLE = {
    "ink": "#0b0b0b",
    "secondary": "#52514e",
    "muted": "#898781",
    "grid": "#e1e0d9",
}

# Colour, marker and line follow the configuration in every figure.
CONFIG = {
    "nsga2": dict(label="OBL start", color="#2a78d6", marker="o", ls="-"),
    "nsga2_sparse": dict(label="Sparse start", color="#eb6834", marker="s", ls="-"),
    "nsgaii_miip": dict(label="NSGAII-MIIP", color="#1baf7a", marker="^", ls="-"),
}
# A difference "a minus b" is drawn in the colour of configuration a; most are sparse minus OBL.
SPARSE = CONFIG["nsga2_sparse"]["color"]
# Classes that are not configurations (parts of a difference, analysis variants, classifiers)
# take these colours in order, each class its own; validated as a set on white (FIGURE-STYLE.md).
CLASS_COLORS = ["#6250d6", "#eda100", "#e87ba4", "#008300"]  # violet, yellow, magenta, green
CLASS_MARKERS = ["o", "s", "D", "v"]

# The pilot (H14-E02). Its two starts over all sizes take the first two class colours; they never
# share a panel with the OBL start, because violet and blue fail the all-pairs check.
PILOT = ROOT / "evidence" / "H14-E02" / "tables"
PILOT_DATASETS = ["Adiac", "Strawberry", "Earthquakes", "Computers"]  # by number of features
PILOT_START = {
    "p2_obl": dict(label="OBL start", color=CONFIG["nsga2"]["color"], marker="o"),
    "p2_sparse": dict(label="Sparse start", color=SPARSE, marker="s"),
    "p2_uniform": dict(label="Uniform start", color=CLASS_COLORS[0], marker="D"),
    "p2_loguniform": dict(label="Log-uniform start", color=CLASS_COLORS[1], marker="v"),
}
# Balanced against forced-flip mutation: the next two class colours.
MUTATION = {"": dict(label="Balanced mutation", color=CLASS_COLORS[2], marker="o"),
            "_min1": dict(label="Forced flip", color=CLASS_COLORS[3], marker="s")}
GRIDS = {
    "H1-E02": "Decision tree (designed)",
    "H5H6-E01": "Decision tree",
    "H5H6-E02": "Random forest",
    "H5H6-E03": "LightGBM",
}
BENCH = ["H5H6-E01", "H5H6-E02", "H5H6-E03"]
# Tick labels for the four groups of runs, in GRIDS order.
GROUP_TICKS = ["Decision\ntree\n(designed)", "Decision\ntree", "Random\nforest", "LightGBM"]


def setup() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["STIXGeneral", "Times New Roman"],
        "mathtext.fontset": "stix",
        "font.size": 8,
        "axes.titlesize": 8,
        "axes.labelsize": 8,
        "legend.fontsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "axes.edgecolor": STYLE["secondary"],
        "axes.linewidth": 0.6,
        "axes.labelcolor": STYLE["ink"],
        "axes.titlecolor": STYLE["ink"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": STYLE["grid"],
        "grid.linewidth": 0.4,
        "grid.linestyle": "-",
        "xtick.color": STYLE["secondary"],
        "ytick.color": STYLE["secondary"],
        "xtick.labelcolor": STYLE["ink"],
        "ytick.labelcolor": STYLE["ink"],
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.minor.width": 0.4,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "xtick.minor.size": 1.5,
        "lines.linewidth": 1.0,
        "lines.markersize": 3.5,
        "legend.frameon": False,
        "pdf.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
    })


def plain_number(x: float, _pos=None) -> str:
    if x <= 0:
        return ""
    if x >= 1:
        return f"{x:,.0f}"
    return f"{x:g}"


def log_axis(ax, which: str = "x") -> None:
    axis = ax.xaxis if which == "x" else ax.yaxis
    (ax.set_xscale if which == "x" else ax.set_yscale)("log")
    axis.set_major_locator(LogLocator(base=10))
    axis.set_major_formatter(FuncFormatter(plain_number))
    axis.set_minor_formatter(NullFormatter())


def baseline(ax, y: float = 0.0) -> None:
    ax.axhline(y, color=STYLE["secondary"], lw=0.6, zorder=1)


def legend_above(fig, methods, extra=()) -> None:
    handles = [plt.Line2D([], [], color=CONFIG[m]["color"], marker=CONFIG[m]["marker"],
                          ls=CONFIG[m]["ls"], label=CONFIG[m]["label"]) for m in methods]
    handles += list(extra)
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0),
               ncol=len(handles), handlelength=2.2, columnspacing=1.4)


def grid_panels(nrows=2, ncols=2, height=80, sharey=True):
    fig, axes = plt.subplots(nrows, ncols, figsize=(FULL_WIDTH, height * MM),
                             sharex=True, sharey=sharey, constrained_layout=True)
    return fig, axes.ravel()


def save(fig, name: str) -> None:
    fig.savefig(OUT / f"{name}.pdf")
    plt.close(fig)
    print("wrote", name)


def runs() -> pd.DataFrame:
    return pd.read_csv(TABLES / "run_measures.csv")


def seed_means(r: pd.DataFrame) -> pd.DataFrame:
    return (r.groupby(["grid", "dataset", "method"])
             .agg(d=("d", "first"), auf=("auf_k10", "mean"), reach=("reach_k10", "mean"),
                  best_f1=("best_f1", "mean"), max_front=("max_front", "median"))
             .reset_index())


def obl_start_reach(d: int, K: int = 10, pairs: int = 50) -> float:
    """P(an opposition-based population of `pairs` pairs holds a subset of 1..K features)."""
    logs = []
    for m in range(d + 1):
        if (1 <= m <= K) or (1 <= d - m <= K):
            logs.append(math.lgamma(d + 1) - math.lgamma(m + 1) - math.lgamma(d - m + 1) - d * math.log(2))
    p_pair = sum(math.exp(x) for x in logs) if logs else 0.0
    return 1.0 - (1.0 - min(p_pair, 1.0)) ** pairs


def kaplan_meier(times, events):
    """Share reached by each time: 1 - S(t), right-censored at the end of the budget."""
    t = np.asarray(times, float)
    e = np.asarray(events, bool)
    order = np.argsort(t)
    t, e = t[order], e[order]
    at_risk, surv, xs, ys = len(t), 1.0, [], []
    for u in np.unique(t):
        here = t == u
        d = int(e[here].sum())
        if d:
            surv *= 1 - d / at_risk
            xs.append(u)
            ys.append(1 - surv)
        at_risk -= int(here.sum())
    return np.array(xs), np.array(ys)


def offset(method: str, step: float) -> float:
    return {"nsga2": -step, "nsga2_sparse": 0.0, "nsgaii_miip": step}[method]


# ----------------------------------------------------------------- figures
def fig_reach_quality() -> None:
    t = pd.read_csv(TABLES / "q1_terms.csv")
    fig, axes = grid_panels(height=78)
    for ax, (g, title) in zip(axes, GRIDS.items()):
        s = t[t.grid == g]
        ax.scatter(s.d, s.reach_term, s=14, color=CLASS_COLORS[0], marker=CLASS_MARKERS[0],
                   lw=0.4, edgecolor="white", zorder=3, label="Reach part")
        ax.scatter(s.d, s.quality_term, s=14, color=CLASS_COLORS[1], marker=CLASS_MARKERS[1],
                   lw=0.4, edgecolor="white", zorder=4, label="Quality part")
        baseline(ax)
        log_axis(ax)
        ax.set_title(title)
        ax.set_ylim(-0.25, 1.05)
    for ax in axes[2:]:
        ax.set_xlabel("Features $d$")
    for ax in axes[::2]:
        ax.set_ylabel("AUF difference,\nsparse minus OBL start")
    h, lab = axes[1].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    save(fig, "fig_reach_quality")


def fig_reach_vs_d() -> None:
    q = pd.read_csv(TABLES / "q2_reach_by_dataset.csv")
    fig, axes = grid_panels(height=78)
    dd = np.unique(np.round(np.logspace(np.log10(10), np.log10(250_000), 400)).astype(int))
    analytic = np.array([obl_start_reach(int(x)) if x <= 400 else 0.0 for x in dd])
    for ax, (g, title) in zip(axes, GRIDS.items()):
        ax.plot(dd, analytic, color=STYLE["muted"], lw=0.8, zorder=2)
        for m in CONFIG:
            s = q[(q.grid == g) & (q.method == m)]
            if s.empty:
                continue
            c = CONFIG[m]
            ax.plot(s.d, s.reach_front_end + offset(m, 0.03), ls="none", marker=c["marker"],
                    color=c["color"], mec="white", mew=0.4, zorder=3)
        log_axis(ax)
        ax.set_title(title)
        ax.set_ylim(-0.08, 1.08)
    axes[0].annotate("OBL start at\ninitialization", xy=(40, 0.2), xytext=(70, 0.45),
                     color=STYLE["secondary"], fontsize=7,
                     arrowprops=dict(arrowstyle="-", color=STYLE["muted"], lw=0.6))
    for ax in axes[2:]:
        ax.set_xlabel("Features $d$")
    for ax in axes[::2]:
        ax.set_ylabel("Share of runs that\nreach ten features")
    legend_above(fig, CONFIG)
    save(fig, "fig_reach_vs_d")


def fig_time_to_reach() -> None:
    r = runs()
    fig, axes = grid_panels(height=78)
    for ax, (g, title) in zip(axes, GRIDS.items()):
        for m in CONFIG:
            s = r[(r.grid == g) & (r.method == m)]
            if s.empty:
                continue
            x, y = kaplan_meier(s.ttr_share, s.ttr_reached)
            x = np.concatenate([[0.005], x, [1.0]])
            y = np.concatenate([[0.0], y, [y[-1] if len(y) else 0.0]])
            c = CONFIG[m]
            ax.step(x, y, where="post", color=c["color"], ls=c["ls"], zorder=3)
        log_axis(ax)
        ax.set_xlim(0.005, 1.0)
        ax.set_ylim(-0.03, 1.03)
        ax.set_title(title)
    for ax in axes[2:]:
        ax.set_xlabel("Share of the fit budget spent")
    for ax in axes[::2]:
        ax.set_ylabel("Share of runs that\nhave reached ten features")
    handles = [plt.Line2D([], [], color=CONFIG[m]["color"], ls=CONFIG[m]["ls"],
                          label=CONFIG[m]["label"]) for m in CONFIG]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3,
               handlelength=2.6)
    save(fig, "fig_time_to_reach")


def fig_large_end() -> None:
    m = seed_means(runs())
    fig, (a, b) = plt.subplots(1, 2, figsize=(FULL_WIDTH, 62 * MM), constrained_layout=True,
                               gridspec_kw=dict(width_ratios=[1, 1.15]))
    rng = np.random.default_rng(20200)
    for i, g in enumerate(GRIDS):
        p = m[m.grid == g].pivot(index="dataset", columns="method", values="best_f1")
        diff = (p["nsga2_sparse"] - p["nsga2"]).dropna()
        x = i + rng.uniform(-0.18, 0.18, len(diff))
        a.scatter(x, diff, s=10, color=SPARSE, edgecolor="white", lw=0.4, zorder=3)
        a.plot([i - 0.28, i + 0.28], [diff.mean()] * 2, color=STYLE["ink"], lw=1.4, zorder=4)
    baseline(a)
    a.set_xticks(range(len(GRIDS)), GROUP_TICKS)
    a.grid(axis="x", visible=False)
    a.set_ylabel("Best test F1 at any size,\nsparse minus OBL start")
    a.set_title("(a) Best score")
    pooled = (m[m.grid.isin(BENCH) | (m.grid == "H1-E02")]
              .groupby(["dataset", "method"]).agg(d=("d", "first"), max_front=("max_front", "median"))
              .reset_index())
    for meth, c in CONFIG.items():
        s = pooled[pooled.method == meth]
        b.plot(s.d, s.max_front, ls="none", marker=c["marker"], color=c["color"], mec="white",
               mew=0.4, zorder=3)
    dd = np.logspace(1, np.log10(250_000), 50)
    b.plot(dd, dd / 2, color=STYLE["muted"], lw=0.8, zorder=2)
    b.text(3_000, 3_000 / 2 * 2.2, "$d/2$", color=STYLE["secondary"], fontsize=7)
    log_axis(b, "x")
    log_axis(b, "y")
    b.set_xlabel("Features $d$")
    b.set_ylabel("Largest subset on the front")
    b.set_title("(b) Largest subset")
    legend_above(fig, CONFIG)
    save(fig, "fig_large_end")


def fig_three_arms() -> None:
    m = seed_means(runs())
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 58 * MM), sharey=True,
                             constrained_layout=True)
    rng = np.random.default_rng(20200)
    pairs = [("nsgaii_miip", "nsga2", "(a) NSGAII-MIIP minus OBL start"),
             ("nsga2_sparse", "nsgaii_miip", "(b) Sparse start minus NSGAII-MIIP")]
    for ax, (ma, mb, title) in zip(axes, pairs):
        for i, g in enumerate(BENCH):
            p = m[m.grid == g].pivot(index="dataset", columns="method", values="reach")
            diff = (p[ma] - p[mb]).dropna()
            x = i + rng.uniform(-0.18, 0.18, len(diff))
            ax.scatter(x, diff, s=10, color=CONFIG[ma]["color"], edgecolor="white", lw=0.4,
                       zorder=3)
            ax.plot([i - 0.28, i + 0.28], [diff.mean()] * 2, color=STYLE["ink"], lw=1.4, zorder=4)
        baseline(ax)
        ax.set_xticks(range(3), ["Decision\ntree", "Random\nforest", "LightGBM"])
        ax.grid(axis="x", visible=False)
        ax.set_title(title)
    axes[0].set_ylabel("Difference in the share of\nruns that reach ten features")
    save(fig, "fig_three_arms")


def fig_repeats() -> None:
    q = pd.read_csv(TABLES / "q8_by_dataset.csv")
    fig, axes = grid_panels(height=74)
    for ax, (g, title) in zip(axes, GRIDS.items()):
        for meth in ["nsga2", "nsga2_sparse"]:
            s = q[(q.grid == g) & (q.method == meth)]
            c = CONFIG[meth]
            ax.plot(s.d, s.median_repeat_share, ls="none", marker=c["marker"], color=c["color"],
                    mec="white", mew=0.4, zorder=3)
        log_axis(ax)
        ax.set_ylim(-0.03, 1.03)
        ax.set_title(title)
    for ax in axes[2:]:
        ax.set_xlabel("Features $d$")
    for ax in axes[::2]:
        ax.set_ylabel("Share of proposed subsets\nalready evaluated")
    legend_above(fig, ["nsga2", "nsga2_sparse"])
    save(fig, "fig_repeats")


def fig_missing() -> None:
    q = pd.read_csv(TABLES / "q5_sensitivity.csv")
    variants = {"S0": "As registered", "S1": "Complete datasets",
                "S2": "Missing as no reach", "S3": "Shared datasets"}
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 55 * MM), constrained_layout=True)
    for ax, part, col, title in [(axes[0], "a", "mean_delta", "(a) Difference in reach"),
                                 (axes[1], "c", "share", "(b) Reach part of the AUF difference")]:
        for j, (v, lab) in enumerate(variants.items()):
            s = q[(q.variant == v) & (q.part == part)].set_index("grid")
            ys = [s.loc[g, col] if g in s.index else np.nan for g in GRIDS]
            xs = np.arange(len(GRIDS)) + (j - 1.5) * 0.14
            ax.plot(xs, ys, ls="none", marker=CLASS_MARKERS[j], ms=4.2, color=CLASS_COLORS[j],
                    mec="white", mew=0.4, label=lab, zorder=3)
        ax.set_xticks(range(len(GRIDS)), GROUP_TICKS)
        ax.grid(axis="x", visible=False)
        ax.set_title(title)
    axes[0].set_ylim(0, 1)
    axes[0].set_ylabel("Mean over datasets")
    axes[1].set_ylim(0.9, 1.005)
    axes[1].set_ylabel("Share")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=4, handletextpad=0.3)
    save(fig, "fig_missing")


def fig_classifier() -> None:
    """The classifier moves the scores but not the comparison: each dataset under the random
    forest and LightGBM against the decision tree, (a) the sparse start's AUF lead, which stays
    on the diagonal, and (b) the sparse start's own AUF, which lies above it."""
    m = seed_means(runs())
    m = m[m.grid.isin(BENCH)]
    p = m.pivot_table(index=["dataset", "grid"], columns="method", values="auf").reset_index()
    p["lead"] = p["nsga2_sparse"] - p["nsga2"]
    lead = p.pivot(index="dataset", columns="grid", values="lead").dropna()
    own = p.pivot(index="dataset", columns="grid", values="nsga2_sparse").loc[lead.index]
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 64 * MM), constrained_layout=True)
    others = [("H5H6-E02", "Random forest"), ("H5H6-E03", "LightGBM")]
    panels = [(axes[0], lead, (-0.05, 1.05), "(a) AUF lead of the sparse start",
               "Lead under the decision tree", "Lead under the other classifier"),
              (axes[1], own, (0.15, 1.02), "(b) AUF of the sparse start",
               "AUF under the decision tree", "AUF under the other classifier")]
    for ax, w, lim, title, xl, yl in panels:
        ax.plot(lim, lim, color=STYLE["muted"], lw=0.8, zorder=2)
        for j, (g, lab) in enumerate(others):
            ax.plot(w["H5H6-E01"], w[g], ls="none", marker=CLASS_MARKERS[j], ms=3.8,
                    color=CLASS_COLORS[j], mec="white", mew=0.4, label=lab, zorder=3)
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_aspect("equal")
        ax.set_title(title)
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
    axes[0].text(0.30, 0.25, "same as under the tree", color=STYLE["secondary"], fontsize=7,
                 rotation=45, rotation_mode="anchor", ha="left", va="top")
    axes[1].text(0.22, 0.95, "above the line:\nhigher than under the tree", color=STYLE["secondary"],
                 fontsize=7, ha="left", va="top")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    save(fig, "fig_classifier")
    print(f"  common datasets: {len(lead)}")


# ------------------------------------------------------------------ pilot
def pilot_runs() -> pd.DataFrame:
    return pd.read_csv(PILOT / "run_measures.csv")


def pilot_title(ax, r: pd.DataFrame, ds: str) -> None:
    d = int(r.loc[r.dataset == ds, "d"].iloc[0])
    ax.set_title(f"{ds} ($d$ = {d})")


def fig_pilot_budget() -> None:
    """When the OBL start reaches ten features, in multiples of the benchmark budget."""
    r = pilot_runs()
    s10 = r[r.method == "p2_obl_b10"]
    fig, axes = grid_panels(height=74)
    c = CONFIG["nsga2"]
    for ax, ds in zip(axes, PILOT_DATASETS):
        s = s10[s10.dataset == ds]
        x, y = kaplan_meier(s.ttr_fits / s.base_budget, s.ttr_reached)
        x = np.concatenate([[0.005], x, [10.0]])
        y = np.concatenate([[0.0], y, [y[-1] if len(y) else 0.0]])
        ax.step(x, y, where="post", color=c["color"], zorder=3)
        for b, lab in [(1, "1×"), (3, "3×")]:
            ax.axvline(b, color=STYLE["muted"], lw=0.6, zorder=2)
            ax.text(b * 1.08, 0.04, lab, color=STYLE["secondary"], fontsize=7)
        log_axis(ax)
        ax.set_xlim(0.005, 10)
        ax.set_ylim(-0.03, 1.03)
        pilot_title(ax, r, ds)
    for ax in axes[2:]:
        ax.set_xlabel("Fits, in multiples of the benchmark budget")
    for ax in axes[::2]:
        ax.set_ylabel("Share of OBL runs that\nhave reached ten features")
    save(fig, "fig_pilot_budget")


def fig_pilot_starts() -> None:
    """Starts over all sizes against the sparse start, per seed (horizontal strips)."""
    r = pilot_runs().set_index(["method", "dataset", "seed"]).sort_index()
    d = r.reset_index().groupby("dataset").d.first()
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 58 * MM), sharey=True,
                             constrained_layout=True)
    measures = [("best_f1", "(a) Best test F1 at any size"), ("auf_k10", "(b) AUF, limit of ten")]
    rows = list(reversed(PILOT_DATASETS))  # widest dataset at the bottom
    for ax, (col, title) in zip(axes, measures):
        for j, m in enumerate(["p2_uniform", "p2_loguniform"]):
            st = PILOT_START[m]
            for i, ds in enumerate(rows):
                diff = (r.loc[(m, ds)][col] - r.loc[("p2_sparse", ds)][col]).dropna()
                y = i + (0.5 - j) * 0.3 + np.linspace(-0.06, 0.06, len(diff))
                ax.plot(diff, y, ls="none", marker=st["marker"], color=st["color"], mec="white",
                        mew=0.4, label=st["label"] if i == 0 else None, zorder=3)
                yc = i + (0.5 - j) * 0.3
                ax.plot([diff.mean()] * 2, [yc - 0.11, yc + 0.11], color=STYLE["ink"], lw=1.2,
                        zorder=4)
        ax.axvline(0, color=STYLE["secondary"], lw=0.6, zorder=1)
        ax.set_yticks(range(4), [f"{ds} ($d$ = {d[ds]})" for ds in rows])
        ax.grid(axis="y", visible=False)
        ax.set_title(title)
        ax.set_xlabel("Difference from the sparse start")
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    save(fig, "fig_pilot_starts")


def fig_pilot_unchanged() -> None:
    """Children left unchanged by balanced mutation against 2k/d, with exp(-2k/d)."""
    s = pd.read_csv(PILOT / "subset_summary.csv")
    fig, axes = grid_panels(height=74)
    xx = np.logspace(-3, 0.2, 100)
    for ax, (m, st) in zip(axes, PILOT_START.items()):
        q = s[s.method == m]
        ax.plot(xx, np.exp(-xx), color=STYLE["muted"], lw=0.8, zorder=2)
        ax.plot(q.expected_flips_2k_over_d, q.unchanged_share, ls="none", marker=st["marker"],
                color=st["color"], mec="white", mew=0.4, zorder=3)
        log_axis(ax)
        ax.set_xlim(0.004, 1.5)
        ax.set_ylim(0.3, 1.03)
        ax.set_title(st["label"])
    axes[0].text(0.012, 0.86, "$e^{-2k/d}$", color=STYLE["secondary"], fontsize=8)
    for ax in axes[2:]:
        ax.set_xlabel("Expected changed features $2k/d$")
    for ax in axes[::2]:
        ax.set_ylabel("Share of children left\nunchanged by mutation")
    save(fig, "fig_pilot_unchanged")


def fig_pilot_min1() -> None:
    """Forced flip against balanced mutation: repeats, proposals per new fit, AUF
    (horizontal strips, starts on a shared axis)."""
    s = pd.read_csv(PILOT / "subset_summary.csv")
    s["per_fit"] = s.proposals / s.new_fits
    r = pilot_runs().set_index(["method", "dataset", "seed"]).sort_index()
    rows = list(reversed(PILOT_START))  # OBL start at the top
    # Narrower than FULL_WIDTH: the tight bounding box adds the start labels on the left.
    fig, axes = plt.subplots(1, 3, figsize=(FULL_WIDTH - 3 * MM, 52 * MM), sharey=True,
                             constrained_layout=True)
    for ax, col in [(axes[0], "repeat_share"), (axes[1], "per_fit")]:
        for j, (suf, mu) in enumerate(MUTATION.items()):
            for i, m in enumerate(rows):
                q = s[s.method == m + suf][col]
                y = i + (0.5 - j) * 0.32 + np.linspace(-0.08, 0.08, len(q))
                ax.plot(q, y, ls="none", marker=mu["marker"], ms=2.8, color=mu["color"],
                        mec="white", mew=0.3, label=mu["label"] if i == 0 else None, zorder=3)
    for i, m in enumerate(rows):
        diff = (r.loc[m + "_min1"]["auf_k10"] - r.loc[m]["auf_k10"]).dropna()
        y = i + np.linspace(-0.15, 0.15, len(diff))
        axes[2].plot(diff, y, ls="none", marker=MUTATION["_min1"]["marker"], ms=2.8,
                     color=MUTATION["_min1"]["color"], mec="white", mew=0.3, zorder=3)
        axes[2].plot([diff.mean()] * 2, [i - 0.2, i + 0.2], color=STYLE["ink"], lw=1.2, zorder=4)
    axes[2].axvline(0, color=STYLE["secondary"], lw=0.6, zorder=1)
    log_axis(axes[1], "x")
    axes[0].set_xlim(-0.03, 1.03)
    axes[0].set_yticks(range(4), [PILOT_START[m]["label"] for m in rows])
    for ax, title, xl in zip(axes, ["(a) Repeated proposals", "(b) Proposals per new fit",
                                    "(c) AUF, forced minus balanced"],
                             ["Share already evaluated", "Proposals per new fit",
                              "Difference (same seed)"]):
        ax.grid(axis="y", visible=False)
        ax.set_title(title)
        ax.set_xlabel(xl)
    h, lab = axes[0].get_legend_handles_labels()
    fig.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    save(fig, "fig_pilot_min1")


if __name__ == "__main__":
    setup()
    for f in (fig_reach_quality, fig_reach_vs_d, fig_time_to_reach, fig_large_end,
              fig_three_arms, fig_repeats, fig_missing, fig_classifier,
              fig_pilot_budget, fig_pilot_starts, fig_pilot_unchanged, fig_pilot_min1):
        f()
