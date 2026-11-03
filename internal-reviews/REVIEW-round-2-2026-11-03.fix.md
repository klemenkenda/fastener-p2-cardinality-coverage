# Response to the second-round internal review

**Review:** [REVIEW-round-2-2026-11-03.md](REVIEW-round-2-2026-11-03.md), on commit `840459b` (revision R1)  
**Revision:** R2, 3 November 2026  
**Manuscript:** `manuscript/build/main.pdf` is **30 pages** including references. The build has no errors, undefined references, BibTeX warnings, or overfull boxes.  
**Supplement:** `manuscript/supplement/supplement.pdf`, 3 pages (Tables S1–S6, Fig. S1)  
**New:** [REPRODUCE.md](../REPRODUCE.md), a reproduction entry point

No experiments or model fits were rerun. All numbers quoted below come from the deposited tables in `evidence/` or from the distilled run logs of `fastener-experiments` at `e44fd74`.

## Summary

| Review item | Status | Where |
|---|---|---|
| 1. Attribution wording in summaries | **Fixed** | abstract; §1 contribution 1; Table 1; §5.1 text and Fig. 1 caption; §6; §7 |
| 2. Proportion standard error used as an F1 rationale | **Fixed** | §4.3 |
| 3. Discussion understates individual differences | **Fixed** | §6, first paragraph |
| 4. "Within 0.001" for the seed-paired check | **Fixed** | §5.1; R1 response annotated |
| 5. Definition and algorithm gaps | **Fixed** | §3.3; §4.2 and Algorithm 1; §4.4 |
| Figure legibility | **Fixed** | `make_figures.py`, all figures regenerated; `FIGURE-STYLE.md` |
| Reproducibility | **Improved**; historical gaps marked as such | §4.5; §6 limits; `REPRODUCE.md` |
| Statistical families | **Fixed** | §4.3; Table 3 caption; Table S1 caption |
| Time-to-reach censoring | **Fixed** | §4.3 |
| Descriptive pilot and mechanism claims | **Fixed** | §5.5, §5.7, Fig. 5 and Fig. 8 captions, §6 |

## Required corrections

### 1. Attribution wording

Every prominent summary now names a single estimand, the **absolute share $A$**. Where a number is quoted, it is described as the reach part's share "of the combined absolute reach and quality parts". Elsewhere the summary says that the split "is dominated by reach".

| Location | Old | New |
|---|---|---|
| Abstract | "reach accounts for 98 to 100 percent of the area-under-the-front difference" | "reach makes up 98 to 100 percent of the combined absolute reach and quality parts of the area-under-the-front difference" |
| §1, contribution 1 | "A split … attributes 98 to 100% of it to reach" | "… is dominated by reach: the reach part makes up 98 to 100% of the combined absolute size of the two parts" |
| Table 1 | "reach accounts for 98–100% of the AUF difference" | "dominated by reach (98–100% of the absolute reach and quality parts)" |
| §6 | "reach accounted for 98 to 100 percent of the AUF difference" | "the split … was dominated by reach" |
| §7 | "Reach accounted for 98 to 100 percent of the AUF difference" | "… dominated by reach, which made up 98 to 100 percent of the combined absolute reach and quality parts" |
| Fig. 1 caption | "Almost all of the AUF difference … comes from reach" | "The split of the AUF difference … is dominated by reach" |

- §5.1 now says explicitly that $S$ and $A$ "measure different things" and reports both.
- The accounting-convention qualification for limits that only one configuration reaches is kept in §3.3.
- Appendix A and Fig. 11 already reported $A$ by name and are unchanged.

### 2. Rationale for the small-test-set check

The Bernoulli standard-error argument ($\sqrt{0.21/n}$) is gone. §4.3 now says only this:

- very small test sets motivated an **exploratory stability check**;
- the cutoff of 50 rows **is not a validated precision threshold**;
- the uncertainty of F1 differences on individual test sets was not estimated.

§4.3 also defines **"inconclusive"**: an interval that includes zero but extends beyond the ±0.02 margin. The random-forest result in the primary analysis, −0.014 [−0.044, +0.008], is now called inconclusive in the abstract, §1, Table 1, §5.1, §6, and §7. The phrase "only without the smallest test sets", which could read as a confirmation, is gone. §5.1 calls the filtered result "an exploratory stability check, not a confirmation".

### 3. Individual matched-size differences

The opening paragraph of §6 now gives the unfiltered extremes in both directions:

- up to **+0.036** in favor of the sparse start (Adiac, LightGBM);
- **−0.106** (BeetleFly) and **−0.138** (Coffee) in favor of the OBL start under the random forest, on the two datasets with 8 and 11 test rows.

§5.1 also says that BeetleFly and Coffee favor the OBL start, and it introduces the other datasets above 0.02 with "besides BeetleFly and Coffee".

