"""Figures for the P2 manuscript, drawn from the copied H13-E01 tables.

Run from the repository root:  python manuscript/figures/make_figures.py
Reads evidence/H13-E01/tables/ only and writes vector PDFs next to this file.
Every style value is in STYLE, MARK, CONFIG, NEUTRAL, PILOT_START, GRIDS and ANNOT;
see manuscript/FIGURE-STYLE.md.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator, MaxNLocator, NullFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "evidence" / "H13-E01" / "tables"
OUT = Path(__file__).resolve().parent

MM = 1 / 25.4
FULL_WIDTH = 125 * MM

STYLE = {
    "ink": "#1a1d23",
    "secondary": "#5a606b",
    "muted": "#9aa0a8",
    "grid": "#e9ebee",
}

# One mark everywhere: a filled circle, partly transparent and without an edge, so that points
# drawn on top of each other read as a darker spot. Colour alone names the series.
MARK = dict(ls="none", marker="o", ms=3.6, mew=0, alpha=0.55)

# Colour is reserved for configurations and is the same in every figure (FIGURE-STYLE.md).
# Every line is solid; no configuration is singled out by a dash.
CONFIG = {
    "nsga2": dict(label="OBL start", color="#285fa8"),
    "nsga2_sparse": dict(label="Sparse start", color="#e07434"),
    "nsgaii_miip": dict(label="NSGAII-MIIP", color="#2a9d8f"),
}
# A difference "a minus b" is drawn in the colour of configuration a; most are sparse minus OBL.
SPARSE = CONFIG["nsga2_sparse"]["color"]
# Classes that are not configurations (parts of a difference, analysis variants, classifiers,
# mutation operators) are neutral: dark slate first, then light grey; mid grey only for a third.
NEUTRAL = {"dark": "#2f3b4c", "mid": "#6e7783", "light": "#a7aeb8"}
# Neutral classes are told apart by lightness, which strong transparency would wash out.
NEUTRAL_ALPHA = 0.8

# The pilot (H14-E02). Its two starts over all sizes are plum and ochre; they never share a panel
# with the OBL or sparse start, because no five hues pass the all-pairs check together.
PILOT = ROOT / "evidence" / "H14-E02" / "tables"
PILOT_DATASETS = ["Adiac", "Strawberry", "Earthquakes", "Computers"]  # by number of features
PILOT_START = {
    "p2_obl": dict(label="OBL start", color=CONFIG["nsga2"]["color"]),
    "p2_sparse": dict(label="Sparse start", color=SPARSE),
    "p2_uniform": dict(label="Uniform start", color="#7e57a6"),
    "p2_loguniform": dict(label="Log-uniform start", color="#b5891c"),
}
# Balanced against forced-flip mutation: operators, so neutral.
MUTATION = {"": dict(label="Balanced mutation", color=NEUTRAL["light"]),
            "_min1": dict(label="Forced flip", color=NEUTRAL["dark"])}
GRIDS = {
    "H1-E02": "Decision tree (designed)",
    "H5H6-E01": "Decision tree",
    "H5H6-E02": "Random forest",
    "H5H6-E03": "LightGBM",
}
BENCH = ["H5H6-E01", "H5H6-E02", "H5H6-E03"]
# Tick labels for the four groups of runs, in GRIDS order, when the groups run along x.
GROUP_TICKS = ["Tree\n(designed)", "Tree", "Forest", "LightGBM"]
BENCH_TICKS = ["Decision\ntree", "Random\nforest", "LightGBM"]
# Annotations and direct labels: the tick size, never smaller.
ANNOT = 9
# One-line names, when the groups run down the y axis.
GROUP_NAMES = list(GRIDS.values())


def setup() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["STIXGeneral", "Times New Roman"],
        "mathtext.fontset": "stix",
        "font.size": 10,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 10,
        "legend.fontsize": 9,
        "legend.labelcolor": STYLE["secondary"],
        "figure.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.edgecolor": STYLE["secondary"],
        "axes.linewidth": 0.6,
        "axes.titlepad": 4,
        "axes.labelpad": 3,
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
        "ytick.minor.width": 0.4,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "xtick.minor.size": 1.5,
        "ytick.minor.size": 1.5,
        "lines.linewidth": 1.2,
        "lines.solid_capstyle": "round",
        "lines.markersize": MARK["ms"],
        "legend.frameon": False,
        "legend.handletextpad": 0.4,
        "legend.columnspacing": 1.6,
        "legend.borderaxespad": 0.2,
        "pdf.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
    })


def plain_number(x: float, _pos=None) -> str:
    if x <= 0:
        return ""
    if x >= 1000:
        return f"{x / 1000:,.0f}k"
    if x >= 1:
        return f"{x:,.0f}"
    return f"{x:g}"


def log_axis(ax, which: str = "x") -> None:
    axis = ax.xaxis if which == "x" else ax.yaxis
    (ax.set_xscale if which == "x" else ax.set_yscale)("log")
    axis.set_major_locator(LogLocator(base=10))
    axis.set_major_formatter(FuncFormatter(plain_number))
    axis.set_minor_formatter(NullFormatter())


def baseline(ax, y: float = 0.0, axis: str = "y") -> None:
    (ax.axhline if axis == "y" else ax.axvline)(y, color=STYLE["secondary"], lw=0.6, zorder=1)


def dots(ax, x, y, color, label=None, zorder=3, **kw) -> None:
    if color in NEUTRAL.values():
        kw = {"alpha": NEUTRAL_ALPHA, **kw}
    ax.plot(x, y, color=color, label=label, zorder=zorder, **{**MARK, **kw})


def mean_bar(ax, centre, value, half=0.28, axis="x", ci=None) -> None:
    """A mean as a short ink bar across a strip; `axis` is the axis the strips run along.
    `ci` = (low, high) adds the 95% interval of the mean as a thin ink line through the bar."""
    span = [centre - half, centre + half]
    xs, ys = (span, [value] * 2) if axis == "x" else ([value] * 2, span)
    ax.plot(xs, ys, color=STYLE["ink"], lw=1.4, solid_capstyle="butt", zorder=4)
    if ci is not None:
        xs, ys = ([centre] * 2, list(ci)) if axis == "x" else (list(ci), [centre] * 2)
        ax.plot(xs, ys, color=STYLE["ink"], lw=0.8, solid_capstyle="butt", zorder=4)


def mean_ci(values, n_boot: int = 10_000, seed: int = 20200) -> tuple[float, float]:
    """Percentile bootstrap 95% interval of the mean (display only; the tests are in the text)."""
    v = np.asarray(values, float)
    rng = np.random.default_rng(seed)
    means = rng.choice(v, size=(n_boot, len(v)), replace=True).mean(axis=1)
    return tuple(np.percentile(means, [2.5, 97.5]))


def legend_in(ax, entries, kind: str = "dot", loc: str = "upper left", anchor=None) -> None:
    """One legend per figure, inside the first panel where the data leave room (left when
    possible), one entry per row, 9 pt in the secondary ink. `entries` are configuration keys
    or (label, colour) pairs; `anchor` is an optional (x, y) in axes fractions for `loc`."""
    pairs = [(CONFIG[e]["label"], CONFIG[e]["color"]) if isinstance(e, str) else e
             for e in entries]
    if kind == "line":
        handles = [plt.Line2D([], [], color=c, lw=1.6, label=lab) for lab, c in pairs]
        length = 1.8
    else:
        handles = [plt.Line2D([], [], color=c, label=lab, **{**MARK, "ms": 4.2, "alpha": 1})
                   for lab, c in pairs]
        length = 0.8
    kw = dict(bbox_to_anchor=anchor) if anchor else {}
    ax.legend(handles=handles, loc=loc, ncol=1, handlelength=length, labelspacing=0.3,
              borderpad=0.2, **kw)


def group_ticks(ax, labels, axis: str = "x") -> None:
    if axis == "x":
        ax.set_xticks(range(len(labels)), labels, linespacing=0.95)
        ax.grid(axis="x", visible=False)
        ax.tick_params(axis="x", length=0)
    else:
        ax.set_yticks(range(len(labels)), labels)
        ax.grid(axis="y", visible=False)
        ax.tick_params(axis="y", length=0)


def grid_panels(nrows=2, ncols=2, height=80, sharey=True):
    fig, axes = plt.subplots(nrows, ncols, figsize=(FULL_WIDTH, height * MM),
                             sharex=True, sharey=sharey, constrained_layout=True)
    return fig, axes.ravel()


def grid_labels(fig, xlabel: str, ylabel: str) -> None:
    """Shared axis labels for a grid of panels, once for the whole figure."""
    fig.supxlabel(xlabel, color=STYLE["ink"])
    fig.supylabel(ylabel, color=STYLE["ink"])


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
    fig, axes = grid_panels(height=72)
    parts = [("reach_term", "Reach part", NEUTRAL["dark"]),
             ("quality_term", "Quality part", NEUTRAL["light"])]
    for ax, (g, title) in zip(axes, GRIDS.items()):
        s = t[t.grid == g]
        baseline(ax)
        # A thin line joins the two parts of one dataset.
        ax.vlines(s.d, s.quality_term, s.reach_term, color=STYLE["muted"], lw=0.5, zorder=2)
        for j, (col, lab, c) in enumerate(parts):
            dots(ax, s.d, s[col], c, zorder=3 + j)
        log_axis(ax)
        ax.set_title(title)
        ax.set_ylim(-0.25, 1.05)
    grid_labels(fig, "Features $d$", "AUF difference, sparse minus OBL start")
    legend_in(axes[3], [(lab, c) for _, lab, c in parts], loc="upper right")
    save(fig, "fig_reach_quality")


def fig_reach_vs_d() -> None:
    q = pd.read_csv(TABLES / "q2_reach_by_dataset.csv")
    fig, axes = grid_panels(height=72)
    dd = np.unique(np.round(np.logspace(np.log10(10), np.log10(250_000), 400)).astype(int))
    analytic = np.array([obl_start_reach(int(x)) if x <= 400 else 0.0 for x in dd])
    for ax, (g, title) in zip(axes, GRIDS.items()):
        ax.plot(dd, analytic, color=STYLE["muted"], lw=0.8, zorder=2)
        for m in CONFIG:
            s = q[(q.grid == g) & (q.method == m)]
            if not s.empty:
                dots(ax, s.d, s.reach_front_end + offset(m, 0.035), CONFIG[m]["color"])
        log_axis(ax)
        ax.set_title(title)
        ax.set_ylim(-0.08, 1.08)
    axes[0].annotate("OBL start at\ninitialization", xy=(40, 0.2), xytext=(70, 0.45),
                     color=STYLE["secondary"], fontsize=ANNOT,
                     arrowprops=dict(arrowstyle="-", color=STYLE["muted"], lw=0.6))
    grid_labels(fig, "Features $d$", "Share of runs that reach ten features")
    legend_in(axes[0], CONFIG, loc="center right")
    save(fig, "fig_reach_vs_d")


def fig_time_to_reach() -> None:
    r = runs()
    fig, axes = grid_panels(height=72)
    for ax, (g, title) in zip(axes, GRIDS.items()):
        for m in CONFIG:
            s = r[(r.grid == g) & (r.method == m)]
            if s.empty:
                continue
            x, y = kaplan_meier(s.ttr_share, s.ttr_reached)
            x = np.concatenate([[0.005], x, [1.0]])
            y = np.concatenate([[0.0], y, [y[-1] if len(y) else 0.0]])
            ax.step(x, y, where="post", color=CONFIG[m]["color"], zorder=3)
        log_axis(ax)
        ax.set_xlim(0.005, 1.0)
        ax.set_ylim(-0.03, 1.03)
        ax.set_title(title)
    grid_labels(fig, "Share of the fit budget spent", "Share of runs that have reached ten features")
    legend_in(axes[0], CONFIG, kind="line", loc="center left", anchor=(0.27, 0.58))
    save(fig, "fig_time_to_reach")


def fig_large_end() -> None:
    m = seed_means(runs())
    fig, (a, b) = plt.subplots(1, 2, figsize=(FULL_WIDTH, 62 * MM), constrained_layout=True,
                               gridspec_kw=dict(width_ratios=[1.3, 1]))
    rng = np.random.default_rng(20200)
    baseline(a)
    for i, g in enumerate(GRIDS):
        p = m[m.grid == g].pivot(index="dataset", columns="method", values="best_f1")
        diff = (p["nsga2_sparse"] - p["nsga2"]).dropna()
        dots(a, i + rng.uniform(-0.18, 0.18, len(diff)), diff, SPARSE)
        mean_bar(a, i, diff.mean(), ci=mean_ci(diff))
    group_ticks(a, GROUP_TICKS)
    a.set_ylabel("Best test F1 at any size,\nsparse minus OBL start")
    a.set_title("(a) Best score")
    pooled = (m[m.grid.isin(BENCH) | (m.grid == "H1-E02")]
              .groupby(["dataset", "method"]).agg(d=("d", "first"), max_front=("max_front", "median"))
              .reset_index())
    dd = np.logspace(1, np.log10(250_000), 50)
    b.plot(dd, dd / 2, color=STYLE["muted"], lw=0.8, zorder=2)
    b.text(12_000, 12_000 / 2 / 6, "$d/2$", color=STYLE["secondary"], fontsize=ANNOT)
    for meth, c in CONFIG.items():
        s = pooled[pooled.method == meth]
        dots(b, s.d, s.max_front, c["color"])
    log_axis(b, "x")
    log_axis(b, "y")
    b.set_xlabel("Features $d$")
    b.set_ylabel("Largest subset on the front")
    b.set_title("(b) Largest subset")
    legend_in(b, CONFIG)
    save(fig, "fig_large_end")


def fig_three_arms() -> None:
    m = seed_means(runs())
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 58 * MM), sharey=True,
                             constrained_layout=True)
    rng = np.random.default_rng(20200)
    pairs = [("nsgaii_miip", "nsga2", "(a) NSGAII-MIIP minus OBL"),
             ("nsga2_sparse", "nsgaii_miip", "(b) Sparse minus NSGAII-MIIP")]
    for ax, (ma, mb, title) in zip(axes, pairs):
        baseline(ax)
        for i, g in enumerate(BENCH):
            p = m[m.grid == g].pivot(index="dataset", columns="method", values="reach")
            diff = (p[ma] - p[mb]).dropna()
            dots(ax, i + rng.uniform(-0.2, 0.2, len(diff)), diff, CONFIG[ma]["color"])
            mean_bar(ax, i, diff.mean(), half=0.3, ci=mean_ci(diff))
        group_ticks(ax, BENCH_TICKS)
        ax.set_title(title)
    axes[0].set_ylabel("Difference in the share of\nruns that reach ten features")
    save(fig, "fig_three_arms")


def fig_repeats() -> None:
    q = pd.read_csv(TABLES / "q8_by_dataset.csv")
    fig, axes = grid_panels(height=70)
    for ax, (g, title) in zip(axes, GRIDS.items()):
        for meth in ["nsga2", "nsga2_sparse"]:
            s = q[(q.grid == g) & (q.method == meth)]
            dots(ax, s.d, s.median_repeat_share, CONFIG[meth]["color"])
        log_axis(ax)
        ax.set_ylim(-0.03, 1.03)
        ax.set_title(title)
    grid_labels(fig, "Features $d$", "Share of proposed subsets already evaluated")
    legend_in(axes[0], ["nsga2", "nsga2_sparse"], loc="center left")
    save(fig, "fig_repeats")


def fig_missing() -> None:
    """The registered sparse-minus-OBL result in orange; the three sensitivity variants in
    neutral tones, on rows by group of runs."""
    q = pd.read_csv(TABLES / "q5_sensitivity.csv")
    variants = {"S0": ("As registered", SPARSE),
                "S1": ("Complete datasets", NEUTRAL["dark"]),
                "S2": ("Missing as no reach", NEUTRAL["mid"]),
                "S3": ("Shared datasets", NEUTRAL["light"])}
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 48 * MM), sharey=True,
                             constrained_layout=True)
    rows = list(reversed(GRIDS))  # designed experiment at the top
    for ax, part, col, title in [(axes[0], "a", "mean_delta", "(a) Difference in reach"),
                                 (axes[1], "c", "share", "(b) Absolute reach share $A$")]:
        for j, (v, (lab, c)) in enumerate(variants.items()):
            s = q[(q.variant == v) & (q.part == part)].set_index("grid")
            xs = [s.loc[g, col] if g in s.index else np.nan for g in rows]
            ys = np.arange(len(rows)) + (1.5 - j) * 0.16
            dots(ax, xs, ys, c, label=lab, alpha=1)
        group_ticks(ax, [GRIDS[g].replace(" (", "\n(") for g in rows], axis="y")
        ax.set_title(title)
    axes[0].set_xlim(0, 1)
    axes[0].set_xticks([0, 0.25, 0.5, 0.75, 1])
    axes[1].set_xticks([0.90, 0.95, 1.00])
    axes[0].set_xlabel("Mean over datasets")
    axes[1].set_xlim(0.9, 1.005)
    axes[1].set_xlabel("Share")
    axes[0].set_ylim(-0.5, len(rows) - 0.5)
    legend_in(axes[1], list(variants.values()), loc="center left")
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
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 60 * MM), constrained_layout=True)
    others = [("H5H6-E02", "Random forest", NEUTRAL["dark"]),
              ("H5H6-E03", "LightGBM", NEUTRAL["light"])]
    panels = [(axes[0], lead, (-0.05, 1.05), "(a) AUF lead of the sparse start",
               "Lead under the decision tree", "Lead under the other classifier"),
              (axes[1], own, (0.15, 1.02), "(b) AUF of the sparse start",
               "AUF under the decision tree", "AUF under the other classifier")]
    for ax, w, lim, title, xl, yl in panels:
        ax.plot(lim, lim, color=STYLE["muted"], lw=0.8, zorder=2)
        for j, (g, lab, c) in enumerate(others):
            dots(ax, w["H5H6-E01"], w[g], c, zorder=3 + j)
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_aspect("equal")
        ax.set_title(title)
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
    axes[0].text(0.30, 0.25, "same as under the tree", color=STYLE["secondary"], fontsize=ANNOT,
                 rotation=45, rotation_mode="anchor", ha="left", va="top")
    axes[1].text(0.20, 0.99, "above the line:\nhigher than\nunder the tree", color=STYLE["secondary"],
                 fontsize=ANNOT, ha="left", va="top")
    legend_in(axes[0], [(lab, c) for _, lab, c in others])
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
    fig, axes = grid_panels(height=66)
    c = CONFIG["nsga2"]
    for ax, ds in zip(axes, PILOT_DATASETS):
        s = s10[s10.dataset == ds]
        x, y = kaplan_meier(s.ttr_fits / s.base_budget, s.ttr_reached)
        x = np.concatenate([[0.005], x, [10.0]])
        y = np.concatenate([[0.0], y, [y[-1] if len(y) else 0.0]])
        for b, lab in [(1, "1×"), (3, "3×")]:
            ax.axvline(b, color=STYLE["muted"], lw=0.6, zorder=2)
            if ds == PILOT_DATASETS[0]:  # label the budgets once, where no curve crosses
                ax.text(b * 1.08, 0.45, lab, color=STYLE["secondary"], fontsize=ANNOT)
        ax.step(x, y, where="post", color=c["color"], zorder=3)
        log_axis(ax)
        ax.set_xlim(0.005, 10)
        ax.set_ylim(-0.03, 1.03)
        pilot_title(ax, r, ds)
    grid_labels(fig, "Fits, in multiples of the benchmark budget", "Share of OBL runs that have reached ten features")
    save(fig, "fig_pilot_budget")


def fig_pilot_starts() -> None:
    """Starts over all sizes against the sparse start, per seed (horizontal strips)."""
    r = pilot_runs().set_index(["method", "dataset", "seed"]).sort_index()
    d = r.reset_index().groupby("dataset").d.first()
    fig, axes = plt.subplots(1, 2, figsize=(FULL_WIDTH, 58 * MM), sharey=True,
                             constrained_layout=True)
    measures = [("best_f1", "(a) Best test F1, any size"), ("auf_k10", "(b) AUF, limit of ten")]
    rows = list(reversed(PILOT_DATASETS))  # widest dataset at the bottom
    starts = ["p2_uniform", "p2_loguniform"]
    for ax, (col, title) in zip(axes, measures):
        baseline(ax, axis="x")
        for j, m in enumerate(starts):
            for i, ds in enumerate(rows):
                diff = (r.loc[(m, ds)][col] - r.loc[("p2_sparse", ds)][col]).dropna()
                yc = i + (0.5 - j) * 0.3
                dots(ax, diff, yc + np.linspace(-0.06, 0.06, len(diff)), PILOT_START[m]["color"])
                mean_bar(ax, yc, diff.mean(), half=0.11, axis="y")
        group_ticks(ax, [f"{ds}\n($d$ = {d[ds]})" for ds in rows], axis="y")
        ax.xaxis.set_major_locator(MaxNLocator(4))
        ax.set_title(title)
        ax.set_xlabel("Minus the sparse start")
    axes[0].set_ylim(-0.5, len(rows) + 0.25)
    legend_in(axes[0], [(PILOT_START[m]["label"], PILOT_START[m]["color"]) for m in starts])
    save(fig, "fig_pilot_starts")


def fig_pilot_unchanged() -> None:
    """Children left unchanged by balanced mutation against 2k/d, with exp(-2k/d)."""
    s = pd.read_csv(PILOT / "subset_summary.csv")
    fig, axes = grid_panels(height=66)
    xx = np.logspace(-3, 0.2, 100)
    for ax, (m, st) in zip(axes, PILOT_START.items()):
        q = s[s.method == m]
        ax.plot(xx, np.exp(-xx), color=STYLE["muted"], lw=0.8, zorder=2)
        dots(ax, q.expected_flips_2k_over_d, q.unchanged_share, st["color"])
        log_axis(ax)
        ax.set_xlim(0.004, 1.5)
        ax.set_ylim(0.3, 1.03)
        ax.set_title(st["label"])
    axes[0].text(0.012, 0.86, "$e^{-2k/d}$", color=STYLE["secondary"], fontsize=ANNOT)
    grid_labels(fig, "Expected changed features $2k/d$", "Share of children left unchanged by mutation")
    save(fig, "fig_pilot_unchanged")


def fig_pilot_min1() -> None:
    """Forced flip against balanced mutation: repeats, proposals per new fit, AUF
    (horizontal strips, starts on a shared axis)."""
    s = pd.read_csv(PILOT / "subset_summary.csv")
    s["per_fit"] = s.proposals / s.new_fits
    r = pilot_runs().set_index(["method", "dataset", "seed"]).sort_index()
    rows = list(reversed(PILOT_START))  # OBL start at the top
    # Narrower than FULL_WIDTH: the tight bounding box adds the start labels on the left.
    fig, axes = plt.subplots(1, 3, figsize=(FULL_WIDTH, 56 * MM), sharey=True,
                             constrained_layout=True)
    small = dict(ms=3.0, mew=0.4)
    for ax, col in [(axes[0], "repeat_share"), (axes[1], "per_fit")]:
        for j, (suf, mu) in enumerate(MUTATION.items()):
            for i, m in enumerate(rows):
                q = s[s.method == m + suf][col]
                y = i + (0.5 - j) * 0.32 + np.linspace(-0.08, 0.08, len(q))
                dots(ax, q, y, mu["color"], **small)
    baseline(axes[2], axis="x")
    for i, m in enumerate(rows):
        diff = (r.loc[m + "_min1"]["auf_k10"] - r.loc[m]["auf_k10"]).dropna()
        dots(axes[2], diff, i + np.linspace(-0.15, 0.15, len(diff)), MUTATION["_min1"]["color"],
             **small)
        mean_bar(axes[2], i, diff.mean(), half=0.22, axis="y")
    log_axis(axes[1], "x")
    axes[0].set_xlim(-0.03, 1.03)
    axes[2].xaxis.set_major_locator(MaxNLocator(3))
    for ax, title, xl in zip(axes, ["(a) Repeats", "(b) Cost", "(c) AUF change"],
                             ["Share of proposals\nalready evaluated", "Proposals per\nnew fit",
                              "Forced minus\nbalanced, same seed"]):
        group_ticks(ax, [PILOT_START[m]["label"].replace(" start", "") for m in rows], axis="y")
        ax.set_title(title)
        ax.set_xlabel(xl)
    axes[0].set_ylim(-1.75, len(rows) - 0.5)
    legend_in(axes[0], [(mu["label"], mu["color"]) for mu in MUTATION.values()], loc="lower left")
    save(fig, "fig_pilot_min1")


if __name__ == "__main__":
    setup()
    for f in (fig_reach_quality, fig_reach_vs_d, fig_time_to_reach, fig_large_end,
              fig_three_arms, fig_repeats, fig_missing, fig_classifier,
              fig_pilot_budget, fig_pilot_starts, fig_pilot_unchanged, fig_pilot_min1):
        f()
