# Review

**Model:** GPT-6.1 Sol Pro  
**Date:** 3 November 2026

**Basis of review.** Locations below refer to printed pages and page-local line numbers in the [manuscript PDF](../manuscript/build/main.pdf). Floating tables and figures generally lack line numbers and are identified by number. Numerical checks use the supplied evidence tables; model fitting and the historical experiments were not reproduced. No files were edited during the review.

## Summary

The paper examines whether performance differences at small feature limits reflect predictive quality or simply whether a search returns sufficiently small subsets. It compares two initializations within a common NSGA-II operator configuration, adds an implementation of the NSGAII-MIIP improvement phase, and investigates budget and mutation effects in a four-dataset pilot. Its contribution is an empirical diagnostic and reporting argument, not a new initialization or optimizer. The evidence strongly supports a large reach difference in the tested configurations, but the headline attribution percentage is inadequately defined, and the predictive-equivalence and causal conclusions exceed what the reported analyses establish.

## Recommendation

**Major revision.** A bounded empirical methods contribution is credible for ComSIS, but the central attribution statistic, post hoc equivalence claim, implementation specification, and causal wording require substantive correction.

## Major issues

### 1. The headline percentage is not the stated fraction of the AUF difference

**Location:** §3.3, p.8, lines 23–37; §5.1, p.16, lines 3–6; abstract, p.1, lines 15–17; conclusion, p.26, lines 19–22; Table 3.

**Problem.** The prose describes a symmetric product decomposition but never writes its equations or defines how its terms become the reported percentage. For limits where both conditional means exist, the apparent intended identity is

$$
r_a c_a-r_b c_b
=
(r_a-r_b)\frac{c_a+c_b}{2}
+
(c_a-c_b)\frac{r_a+r_b}{2}.
$$

The supplied [decomposition table](../evidence/H13-E01/tables/q1_terms.csv) satisfies the additive identity to numerical precision. However, the reported reach shares are reproduced by

$$
\frac{\sum_i |R_i|}
{\sum_i |R_i|+\sum_i |Q_i|},
$$

not by the reach contribution divided by the net AUF difference:

| Group | Reported absolute-component share | Signed reach contribution / net AUF difference |
|---|---:|---:|
| Designed decision tree | 99.84396% | 100.10471% |
| Benchmark decision tree | 99.73182% | 99.98904% |
| Random forest | 98.12059% | 101.16434% |
| LightGBM | 99.22473% | 99.97185% |

These are different estimands. Negative quality contributions can make the signed fraction exceed 100%; that is not an arithmetic error.

Furthermore, a reach contribution includes **different frequencies of reaching a limit**, not only limits that OBL “does not reach” at all. For example, designed EOData has final reach rates of 1.0 and 0.2.

**Why it matters.** This is the paper’s principal numerical contribution. The conclusion that reach dominates appears robust, but “98–100% of the AUF difference comes from unreached sizes” is not an exact description of the calculation.

**Concrete fix.**

- State the decomposition and aggregation equations explicitly.
- Define the cases where neither or only one configuration reaches a limit.
- Label the absolute-component statistic accurately, or report signed contributions alongside it.
- Replace “limits OBL does not reach” with wording covering lower reach frequencies.
- Provide uncertainty for the aggregate attribution and explain that assigning the whole difference to reach when one side has no observations is an accounting convention, not identification of counterfactual predictive quality.

### 2. Predictive equivalence is conditional, post hoc, and overstated

**Location:** §4.1, p.12, lines 13–19; §4.3, p.13, lines 35–38; §5.1, p.16, lines 7–13; abstract, p.1, line 17; conclusion, p.26, lines 21–22.

**Problem.** The manuscript transparently acknowledges that the exclusion of datasets with at most 50 test rows was introduced after observing a failed result under random forest. This is consequential: the original [criterion table](../evidence/H13-E01/tables/q1_criterion.csv) gives a random-forest matched-size mean of **−0.01358**, with interval **[−0.04364, +0.00830]**. After the exclusion, the corresponding result is **+0.00611 [+0.00033, +0.01258]**.

