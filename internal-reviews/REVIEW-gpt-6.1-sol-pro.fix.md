# Response to the GPT-6.1 Sol Pro review

**Review:** [REVIEW-gpt-6.1-sol-pro.md](REVIEW-gpt-6.1-sol-pro.md)  
**Revision date:** 3 November 2026  
**Manuscript:** [manuscript/](../manuscript/), built to `manuscript/build/main.pdf`, **30 pages** in `comsis3` including references (page limit kept)  
**New supplement:** [manuscript/supplement/](../manuscript/supplement/) (`supplement.tex`, tables from `make_tables.py`, 3 pages)  
**New evidence:** [evidence/R1/](../evidence/R1/): [review_supplement.py](../evidence/R1/review_supplement.py), its output tables, and a [manifest](../evidence/R1/PROVENANCE.json)

The script recomputes every new number from the distilled run logs of `fastener-experiments` (commit `e44fd74`), using the measure definitions in `experiments/h13_coverage.py`. Where its numbers overlap with the copied H13-E01 tables, they agree exactly: the absolute reach shares, the matched-size means and intervals, and the half-reach locations. No new runs were made.

## Summary of changes

| Review point | Status | Where |
|---|---|---|
| M1 Headline attribution percentage | **Fixed** | §3.3 Eq. (2)–(3); §5.1; Table 3a; abstract; introduction; Table 1; conclusion; Supplementary Table S2 |
| M2 Matched-size equivalence is post hoc and overstated | **Fixed** (confirmation on new data is still open) | §4.3; §5.1; Table 3b; abstract; introduction; Table 1; discussion; conclusion; Supplementary Table S3 |
| M3 Definitions and boundary cases | **Fixed** | §3.1, §3.2, §3.3, §3.4, §3.5; Algorithm 1 (§4.2) |
| M4 Pilot causal and scaling wording | **Fixed** | §5.7; Fig. 9 caption; discussion; conclusion; Table 1; Supplementary Table S6 |
| M5 Implementation fidelity and reproducibility | **Mostly fixed** (exact library versions are still open) | §4.1 (budget rule), §4.2 (deviations), new §4.5; "our implementation of NSGAII-MIIP" throughout |
| M6 Missingness and uncertainty | **Fixed** | §4.3; §5.2 (d₅₀ intervals); Appendix A; discussion; Supplementary Tables S1, S4, S5 |
| m1 Positioning against Miyandoab | **Fixed** | §1; §2; §2.1; Table 1 |
| m2 "introduced" → "described" | **Fixed** | §2.1, §3.4 |
| m3 Contribution table qualifications | **Fixed** | Table 1 |
| m4 Notation and scope | **Fixed** | §3.2, §4.2, §5.1, §5.4 |
| m5 Figure lettering and redundant encodings | **Open** | see open issues |
| m6 Bibliography alphabetization | **Fixed** | `references.bib` |
| m7 Repetition | **Fixed** (condensed) | §1, §2, §6, §7 |
| Missing references | **Fixed** | Miyandoab2026 and Cattelani2022 now cited in §1, §2, and Table 1 |
| Corresponding author | **Fixed** | `main.tex` (`\thanks{Corresponding author}`) |

## Major issues

### M1. The headline percentage is not the stated fraction of the AUF difference

The reviewer was right. The reported 98.1–99.8% is the **absolute-component share** $A=\sum|\rho_i|/(\sum|\rho_i|+\sum|\kappa_i|)$, which is the `reach_share` in `h13_coverage.py`. It is not the signed fraction of the net difference.

What changed:

- §3.3 now writes out the symmetric product split (Eq. 2) and both aggregations (Eq. 3):
  - the signed share $S=\sum\rho_i/\sum\Delta_i$;
  - the absolute share $A$.
- §3.3 now spells out the boundary cases:
  - $\tilde c$ takes the other configuration's mean when $r(k)=0$;
  - a limit reached by only one configuration counts only as reach;
  - a limit reached by neither contributes nothing.