### 4. Agreement of the seed-paired version

The deposited `matched_summary.csv` gives these differences between the seed-paired and conditional means:

| | Decision tree | Random forest | LightGBM |
|---|---:|---:|---:|
| All datasets | 0.00071 | 0.00103 | 0.00085 |
| More than 50 test rows | 0.00071 | 0.00122 | 0.00101 |

§5.1 now reads: "The seed-paired means differ from the conditional means by at most 0.0011 in the primary analysis and 0.0013 in the exploratory one, so they do not change the interpretation." No claim of equivalence rests on this agreement. The "within 0.001" sentence in the R1 response is annotated with the correction.

### 5. Remaining definitions

1. **Neither configuration reaches a limit.** Eq. (2) now defines $\tilde c_a(k)=\tilde c_b(k)=0$ in that case (§3.3). Both parts are then zero, which matches `h13_coverage.decompose`, where `nan_to_num` sets both to zero.
2. **Undefined ratios.** $S$ and $A$ are undefined when their denominator is zero; this does not happen in our groups. Bootstrap resamples with a zero denominator are skipped, as `review_supplement.boot` does by dropping non-finite values (§3.3).
3. **Incomplete seeds.** The rule is $r \geq 0.6$ of *finished* seeds (`MATCH_SHARE = 0.6`). That means three of five, three of four, or two of three. §3.3 now says this and adds that every dataset with a matched limit has five finished seeds for both starts (checked in `matched_by_dataset.csv`).
4. **Forced-flip boundaries (§4.4).** These now follow `nsgaii_miip.balanced_mutation_min1`:
   - for $1<k<d$, the forced move adds or removes one feature with equal probability, so its expected size change is zero;
   - for $k\le 1$ it can only add, and for $k=d$ it can only remove;
   - an unchanged empty child gains one feature, while a child that the balanced mutation itself emptied stays empty and is scored with $s=-1$.
5. **Budget during the improvement phase.** Algorithm 1 now says that MIIP candidates are scored "under the same cap". §4.2 explains that the budget is applied subset by subset in every scoring step: once it is spent, cached subsets are still scored, the others are dropped, and subsets already scored in the same batch are kept. This matches `run_nsgaii_miip`, which calls the same capped `evaluate` for the improved batch, so no run exceeds its budget.

## Remaining submission and interpretation concerns

### Figure legibility

The figures now meet the ComSIS lettering requirement of about 2 mm (10-point type). Each layout was fixed on its own; the font sizes were not simply raised across the board.

- **Type.** Axis labels, panel titles, and legends are 10 pt. Tick labels and annotations are 9 pt. Nothing is smaller than 9 pt at natural size.
- **2×2 grids** (Figs. 1, 2, 3, 6, 7, 9) use one shared axis label per figure, so long labels no longer run into the next row or column.
- **Log axes** write thousands as k (1k, 10k, 100k), so four decades fit a half-width panel.
- **Figs. 4, 5, 10, and 11** use short or two-line category names; the captions give full names where needed. Fig. 11 has a two-row legend so that it stays within 125 mm. Figs. 8 and 10 have fewer ticks and shorter titles.
- **Fig. 7** labels the 1× and 3× budget lines once, where no curve crosses them.
- **Distinguishability without hue.** CIELAB lightness was computed: OBL blue L* 40, sparse orange 60, NSGAII-MIIP teal 59. Sparse and NSGAII-MIIP differ only in hue, so they now get a second cue wherever they share a panel:
  - in Fig. 3 the NSGAII-MIIP curve is dashed;
  - in Fig. 2 points are offset by configuration;
  - in Fig. 4b position already separates them.

  Pilot plum and ochre differ in lightness (L* 44 and 60).
- **Checks.** Every figure was rendered and inspected at natural size: width ≤ 125 mm, no overlapping or clipped text.
- **Style guide.** `FIGURE-STYLE.md` now records the 10/9 pt sizes, shared grid labels, k notation, two-line category labels, and the dashed NSGAII-MIIP line.
- **Page budget.** The larger lettering pushed the paper to 31 pages. To stay within 30:
  - several figures were made 4–8 mm shorter;
  - Table 1, §2, §4.2, and the second paragraph of §6 were condensed, with no change of content;
  - **the classifier figure (former Fig. 12) moved to the supplement as Fig. S1.** Appendix A still reports its numbers and now points to Fig. S1. The paper now has 11 figures.

### Reproducibility