The statement that “a single misclassified row changes F1 by more than 0.02” below 50 rows is not generally true for weighted F1. Its change depends on class counts and the confusion matrix; the familiar $1/n$ increment applies to accuracy, not universally to F1.

The headline also sounds like a bound on individual differences. Retained datasets exceed 0.02:

- Adiac, random forest: **+0.02805**;
- TwoLeadECG, random forest: **+0.02177**;
- Adiac, LightGBM: **+0.03559**.

Finally, the designed experiment has only **one matched dataset**, with no dataset-level uncertainty interval in Table 3.

**Why it matters.** Small conditional group means do not establish that the methods predict equally well generally—or even on every dataset represented in those means. The filtering decision changes the evidential status of the result.

**Concrete fix.**

- Make the unfiltered analysis primary and the filtered result an explicitly exploratory sensitivity analysis.
- Replace the incorrect weighted-F1 justification with an uncertainty-based rationale.
- State “the mean conditional difference on eligible common-support datasets,” including sample counts.
- Report individual dataset effects and paired-seed uncertainty.
- Do not claim equivalence for the one-dataset designed group.
- Confirm the equivalence statement on new splits or datasets using a fixed margin and eligibility rule.

The dataset-level analysis correctly avoids treating five seeds as five independent datasets; that feature should be retained.

### 3. Several definitions and boundary cases remain insufficiently specified

**Location:** §3.1–3.3, p.8, lines 3–37; §3.4–3.5, p.9, lines 19–37; §4.4, p.14, lines 25–27.

**Problem.**

- Sparse initialization is specified as drawing sizes from 1–30, although two datasets have fewer than 30 features. Clipping, truncating the sampling range, and rejecting invalid draws produce different size distributions. Consequently, the stated $1/3$ probability is not universally applicable.
- Giving the empty subset “the worst score” does not specify whether it is excluded from the returned front and reach calculation. With cardinality zero, even a very poor empty subset can remain nondominated.
- Validation-score ties between subsets of the same size need deterministic handling. Their test scores can differ.
- The matched-size statistic averages separately conditioned seed means. Those means need not involve the same successful seeds; pairing by seed is not automatically preserved.
- Balanced mutation is derived only for $0<k<d$. The treatment of $k=0$, $k=d$, invalid children, and forced removal from a singleton is unspecified.
- Test F1 can genuinely be zero on a reached limit. Thus, “a zero means that the run returned nothing” is too categorical.
- Because selection uses validation scores but reporting uses test scores, $q(k)$ need not be monotone in $k$. This should be explicit when calling the result an area under a front.

**Why it matters.** These choices affect reach, singleton retention, cache accounting, reproducibility, and the interpretation of the central decomposition.

**Concrete fix.** Supply compact pseudocode defining admissible subsets, initialization for $d<30$, boundary mutation/repair, tie-breaking, candidate selection, and the exact matched-limit aggregation. Distinguish “absence is assigned zero” from “every zero indicates absence.”

### 4. The pilot does not isolate selection as the cause, or establish proportional budget scaling

**Location:** §5.7, p.21, lines 5–21; discussion, p.24, lines 28–39 and p.25, lines 1–5; conclusion, p.26, lines 24–28; Table 4 and Fig. 9.

**Problem.** The conclusion states that “selection, not the start, removed the large subsets.” The pilot demonstrates disappearance of large subsets under the **combined search and survival process**. It does not vary selection or separate loss through dominance, validation-score ties, crossover, mutation, and population duplication.

The broader statement that the required fits grow “roughly in proportion” to feature count is also unsupported by four heterogeneous datasets. The supplied pilot records give median first-hit counts of:

| Dataset | Features | Median fits | Fits per feature |
|---|---:|---:|---:|
| Adiac | 176 | 6,534 | 37.1 |
| Strawberry | 235 | 9,292 | 39.5 |
| Earthquakes | 512 | 47,830 | 93.4 |
| Computers | 720 | 85,239 | 118.4 |

This supports increasing effort in these four cases, not approximate proportionality.

Fig. 9 also compares a proposal-level unchanged-child frequency with a prediction evaluated at the **median size of newly evaluated subsets**. That is not the exact exposure-weighted prediction: cached proposals and changing population sizes matter.

**Why it matters.** The observational findings are useful without stronger causal or scaling claims. The present wording conflicts with the otherwise appropriate acknowledgment that selection and crossover were not varied.

**Concrete fix.**

- Say that large subsets disappear “under the tested variation and survival rules.”
- Describe the budget result as a four-dataset demonstration that additional evaluations can restore reach.
- Remove proportional-scaling language unless a suitable analysis supports it.
- For Fig. 9, average the exact unchanged probability over actual mutation inputs, or clearly label the current curve as an approximate diagnostic.
- A modest survival/archiving ablation would support a stronger mechanism claim, but is not essential if the conclusions are narrowed.

### 5. Budget accounting is substantially described, but implementation fidelity and reproducibility are not

**Location:** §4.1–4.2, p.12, lines 4–12 and 21–43; p.13, lines 1–18; §5.6, p.19, lines 15–20.

**Problem.** Counting new fits, excluding cache hits, and charging MI-phase fits are sensible and clearly stated. However, “complete NSGAII-MIIP” is stronger than the documented evidence of fidelity. The paper lacks an accessible implementation/reproduction statement specifying software versions, relevant implementation differences, preprocessing, the data used for MI estimation and discretization, and the treatment of invalid candidates and partial generations.

These details matter particularly because:

- the compared groups differ in code version, hardware, classifier and stopping rule;
- many sparse runs terminate well before their nominal fit allocation;
- the MI phase has computational costs beyond classifier fits;
- “defaults” are not reproducible without library versions;
- the calibration rule does not explain its fallback when no candidate budget satisfies the conditions, or how an already maximal budget is “increased by one step.”

The supplied provenance records are useful, but historical reports and analysis code are often only hashed, not included. Derived tables permit consistency checks, not independent reconstruction of the entire analysis.

**Why it matters.** An initialization comparison within this implementation is legitimate. Conclusions about the published complete algorithm require stronger fidelity documentation.

**Concrete fix.** Add a versioned reproducibility statement with executable analysis code, run-level records, split identifiers, package versions, preprocessing and MI-data provenance, implementation deviations, and nominal versus consumed budgets. Unless fidelity is established, consistently say “our implementation of NSGAII-MIIP.” Clarify whether final test evaluation entails additional fits and whether those costs are outside the search budget.

### 6. Missingness and uncertainty need more cautious interpretation

**Location:** §4.3, p.13, lines 25–44 and p.14, lines 3–10; Appendix A, p.27, lines 5–20; §5.2, p.17, lines 3–9.

**Problem.** Complete-case analysis, complete-seed analysis, common-dataset analysis, and missing-as-zero sensitivity are useful. They do not establish that the result is unaffected by informative missingness: unfinished runs are concentrated by configuration and dataset difficulty. Assigning zero to every missing run is one scenario, not a general bound on the comparison.

Additional uncertainty is underreported:

- the attribution percentage has no interval;
- the dimensional half-reach points are reported without their uncertainty;
- five seeds on one fixed split quantify search variability, not split variability;
- the statistical section promises rank-biserial effect sizes, but these are not presented alongside most principal results.

**Why it matters.** “The main reading does not depend on how missing runs are treated” is stronger than “it persists under the tested treatments.” The dimensional thresholds are especially easy to misread as transferable operating limits.