- The paper now calls the one-sided case an **accounting convention, not an estimate of counterfactual quality**.
- The paper now says that the reach part includes limits that one configuration reaches **less often**, not only limits it never reaches.
- Table 3a reports both shares with 95% bootstrap intervals over datasets:

  | Group | $S$ (signed) | $A$ (absolute) | Share from limits OBL never reaches |
  |---|---|---|---|
  | Decision tree (designed) | 100.1 [99.9, 100.5] | 99.8 [99.4, 100.0] | 99.2 |
  | Decision tree | 100.0 [99.8, 100.2] | 99.7 [99.4, 99.9] | 93.8 |
  | Random forest | 101.2 [99.5, 104.3] | 98.1 [95.2, 99.7] | 93.1 |
  | LightGBM | 100.0 [99.3, 100.8] | 99.2 [98.3, 99.8] | 88.4 |

- §5.1 explains that $S>100\%$ under the random forest comes from the negative quality parts on BeetleFly and Coffee.
- The abstract, introduction, Table 1, discussion, and conclusion no longer say "from limits the OBL start does not reach". They now say that reach "accounts for 98 to 100 percent", "mostly at limits that the OBL start never reaches".
- Appendix A and Fig. 11 now name the variant they report: the absolute share $A$.

### M2. Predictive equivalence is conditional, post hoc, and overstated

What changed:

- **The unfiltered analysis is now primary** (Table 3b, §5.1, §4.3).
  - Random forest: −0.014 [−0.044, +0.008] on 13 datasets with up to 512 features. This exceeds the margin.
  - Decision tree: −0.001 [−0.004, +0.002] on 10 datasets.
  - LightGBM: +0.001 [−0.006, +0.008] on 13 datasets.
- The rule that drops datasets with at most 50 test rows is now labeled an **exploratory sensitivity analysis chosen after the result was seen**. Its numbers appear in a separate column.
- The incorrect weighted-F1 justification ("one misclassified row changes F1 by more than 0.02") is gone. In its place, §4.3 gives an uncertainty-based rationale: a score near 0.7 on $n$ test rows has a standard error of about $\sqrt{0.21/n}$, which is above 0.06 for $n\le 50$.
- The claim is now worded as a **group mean over eligible datasets**, with counts. §5.1 names the individual datasets above 0.02:
  - Adiac, +0.028 (random forest);
  - TwoLeadECG, +0.022 (random forest);
  - Adiac, +0.036 (LightGBM).

  Supplementary Table S3 lists every dataset.
- A **seed-paired version** was added (defined in §3.3; reported in Table 3b and Supplementary Table S3). It agrees with the conditional means within 0.001.
- The designed group has one matched dataset (satimage). The paper now states explicitly that no conclusion follows from it, and that a group with one dataset has no interval.
- Abstract and conclusion now read: "mean test F1 differences stay within 0.02 under two classifiers, and under the third only without the smallest test sets."
- The retained feature from the review (datasets, not seeds, as units) is unchanged.

**Open:** confirming the matched-size reading on new splits or unseen datasets, with the margin and eligibility rule fixed in advance. This needs new runs. It is listed as future work in the conclusion.

### M3. Definitions and boundary cases

Each item was checked against the code in `fastener-experiments` (`nsgaii_miip.py`, `sota_baselines.py`, `make_report.py`, `h13_coverage.py`):

- **Sparse start for $d<30$.** The code draws sizes from $1..\min(30,d)$, which truncates the range. §3.4 and §4.2 now say this. They also say that for PenDigits ($d=16$) and ItalyPowerDemand ($d=24$), the probability of drawing at most ten features is $10/d>1/3$.
- **Empty subset.** It is scored $s=-1$. Because nothing is smaller, it is never dominated and can stay in the population. It is excluded from the returned front, from reach, and from AUF (§3.1). In the pilot, 0.03–7% of proposals were empty (§3.5).
- **Ties.**
  - Within a size, the first subset on the front is kept; across sizes, the smaller one (strict `>` in `opt_curve`), as stated in §3.2.
  - Validation ties with different test scores occur at 2.0–4.8% of reached limits.
