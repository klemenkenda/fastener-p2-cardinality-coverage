"""Supplementary statistics for the first revision of the P2 manuscript (R1).

Answers the quantitative points of REVIEW-gpt-6.1-sol-pro.md that the copied
H13-E01 and H14-E02 tables cannot answer on their own. Every number is computed
from the distilled run logs of fastener-experiments with the measure
definitions of `experiments/h13_coverage.py`, so it matches the tables already
in evidence/ where the two overlap.

    git clone https://github.com/klemenkenda/fastener-experiments <FX>
    python evidence/R1/review_supplement.py --fx <FX>

Writes evidence/R1/tables/*.csv. Needs numpy, pandas, scipy and scikit-learn.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent / "tables"
GRIDS = ("H1-E02", "H5H6-E01", "H5H6-E02", "H5H6-E03")
A, B = "nsga2_sparse", "nsga2"
MARGIN = 0.02
MIN_TEST = 50


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.6g}" if isinstance(v, float) else v) for k, v in r.items()})
    print(f"wrote {OUT / name} ({len(rows)} rows)")


def boot(values, stat, n=10_000, seed=20200):
    """95% percentile interval of `stat` over a dataset-level bootstrap."""
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(values), size=(n, len(values)))
    with np.errstate(invalid="ignore", divide="ignore"):
        s = np.array([stat(values[i]) for i in idx])
    s = s[np.isfinite(s)]
    return float(np.quantile(s, 0.025)), float(np.quantile(s, 0.975))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fx", type=Path, required=True, help="fastener-experiments clone")
    args = ap.parse_args()
    sys.path.insert(0, str(args.fx / "experiments"))
    import h13_coverage as cov  # noqa: E402
    import h13_report as rep  # noqa: E402

    runs, missing = [], []
    for g in GRIDS:
        r, m = rep.load_grid(g)
        runs += r
        missing += m
    agg = rep.aggregates(runs)
    n_test = rep.test_rows()
    by_run = defaultdict(dict)
    for r in runs:
        by_run[(r["grid"], r["dataset"], r["method"])][r["seed"]] = r

    # ---------------------------------------------------- attribution and matched size
    att_rows, ds_rows, match_rows = [], [], []
    for g in GRIDS:
        sa, sb = agg[(g, A)], agg[(g, B)]
        terms = []
        for ds in sorted(set(sa) & set(sb)):
            xa, xb = sa[ds], sb[ds]
            reach, quality = cov.decompose(xa["r"], xa["c_bar"], xb["r"], xb["c_bar"])
            # The reach term split by whether OBL never or only sometimes reaches k.
            ra, rb = np.asarray(xa["r"]), np.asarray(xb["r"])
            ca = np.where(ra > 0, xa["c_bar"], xb["c_bar"])
            cb = np.where(rb > 0, xb["c_bar"], ca)
            per_k = (ra - rb) * (np.nan_to_num(ca) + np.nan_to_num(cb)) / 2 / cov.K
            never = float(per_k[rb == 0].sum())
            partly = float(per_k[rb > 0].sum())
            matched = cov.matched_difference(xa["r"], xa["c_bar"], xb["r"], xb["c_bar"])
            M = (ra >= cov.MATCH_SHARE - 1e-12) & (rb >= cov.MATCH_SHARE - 1e-12)
            # Seed-paired matched difference: same seed, only limits both runs reach.
            paired = []
            for s in sorted(set(by_run[(g, ds, A)]) & set(by_run[(g, ds, B)])):
                ua, ub = by_run[(g, ds, A)][s], by_run[(g, ds, B)][s]
                both = M & ua["reach"] & ub["reach"]
                if both.any():
                    paired.append(float(np.mean(ua["c"][both] - ub["c"][both])))
            row = {"grid": g, "dataset": ds, "d": xa["d"], "n_test": n_test[(g, ds)],
                   "seeds_a": xa["n_seeds"], "seeds_b": xb["n_seeds"],
                   "R_a": xa["R"], "R_b": xb["R"],
                   "auf_delta": xa["auf_k10"] - xb["auf_k10"],
                   "reach_term": reach, "quality_term": quality,
                   "reach_term_obl_never": never, "reach_term_obl_partly": partly,
                   "matched": matched, "matched_k": int(M.sum()),
                   "paired_seeds": len(paired),
                   "paired_mean": float(np.mean(paired)) if paired else None,
                   "paired_min": float(np.min(paired)) if paired else None,
                   "paired_max": float(np.max(paired)) if paired else None}
            ds_rows.append(row)
            terms.append(row)
        R = np.array([t["reach_term"] for t in terms])
        Q = np.array([t["quality_term"] for t in terms])
        D = np.array([t["auf_delta"] for t in terms])
        never = np.array([t["reach_term_obl_never"] for t in terms])
        pairs = np.c_[R, Q, D, never]

        def abs_share(p):
            return np.abs(p[:, 0]).sum() / (np.abs(p[:, 0]).sum() + np.abs(p[:, 1]).sum())

        def signed(p):
            return p[:, 0].sum() / p[:, 2].sum()

        def never_share(p):
            return p[:, 3].sum() / p[:, 2].sum()

        alo, ahi = boot(pairs, abs_share)
        slo, shi = boot(pairs, signed)
        nlo, nhi = boot(pairs, never_share)
        att_rows.append({"grid": g, "n_datasets": len(terms),
                         "auf_delta_mean": float(D.mean()),
                         "reach_term_mean": float(R.mean()), "quality_term_mean": float(Q.mean()),
                         "abs_share": abs_share(pairs), "abs_share_lo": alo, "abs_share_hi": ahi,
                         "signed_share": signed(pairs), "signed_share_lo": slo,
                         "signed_share_hi": shi,
                         "obl_never_share": never_share(pairs), "obl_never_lo": nlo,
                         "obl_never_hi": nhi,
                         "datasets_negative_quality": int((Q < 0).sum()),
                         "datasets_positive_quality": int((Q > 0).sum())})
        for label, keep in (("all", lambda t: True),
                            (f"more_than_{MIN_TEST}_test_rows", lambda t: t["n_test"] > MIN_TEST)):
            sel = [t for t in terms if keep(t) and t["matched"] is not None]
            x = np.array([t["matched"] for t in sel])
            p = np.array([t["paired_mean"] for t in sel if t["paired_mean"] is not None])
            lo, hi = boot(x, np.mean) if len(x) > 1 else (float("nan"), float("nan"))
            plo, phi = boot(p, np.mean) if len(p) > 1 else (float("nan"), float("nan"))
            match_rows.append({
                "grid": g, "datasets": label, "n_matched": len(x),
                "max_d": max((t["d"] for t in sel), default=None),
                "mean": float(x.mean()) if len(x) else None, "lo": lo, "hi": hi,
                "within_margin": bool(len(x) > 1 and -MARGIN < lo and hi < MARGIN),
                "min": float(x.min()) if len(x) else None,
                "max": float(x.max()) if len(x) else None,
                "n_abs_above_margin": int((np.abs(x) > MARGIN).sum()),
                "above_margin": ";".join(f"{t['dataset']}({t['matched']:+.3f})"
                                         for t in sel if abs(t["matched"]) > MARGIN),
                "paired_n": len(p), "paired_mean": float(p.mean()) if len(p) else None,
                "paired_lo": plo, "paired_hi": phi})
    write("attribution.csv", att_rows)
    write("matched_by_dataset.csv", ds_rows)
    write("matched_summary.csv", match_rows)

    # ---------------------------------------------------- completion denominators
    planned = defaultdict(int)
    done = defaultdict(int)
    for r in runs:
        done[(r["grid"], r["method"])] += 1
        planned[(r["grid"], r["method"])] += 1
    for m in missing:
        planned[(m["grid"], m["method"])] += 1
    write("completion.csv", [{"grid": g, "method": a, "finished": done[(g, a)],
                              "planned": planned[(g, a)],
                              "share": done[(g, a)] / planned[(g, a)]}
                             for (g, a) in sorted(planned)])

    # ---------------------------------------------------- d50 with intervals
    from sklearn.linear_model import LogisticRegression
    d50_rows = []
    for g in GRIDS:
        for arm in ("nsga2", "nsgaii_miip"):
            rs = [r for r in runs if r["grid"] == g and r["method"] == arm]
            if not rs:
                continue
            X = np.array([[np.log2(r["d"]), np.log2(r["budget"] / cov.POPULATION)] for r in rs])
            y = np.array([bool(r["reach"][-1]) for r in rs])
            ds = np.array([r["dataset"] for r in rs])
            z = float(np.median(X[:, 1]))

            def d50(Xs, ys):
                m = LogisticRegression(C=1e6, max_iter=10_000).fit(Xs, ys)
                b0, b1, b2 = m.intercept_[0], *m.coef_[0]
                return 2 ** (-(b0 + b2 * z) / b1) if b1 < 0 else float("nan")

            est = d50(X, y)
            rng = np.random.default_rng(cov.BOOT_SEED)
            uniq = np.unique(ds)
            bs = []
            for _ in range(rep.N_BOOT_GLM):
                pick = rng.choice(uniq, size=len(uniq), replace=True)
                idx = np.concatenate([np.where(ds == u)[0] for u in pick])
                if y[idx].all() or not y[idx].any():
                    continue
                bs.append(d50(X[idx], y[idx]))
            bs = np.array(bs)
            ok = bs[np.isfinite(bs)]
            d50_rows.append({"grid": g, "method": arm, "d50": est,
                             "lo": float(np.quantile(ok, 0.025)),
                             "hi": float(np.quantile(ok, 0.975)),
                             "n_boot": len(bs), "n_finite": len(ok),
                             "median_budget": 2 ** z * cov.POPULATION})
    write("d50.csv", d50_rows)

    # ---------------------------------------------------- boundary cases on the fronts
    zero_rows = []
    for g in GRIDS:
        for arm in ("nsga2", "nsga2_sparse", "nsgaii_miip"):
            rs = [r for r in runs if r["grid"] == g and r["method"] == arm]
            if not rs:
                continue
            zero = sum(int(((r["c"] == 0) & r["reach"]).sum()) for r in rs)
            nonmono = sum(int((np.diff(r["c"][r["reach"]]) < -1e-12).any()) for r in rs)
            zero_rows.append({"grid": g, "method": arm, "runs": len(rs),
                              "reached_limits_with_test_f1_zero": zero,
                              "runs_with_q_decreasing_in_k": nonmono})
    write("front_boundary.csv", zero_rows)

    # ---------------------------------------------------- validation ties at a limit
    tie_rows = []
    for g in GRIDS:
        recs = rep._read(g, "records")
        recs = recs[recs["method"].isin(rep.ARMS)]
        n_lim = n_tie = 0
        for _, grp in recs.groupby(["run_id", "method", "seed"]):
            sizes = grp["n_features"].to_numpy()
            val = grp["val_score"].to_numpy()
            test = grp["test_score"].to_numpy()
            for k in range(1, cov.K + 1):
                m = sizes <= k
                if not m.any():
                    continue
                n_lim += 1
                best = val[m].max()
                if np.unique(test[m][val[m] == best]).size > 1:
                    n_tie += 1
        tie_rows.append({"grid": g, "reached_run_limits": n_lim,
                         "limits_with_val_tie_and_different_test": n_tie})
    write("val_ties.csv", tie_rows)

    # ---------------------------------------------------- pilot
    here = Path(__file__).resolve().parents[1] / "H14-E02" / "tables"
    rm = pd.read_csv(here / "run_measures.csv")
    b10 = rm[rm["method"] == "p2_obl_b10"]
    pilot = []
    for ds, grp in b10.groupby("dataset"):
        d = int(grp["d"].iloc[0])
        med = float(grp["ttr_fits"].median())
        pilot.append({"dataset": ds, "d": d, "base_budget": int(grp["base_budget"].iloc[0]),
                      "median_first_hit_fits": med,
                      "min_first_hit_fits": float(grp["ttr_fits"].min()),
                      "max_first_hit_fits": float(grp["ttr_fits"].max()),
                      "fits_per_feature": med / d,
                      "budgets_to_reach": med / int(grp["base_budget"].iloc[0])})
    write("pilot_first_hit.csv", sorted(pilot, key=lambda r: r["d"]))
    ss = pd.read_csv(here / "subset_summary.csv")
    emp = []
    for m, grp in ss.groupby("method"):
        emp.append({"method": m, "proposals": float(grp["proposals"].sum()),
                    "empty": float(grp["empty"].sum()),
                    "empty_share": float(grp["empty"].sum() / grp["proposals"].sum()),
                    "runs_with_empty": int((grp["empty"] > 0).sum()), "runs": len(grp)})
    write("pilot_empty.csv", emp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