**Concrete fix.** Report configuration-specific completion denominators, intervals for the principal estimates, and rank-biserial effects in a compact supplement. Use explicitly bounded sensitivity language. Present the 163–226-feature values as descriptive fitted locations for this selected benchmark and budget policy, not general thresholds.

## Minor issues

1. **Positioning can be sharper without demanding frontier novelty.**  
   **Location:** §2.1, p.6, lines 28–35. Miyandoab’s CEC 2024 study includes an initialization-only comparator as well as the full diversity-maintaining method. Acknowledge that controlled initialization comparisons are also prior art. The defensible addition here is AUF attribution, conditional quality analysis, and proposal/fit diagnostics across datasets—not merely studying initialization.

2. **Historical priority wording is unnecessarily strong.**  
   **Location:** §2.1, p.6, lines 28–30; discussion, p.26, lines 8–10. Replace “introduced” size sampling with “described” or “used,” unless earlier uniform-covering work has been ruled out.

3. **The contribution table overcompresses important qualifications.**  
   **Location:** Table 1, p.7. “46 datasets and three classifiers” suggests a complete factorial design; three classifiers were attempted on the 39-dataset benchmark, with further missing cells. “F1 differs by less than 0.02” needs “group mean, conditional on eligibility.” Mark $e^{-2k/d}$ as approximate.

4. **Notation and scope should be made consistent.**  
   **Location:** Table 3, p.15; §3.2, p.8, line 17; §5.4, p.18. Expand “OBL” explicitly. “We use $K=10$ throughout” conflicts with later AUF results for $K=20$ and $K=d$; say “as the primary limit.” Define “over the whole front” as AUF with $K=d$ if that is intended.

5. **Figures are coherent but unnecessarily dependent on small type and color.**  
   **Location:** Figs. 1–12, especially the multipanel figures. The vector format and consistent encoding are appropriate, but the author’s [figure guide](../manuscript/FIGURE-STYLE.md) specifies 7–8 pt lettering, whereas the journal PDF instructions request approximately 10 pt. Identical marker shapes and solid lines also provide limited grayscale discrimination. Increase lettering and add redundant encodings where feasible.

6. **Bibliographic alphabetization has an encoding anomaly.**  
   **Location:** References, p.30, lines 39–44. Šircelj appears after Zanjani Miyandoab rather than under S. The selected bibliography style is correct, but literal Unicode handling appears to defeat normal alphabetization. Correct the BibTeX encoding/name handling.

7. **Some interpretation is repeated more often than necessary.**  
   **Location:** Introduction, §2.1, Table 1, discussion and conclusion. The contribution is restated several times at substantial length. Condensing these repetitions would improve accessibility and create room for the missing formal definitions without exceeding the page limit.

## Number/claim consistency check

Sources below are the supplied records, not independent experimental reproductions.