- **Matched-limit aggregation and seed pairing.** Defined exactly in §3.3, with the seed-paired variant added (see M2).
- **Mutation boundaries.** §3.5 now covers $k=d$ (removal only) and $k=0$ (no change). There is no repair step, and an empty child is scored as in §3.1. §4.4 already described the forced flip at $k\le1$ and $k=d$; Algorithm 1 adds the pilot arms.
- **Zero scores.** §3.2 now separates "absence is assigned zero" from "every zero indicates absence". A returned subset could score 0, but no reached limit does in the 1,544 runs.
- **Non-monotone $q(k)$.** §3.2 now says that $q(k)$ is a validation-selected test curve: it decreases at some $k\le10$ in 662 of 1,544 runs. AUF is therefore not the area under a monotone front.
- **Pseudocode.** Algorithm 1 (§4.2) gives one run: start, scoring and cache, tournament, crossover locus, mutation, exact budget truncation, the MIIP step, survival, the stopping rule, and the final refit.
- **Final refit.** Returned subsets are refitted once with the same fixed random state and scored on validation and test. These fits are not charged to the budget (§3.1).

### M4. The pilot does not isolate selection or establish proportional scaling

- "Selection, not the start, removed the large subsets" now reads: the large subsets "disappear during the search **under the tested variation and survival rules**". §5.7 adds that selection and crossover were not varied, so the pilot does not show which step removes them. The wording was changed in §5.7, the discussion, the conclusion, and Table 1.
- "Roughly in proportion to the number of features" was removed everywhere: introduction, §5.7, discussion, and Table 1. §5.7 now reports:
  - the median first-hit fits: 6,534, 9,292, 47,830, and 85,239;
  - the fits per feature: 37, 40, 93, and 118;
  - that four heterogeneous datasets cannot show how the effort scales.

  Supplementary Table S6 gives medians and ranges.
- Fig. 9 is now labeled an **approximate check**. The caption says the prediction uses the median size of newly evaluated subsets, and that the exact exposure-weighted prediction would need the sizes of all mutated children, which were not logged. The text says "lies close to", not "follows".
- The pilot's proposals-per-fit numbers (176 → 4.7) are now marked as **pooled over runs**.

**Not done:** a survival or archiving ablation. The review says it is not essential once the claims are narrowed, and it would need new runs.

### M5. Implementation fidelity and reproducibility

- The paper now uses **"our implementation of NSGAII-MIIP"** consistently. "Complete NSGAII-MIIP" is gone from the abstract, §1, §2, §4.2, §5, §6, §7, and Table 1.
- §4.2 lists the documented departures from the published method:
  1. the objective is the run classifier's validation weighted F1, not the geometric mean over internal cross-validation folds;
  2. the fit budget is our own;
  3. negative clustering distances are clipped at 0;
  4. empty subsets are handled as described in §3.1.

  §4.2 also says the implementation was **not compared with the authors' code outputs**.
- **MI data provenance.** Discretization, mutual information, and clusters are computed once per dataset from the **training part only**. Their time counts toward elapsed time, not toward fits (§4.2).
- **Budget calibration** (§4.1) is now exact:
  - the grid is 1,000, 2,000, 4,000, and 6,000, then one step up;
  - if no value qualifies, the budget falls back to 12,000;
  - calibration used validation data only and a separate seed.
- **Nominal versus consumed budgets.** §4.2 now states that runs stopped by the stagnation rule spend less than their nominal budget, and points to the consumed fits in §5.6.
- **A new §4.5, Implementation and Reproducibility**, covers:
  - the public code and run logs (`fastener-experiments`), with what each run log holds;
  - the split seed and preprocessing (channel-wise flattening, no scaling, rows with missing values dropped);
  - the derived tables, scripts, and checksums in this repository and the supplement;
  - Python 3.11, NumPy 2, and scikit-learn 1.9.0 (workstation) or 1.9.1 (Vega);
  - that exact library versions, including LightGBM's, are not stored in the run logs;
  - that random-forest runs do not record a commit.

### M6. Missingness and uncertainty

- **Completion denominators.** Appendix A gives them, and Supplementary Table S4 gives them per configuration and classifier:

  | Configuration | Completion |
  |---|---|
  | OBL | 69–87% |
  | Sparse | 85–100% |
  | NSGAII-MIIP | 68–82% |
  | Designed experiment | 100% |