- **Run provenance, corrected.** R1 said the random-forest runs "used a copy outside version control". That is wrong. Per DEC-43 in `fastener-experiments`, the Vega compute nodes had no git, so those runs did not record a commit. Their commits, `5efd5a3` and `f3eb230`, were reconstructed from the cluster clone's history. §4.5, §6, and `REPRODUCE.md` now say this.
- **No uncommitted code.** No analyzed run has a `-dirty` algorithm ID. The `dirty` flag that some runs show also counts non-code paths such as results and reports (`provenance.git_state`). Runs started with `--experiment` refuse uncommitted code (DEC-15).
- **Library versions.** §4.5 now separates what is recorded from what is reconstructed:
  - library versions are **not stored per run**;
  - Python 3.11, NumPy 2, scikit-learn 1.9.0 (workstation) and 1.9.1 (Vega) come from the experiment records;
  - the LightGBM version is not recorded.
- **New `REPRODUCE.md`**, cited in §4.5. It lists:
  - every code commit per group of runs (recorded or reconstructed) and the analysis commits (`354c307`, `e44fd74`, FASTENER `047e1fb`);
  - split settings (60/20/20, `SPLIT_SEED = 20200`, merged archive splits, `ROW_CAP = 50,000`) and seeds (model 20200, search 2020–2024 and 2025–2029, calibration 1999);
  - the environment used to rerun the analysis layer;
  - the commands that go from distilled logs to tables, figures, and PDFs;
  - the known gaps.
- "Our implementation of NSGAII-MIIP" is now also used in §1, Table 1, §5.5, and the Fig. 5 caption.

### Statistical families

- §4.3 now states that the sparse-versus-OBL comparison belongs to two families:
  - the four groups (Table 3);
  - the three pairs within a group (Table S1).
- §4.3 adds that the corrected $p$-values therefore differ slightly between the two tables, and that neither changes a decision.
- The Table 3 caption reads "Holm-corrected over the four groups". The Table S1 caption names its family and refers back to Table 3.

### Time-to-reach convention

The deposited `run_measures.csv` was checked:

- 565 of 1,544 completed runs never reached the limit;
- **every one of them ran to its full budget**;
- all 175 stagnation-stopped runs had reached the limit.

§4.3 now says that a non-reaching run is censored at its last fit count. In all completed runs that count is the full budget, so the measure is a budget-normalized description of the completed runs. Timed-out runs remain outside this analysis, as Appendix A states.

### Descriptive mechanism and pilot claims

These statements are now explicitly limited to the tested budgets and runs:

| Location | Old | New |
|---|---|---|
| §5.5 | "the start decides whether the front reaches small sizes" | "in these runs … the start matters far more for whether the front reaches small sizes" |
| §6 | "the start decided whether …" | "In these runs and within the tested budgets, the start mattered far more than the improvement phase …" |
| §6 | "with the same AUF … so it controls cost rather than improving the search" | "with a similar AUF …; there, it lowered the cost rather than improving the search" |
| §5.7 | "the OBL start scores as well as the sparse start" | "scores similarly to" |
| §5.7 | "leaves AUF unchanged" | "changes AUF little (−0.003 and 0.000 on average)" |
| §5.7 | "AUF … measures how far the start is from the small sizes" | "largely measures" |
| Fig. 8 caption | "do as well as the sparse start" | "score similarly to the sparse start" |

The narrowing of R1 (no claim that selection alone causes the loss, no scaling law) is kept.

## Other changes

- **Abstract:** 149 words in the source by whitespace count (hyphenated compounds count as one word), down from 150.
- **Overfull box:** the 0.85 pt overfull box in §2 was removed by rewording.
- **README:** now links `REPRODUCE.md` and this response.

## Open issues

1. **Exact historical library versions.** Per-run scikit-learn and LightGBM versions cannot be recovered from the run logs. This is stated as a limitation.
2. **Random-forest commits.** They were reconstructed, not recorded. The reconstruction (DEC-43) is documented, not independently verified.
3. **Fidelity to the authors' NSGAII-MIIP code.** Not tested, because it needs MATLAB and Weka. The paper limits its claims to our implementation.
4. **Confirmatory matched-size analysis.** It still needs new splits or unseen datasets with a pre-specified margin and eligibility rule. It is listed as future work.
5. **Fig. 9.** It remains an approximate check, because the sizes of mutated children were not logged.
6. **Classifier figure.** It is now in the supplement. If the journal allows more pages, it can return to Appendix A unchanged.

## Verification

- The manuscript builds with `latexmk`: **30 pages**, with no errors, undefined references or citations, BibTeX warnings, or overfull boxes.
- `supplement.tex` builds to 3 pages, with tables regenerated by `make_tables.py`.
- All 12 figures were regenerated by `make_figures.py` and inspected at natural size: 11 in the paper and Fig. S1 in the supplement.
- New numbers were checked against the deposited tables:
  - seed-paired differences (`matched_summary.csv`);
  - the extremes of the individual matched-size differences (`matched_by_dataset.csv`);
  - censoring and stagnation counts (`run_measures.csv`);
  - commit and dirty-flag status per group (distilled `runs.csv.xz`).