| Claim | Location | Source checked | Consistent? | Note |
|---|---|---|---|---|
| 46 datasets, 16–192,000 features, 2–39 classes | Abstract; §4.1, p.10, line 23 | [Dataset table](../manuscript/tables/datasets.tex) | Yes | 46 dataset rows; stated extrema agree. |
| Three configurations on 46 datasets | Conclusion, p.26, lines 18–19 | §4.2; [run records](../evidence/H13-E01/tables/run_measures.csv) | **No, literally** | Complete MIIP was attempted only in the 39-dataset benchmark, not on the seven designed-only datasets. |
| Up to three classifiers; five seeds | Abstract; introduction, p.2, lines 42–44 | Design and run records | Yes, qualified | Not all dataset/configuration/classifier cells finished or were attempted. |
| 1,544 completed main runs; 594 sparse runs, all retaining a singleton | §5.2–5.3, pp.17–18 | Run records | Yes | Independently counted 1,544 and 594; all 594 sparse records have minimum final size 1. |
| 98.1–99.8% of AUF difference is reach | §5.1, p.16, lines 3–4 | [Decomposition terms](../evidence/H13-E01/tables/q1_terms.csv) and [criterion summary](../evidence/H13-E01/tables/q1_criterion.csv) | **Numerically reproducible; interpretation mismatched** | Matches the absolute-component share, not the signed fraction of the net AUF gap. |
| At matched sizes, F1 differs by less than 0.02 | Abstract; discussion; conclusion | Decomposition terms and filtered criterion tables | **Only for selected group means** | Retained individual dataset differences exceed 0.02; unfiltered RF interval exceeds the margin. |
| Matched comparison uses 1–11 datasets, all with at most 235 features | §5.1, p.16, lines 7–10 | [Filtered criterion](../evidence/H13-E01/tables/q1_criterion_min_test50.csv) and dataset records | Yes | Conditional on the post hoc test-size exclusion. |
| Exact-size check supports the same aggregate conclusion | §5.1, p.16, line 10 | [Exact-size criterion](../evidence/H13-E01/tables/q1_criterion_min_test50_exact.csv) | Yes, qualified | Exact-size support counts differ; designed group still has only one dataset. |
| OBL reaches every dataset with at most 99 features and none above 512 | §5.2, p.17, lines 1–3 | Run records | Yes | Verified for completed runs; not proof about uncompleted cells. |
| Benchmark AUF lead is 0.42–0.49 | §5.1, p.14, lines 38–40 | [Pairwise results](../evidence/H13-E01/tables/q3_pairs.csv) | Yes | 0.490785, 0.477096 and 0.415014, approximately. |
| Sparse best-F1 loss is 0.007–0.029; final fronts end by 36 features | Introduction; §5.4; discussion | [Large-front results](../evidence/H13-E01/tables/q4_large_end.csv) and run records | Yes | Group means and maximum final size agree; not a universal score loss. |
| MIIP increases reach by 0.043, 0.075 and 0.082 | §5.5, p.19, lines 3–7 | Pairwise results | Yes | Rounded values and associated reported tests agree. |
| Sparse repeats are 96–99%; stopping counts are 72/195 and 63/194 | §5.6, p.19, lines 10–18 | [Stagnation summary](../evidence/H13-E01/tables/q8_stagnation.csv) | Yes | Specify the aggregation behind the repeat range. |
| OBL reaches all four pilot datasets at 10× | Abstract; §5.7, p.21, lines 1–6 | [Pilot criterion](../evidence/H14-E02/tables/criterion.csv) and [pilot runs](../evidence/H14-E02/tables/run_measures.csv) | Yes | All 20 runs reach; the pilot does not test very high-dimensional datasets. |
| First-hit effort is 0.54, 1.55, 3.99 and 7.10× | §5.7, p.21, lines 5–7 | Pilot runs | Yes | These are dataset medians, not ranges covering every run. Proportional scaling is not established. |
| Pilot OBL 10× AUF exceeds sparse 1× by 0.009, winning 12/20 | §5.7, p.21, lines 8–10 | [Pilot paired results](../evidence/H14-E02/tables/pairs.csv) | Yes | Mean difference 0.009411. |
| Forced flip lowers sparse proposals per fit from 176 to 4.7 | §5.7, p.24, lines 8–10 | [Subset summary](../evidence/H14-E02/tables/subset_summary.csv) | Yes | Pooled ratios are 176.212 and 4.686; these are not medians of run-level ratios. |
| Maximum generations are 563,390 and 465,914 | Discussion, p.25, lines 14–16 | Main run records | Yes | Independently checked. |
| Original H1 descriptive results agree with later analysis | Supporting evidence | [Original CSV](../evidence/H1_auf10_per_seed.csv), later run records and [provenance](../evidence/PROVENANCE.json) | Yes | Maximum AUF discrepancy approximately $2.2\times10^{-16}$; CSV checksum matches. |

## ComSIS compliance checklist