- **Bounded wording.** "Does not depend on how missing runs are treated" now reads "persists under the tested treatments", and the treatments are called "scenarios, not bounds" (§4.3, Appendix A, Fig. 11 caption, discussion). The text also says that missing runs are concentrated in OBL and MIIP runs on wide datasets.
- **Intervals for principal estimates:**
  - the attribution shares (Table 3a);
  - the half-reach locations d₅₀ (§5.2 and Supplementary Table S5), for example OBL 163 [122, 202], 212 [145, 277], and 226 [148, 300];
  - every principal paired comparison, with rank-biserial $r$ (Supplementary Table S1).
- **d₅₀ interpretation.** §4.3 and §5.2 now call d₅₀ "fitted locations for these datasets and budgets, not thresholds".
- **Split variability.** §4.3 and the discussion now state that five seeds on one split measure search variability, not split variability.
- **Rank-biserial in the text.** Reach ($r=1$) and time to reach ($r=-1$) now carry rank-biserial correlations; the full list is in Supplementary Table S1.

## Minor issues

1. **Positioning.**
   - §1 and §2 now say that Miyandoab et al. compare NSGA-II with and without their initialization, which makes initialization-only comparisons prior art.
   - The paper now describes its contribution as the *reading* of such comparisons: the reach/quality split, the dependence on $d$ and the budget, MIIP, and the proposal and fit counts.
   - Table 1 now cites the initialization-only comparison in its first row.
2. **Priority wording.** "Introduced the size sampling" now reads "described the size sampling" (§2.1). The uniform start is now "as in the initial population of Miyandoab et al." (§3.4). The arXiv text shows that the authors cite earlier uniform-covering work, so priority is not claimed.
3. **Table 1.**
   - Row 1 now reads "39 of them attempted with three classifiers", and the matched-size result is stated as a conditional group mean.
   - $e^{-2k/d}$ is marked as approximate.
   - The forced-flip statement is corrected: it lowers repeats only partly.
4. **Notation.**
   - "OBL" is expanded at first use in §1, §4.2, §5.1, and Table 3.
   - "We use $K=10$ throughout" now reads "as the primary limit and also report $K=20$ and $K=d$".
   - "Over the whole front" is now marked $(K=d)$.
5. **Figures.** Open; see below.
6. **Bibliography.**
   - `Šircelj` is now `{\v{S}}ircelj`, and the reference now sorts under S.
   - The other literal Unicode names are now LaTeX escapes: Ayça, López-Ibáñez, Joaquín, García.
   - An unescaped `Supplement_2` that broke BibTeX output is now escaped.
7. **Repetition.**
   - The intro contribution list is roughly halved.
   - The opening related-work paragraph that repeated the introduction is removed, as is the duplicated "Two studies are closest" paragraph in the discussion.
   - The paragraph after Table 1 is merged with the positioning paragraph.
   - The Holm explanation, the paper-outline paragraph, and the conclusion are shortened.

## Compliance checklist items

- **Page limit.** 30 pages including references, as before.
- **Abstract.** 148 words by the reviewer's convention; no citations.
- **References.** Alphabetization is fixed.
- **Corresponding author.** The single author is now marked with `\thanks{Corresponding author}`. The co-author TODO comment in `main.tex` remains.
- **Conference extension.** Not applicable. The author confirmed (3 November 2026) that the paper does not extend any conference paper, so no footnote under the title or cover-letter disclosure is needed. The cover letter may say that the submission is original.
- **Appendix order.** The appendix still comes before the references, because the newer template places it there. This can be checked with the journal at submission.

## Missing references

- **Zanjani Miyandoab et al. 2026, IJMLC** (`Miyandoab2026`). Now cited as a later study that extends the comparison with size-based initialization to several population-based methods. Only the abstract and preview were read, so the paper makes no claim about its detailed settings.
- **Cattelani and Fortino 2022, Bioinformatics** (`Cattelani2022`). Now cited as a bounded-start precedent, explicitly *as attributed by Cong et al.* The full text could not be retrieved (HTTP 403), so the attribution stays secondary, as the review advised.

## Answers to the reviewers' questions

1. **Which statistic is the headline?** It was the absolute-component share. Both shares are now defined (Eq. 3) and reported with intervals.
2. **What happens with zero, one, or two successful seeds?**
   - $r(k)=0$: $\bar c(k)$ is undefined, and the split assigns the limit to reach.
   - The matched-size difference uses only limits reached in at least 3 of 5 seeds.
   - The seed-paired version uses only seeds in which both runs reach the limit.
3. **What if the sparse start draws a size above $d$, or mutation empties or fills a subset?**
   - The sparse range is truncated at $d$.
   - An empty child is scored −1, can stay in the population, and is never returned.
   - At $k=d$ the mutation only removes features; at $k=0$ it changes nothing; there is no repair step.
4. **Which matched-size analysis is primary?** The unfiltered one. The filtered result is now exploratory.
5. **How faithful is the NSGAII-MIIP implementation?** It is a port of the published MATLAB source. The departures are documented in §4.2, and its outputs were not compared with those of the authors' code.
6. **Were MI and discretization fitted on training data, and were models refitted for testing?** MI and discretization use training data only. Test scores come from one deterministic refit per returned subset, outside the budget.
7. **Is the analysis released?** Yes. Run logs and analysis code are in `fastener-experiments`. The derived tables and the R1 script are in this repository.
8. **Can the selection and scaling claims be narrowed?** Yes; see M4.
9. **Is this a conference extension?** No. The author confirmed that the submission does not extend any conference paper, so no disclosure is required.

## Open issues

1. **Figure lettering (m5).** The ComSIS instructions ask for lettering about 2 mm high (10 pt). The figures use 8 pt labels and 7 pt ticks, set in the author's [FIGURE-STYLE.md](../manuscript/FIGURE-STYLE.md).
   - I tried 9/8 pt in `make_figures.py`. Text then collided in at least five figures: `fig_large_end` tick labels, `fig_pilot_min1` panel titles, `fig_repeats` y-labels, `fig_pilot_budget` x-labels, and `fig_missing` ticks.
   - I restored the committed figures and script unchanged.
   - Reaching about 10 pt needs per-figure layout work (fewer panels per row, shorter labels, or taller figures). Taller figures would cost page budget.
   - Redundant marker shapes conflict with the deliberate "one marker shape, all figures in colour" rule.
   - Both need an author decision.
2. **Confirmatory matched-size test (M2).** It needs new splits or unseen datasets with a pre-registered margin and eligibility rule.
3. **Survival/archive ablation (M4).** It would be needed for any causal claim about which step removes large subsets. The paper no longer makes that claim.
4. **Exact library versions (M5).** These are not in the run logs: scikit-learn per run, the LightGBM version, and the commit of the random-forest runs. They could be recovered from the Vega environment or job logs if those still exist.
5. **Fidelity check against the authors' NSGAII-MIIP code (M5).** It needs MATLAB and Weka. The paper now limits its claims to our implementation.
6. **Exact Fig. 9 prediction (M4).** It needs the sizes of mutation inputs, which the pilot's subset logs do not record.
7. **Cattelani and Fortino 2022.** The full text was not read.
8. **Corresponding-author designation.** Recheck it when co-authors are added. (The conference-extension question is closed: the paper extends no conference paper.)
9. **Small overfull box.** One remains in the Related Work paragraph on repeated candidates (0.8 pt, not visible).

## Verification

- `latexmk` builds `manuscript/main.tex` without errors, undefined references, or BibTeX warnings: **30 pages**.
- `supplement.tex` builds to 3 pages.
- `python evidence/R1/review_supplement.py --fx <fastener-experiments clone>` reproduces the H13-E01 values exactly:
  - absolute shares 0.99844, 0.99732, 0.98121, and 0.99225;
  - unfiltered and filtered matched-size means and intervals;
  - d₅₀ point estimates.
- The reviewer's signed shares (100.10, 99.99, 101.16, and 99.97%) are reproduced.