Checked against the supplied template instructions and the [current contributor guidance](https://comsis.org/information.php).

| Requirement | Status | Evidence/Location |
|---|---|---|
| At most 25–30 pages in the comsis3 template | **Pass** | Built PDF is exactly 30 pages, including references; correct class selected. No room remains for substantial additions without condensation. |
| Abstract: 70–150 words, no citations | **Pass** | **147 words**, excluding “Abstract” and keywords, counting hyphenated compounds as single words. No citations; p.1, lines 9–20. |
| Keywords present | **Pass** | P.1, lines 21–22. |
| Numeric square-bracket citations; alphabetically ordered references using splncs03 | **Fail—alphabetization detail** | Numeric format and style are correct. Šircelj is incorrectly placed after Z; p.30, lines 39–44. |
| Review line numbers present | **Pass** | Pagewise line numbering throughout the body. Floats themselves are generally unnumbered. |
| Conference extension disclosed under title and in cover letter, if applicable | **Unclear** | No extension footnote; no cover letter examined. Citation of earlier FASTENER work does not itself establish that this submission is a conference extension. |
| Generative-AI use beyond proofreading disclosed in acknowledgments | **Pass** | Explicit purposes listed, p.26, lines 42–44 and p.27, lines 1–3. |
| Complete author/affiliation/email block and corresponding author marked | **Fail as requested** | Author, institution, address and email are present, p.1, lines 5–8; no corresponding-author designation. The website explicitly requires designation for coauthored papers, whereas this draft currently has one author. |
| No visible TODO markers or todolist environments | **Pass** | No visible TODO text found in the PDF. Active drafting macros remain in source but are not visibly invoked. |
| All figures and tables cited and before references | **Pass** | All 12 figures and four tables have textual references; floats finish before references begin on p.29. |

**Additional template point:** the older PDF instructions place appendices after references, whereas this draft places Appendix A before them. Resolve that ordering with the journal; it does not invalidate the requested float-placement check.

## Missing references

No missing foundational reference was established that would, by itself, defeat the contribution. Two additions deserve attention:

1. **Zanjani Miyandoab et al., “A comparative study on population-based multi-objective feature selection,” DOI: 10.1007/s13042-025-02921-5.**  
   Already present in the [bibliography source](../manuscript/references.bib), but not cited in the paper. Its overlap with initialization/diversity comparisons should be explicitly assessed; bibliographic identity was verified, but detailed substantive overlap should not be assumed without checking the article.

2. **Cattelani and Fortino, “Improved NSGA-II algorithms for multi-objective biomarker discovery,” DOI: 10.1093/bioinformatics/btac463.**  
   Also present but uncited. Cong’s paper identifies it as an earlier bounded-size initialization precedent. Consult and cite the original when discussing the history of sparse starts; that particular historical connection was corroborated through the later paper rather than independently reconstructed from implementation code.

Miyandoab CEC 2024, Li’s NSGAII-MIIP, Cong, balanced mutation, sparse evolutionary search, and optimization-budget benchmarking are already recognized. The needed improvement is more precise comparison with these works, not a longer undirected literature survey.

## Questions for the authors

1. Is the intended headline statistic the absolute-component share reproduced above? If so, why is it described as a fraction of the net AUF difference?
2. How are conditional quality, attribution and matched-seed comparisons defined when one side has zero, one or two successful seeds?
3. What exactly happens when sparse initialization draws a size exceeding $d$, or mutation produces an empty or full subset?
4. Would the authors retain the original unfiltered quality analysis as primary and describe the test-size-filtered equivalence result as exploratory?
5. What implementation checks establish fidelity to NSGAII-MIIP, and which differences from the published code remain?
6. Were MI statistics and discretization fitted exclusively using training data? Were models refitted before test evaluation?
7. Can versioned analysis code and sufficient front-level records be released to reconstruct the decomposition, tie-breaking and matched-size results?
8. Can “selection causes the loss” and “roughly proportional budget scaling” be narrowed to the observations actually established by the pilot?
9. Does the submission extend any conference publication, and is the corresponding disclosure required?
