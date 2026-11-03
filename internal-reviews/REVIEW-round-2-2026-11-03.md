# Internal manuscript review — second round

**Date:** 3 November 2026  
**Version reviewed:** commit `840459b`, revision R1; clean working tree at the start of review.  
**Material:** [manuscript](../manuscript/main.tex), [current PDF](../manuscript/build/main.pdf), [supplement](../manuscript/supplement/supplement.pdf), [first review](REVIEW-gpt-6.1-sol-pro.md), [response](REVIEW-gpt-6.1-sol-pro.fix.md), and the deposited evidence and analysis scripts.

## Recommendation

**Targeted revision before submission.** R1 substantially improves the paper: the central accounting is now explicit, the unfiltered matched-size analysis is primary, implementation deviations are disclosed, and the pilot's causal and scaling conclusions are narrower. The empirical reporting contribution is defensible within the tested configurations. A second major experimental campaign is not necessary for that bounded contribution.

The paper is not yet submission-ready. Most importantly, its abstract and other prominent summaries still use the misleading attribution wording that the first review challenged. There are also residual statistical justifications and numerical statements to correct, plus unresolved figure legibility and historical reproducibility limitations.

This is a fresh review, not an implementation of manuscript edits. No experiments or model fitting were rerun. Page references below refer to the existing 30-page PDF; source links identify the reviewed text without relying on old page-local line numbers.

## What was checked

- Read the manuscript sections, contribution table, main criterion table, supplement generator, R1 analysis script, and first-round response.
- Checked the reach/quality identity and recomputed the signed and absolute shares from the deposited per-dataset R1 table. The largest identity residual is below `9e-7`, consistent with CSV rounding.
- Verified all ten SHA-256 entries in the R1 provenance manifest: nine tables and the generating script agree with their recorded hashes.
- Checked the completion totals against the deposited main run-measure table: **1,544 completed runs**, including **594 sparse runs**.
- Compared the primary and seed-paired matched-size summaries and inspected their eligibility counts.
- Read the existing PDF text and build log. The saved manuscript has **30 pages**, the supplement **3 pages**. The build log contains one **0.84674 pt overfull box**, with no undefined-reference or undefined-citation warning found. The paper was not rebuilt, and this does not constitute a visual inspection of every figure.

These checks establish internal consistency of the deposited evidence, not independent reproduction from raw datasets or verification of the original NSGAII-MIIP implementation. Literature positioning was assessed from the repository's material; no new full-text literature verification was performed.

## First-round issues: current status

| Original issue | Assessment after R1 |
|---|---|
| Attribution percentage | Equations and numerical table corrected; headline wording still not corrected consistently. |
| Predictive equivalence | Much improved: unfiltered analysis is primary, counts and individual effects are reported, and the filtered analysis is exploratory. The small-test-set justification still needs correction. |
| Definitions and boundaries | Substantially improved; a few mathematical and mutation boundary cases remain implicit. |
| Pilot causality and budget scaling | Substantially resolved for a descriptive paper. No selection-only causal claim or proportional scaling law is needed. |
| Implementation and reproducibility | Improved by explicit deviations and a reproducibility subsection; exact historical software versions and the random-forest source snapshot remain unresolved. |
| Missingness and uncertainty | Substantially improved: completion denominators, intervals, and scenario language are now present. |
| Literature positioning | Improved: initialization-only comparisons are acknowledged as prior art. |
| Figure readability | Still open; the response explicitly records the unresolved layout problem. |

## Required corrections

### 1. The abstract still describes the absolute share as a fraction of the AUF difference

**Priority: high.**  
**Locations:** [abstract](../manuscript/sections/00-abstract.tex), p.1; [introduction, contribution 1](../manuscript/sections/01-introduction.tex); [contribution table](../manuscript/sections/02-related-work.tex), p.6; [discussion](../manuscript/sections/06-discussion.tex); [conclusion](../manuscript/sections/07-conclusion.tex).

The methods now correctly distinguish

$$
S=\frac{\sum_i\rho_i}{\sum_i\Delta_i},\qquad
A=\frac{\sum_i|\rho_i|}{\sum_i|\rho_i|+\sum_i|\kappa_i|}.
$$

However, the abstract still says that “reach accounts for 98 to 100 percent of the area-under-the-front difference.” The introduction likewise says that the split “attributes 98 to 100% of it to reach.” Those statements still describe the net-difference estimand, while quoting the absolute-component statistic.

Recalculation from the deposited per-dataset table gives:

| Group | Signed share of net difference, $S$ | Absolute-component share, $A$ |
|---|---:|---:|
| Decision tree, designed | 100.105% | 99.844% |
| Decision tree, benchmark | 99.989% | 99.732% |
| Random forest | 101.164% | 98.121% |
| LightGBM | 99.972% | 99.225% |

The full results paragraph explains this properly. The prominent summaries do not. This is a reporting error rather than evidence against reach dominance, but it is the central issue of the original review and should not be marked fully fixed.

**Required change:** use one estimand consistently. For example, “Reach represents 98–100% of the combined absolute reach and quality components,” or simply “The decomposition is dominated by reach,” with the two shares left to the results table. Apply the same change to Table 1, the discussion, conclusion, and any figure caption that describes $A$ as a fraction of the net difference. Preserve the accounting-convention qualification for one-sided support.

### 2. The small-test-set rationale still substitutes a proportion standard error for F1 uncertainty

**Priority: medium.**  
**Location:** [statistical analysis](../manuscript/sections/04-experimental-design.tex), §4.3, p.14.

The earlier universal claim about a single row changing weighted F1 has been removed. Its replacement states that a score near 0.7 “that behaves like a proportion” has standard error approximately $\sqrt{0.21/n}$ and compares that value with the 0.02 margin.

The square-root expression is a Bernoulli-proportion calculation, not a weighted-F1 standard error. Weighted F1 depends on the joint confusion matrix, class frequencies, and prediction errors. Moreover, the uncertainty of a paired difference depends on the relationship between the two sets of predictions, not just the uncertainty of one score. Qualifying the approximation does not establish either a weighted-F1 uncertainty estimate or a principled cutoff of 50 rows.

The correct evidential presentation is already mostly in place: the cutoff was selected after inspecting the result, and the filtered result is exploratory.

**Required change:** remove the numerical standard-error argument and state that very small test sets motivate an exploratory stability check, without treating 50 as a validated precision threshold. If prediction-level uncertainty is estimated instead, use a method appropriate to paired F1 differences and class composition. No new analysis is necessary if the claim is simply narrowed.

Keep the unfiltered random-forest estimate, $-0.014$ with interval $[-0.044,+0.008]$, primary. In summaries, avoid letting “only without the smallest test sets” sound like an independent confirmation of equivalence. A clear alternative is that two classifiers have small conditional group means, while the third is inconclusive in the primary analysis.

### 3. The discussion understates individual matched-size differences

**Priority: medium.**  
**Location:** [discussion opening](../manuscript/sections/06-discussion.tex), pp.24–25; [supporting dataset table](../evidence/R1/tables/matched_by_dataset.csv).

The statement that “single datasets differed by up to 0.036” is not true for the unfiltered analysis. The deposited matched-size differences include:

- Coffee, random forest: **−0.137960**;
- BeetleFly, random forest: **−0.105749**;
- Adiac, LightGBM: **+0.035593**.

The maximum near 0.036 applies after excluding the small test sets, not to all individual datasets. The preceding paragraph discusses both the primary and filtered analyses, so its scope is ambiguous and understates the strongest counterexamples.

**Required change:** report the unfiltered range, or explicitly attach the 0.036 maximum to the exploratory filtered set. Distinguish positive differences favoring sparse initialization from absolute differences. The detailed results section already reports the large negative random-forest effects correctly.

### 4. “Within 0.001” is slightly too strong for the seed-paired check

**Priority: low.**  
**Locations:** [results §5.1](../manuscript/sections/05-results.tex), p.16; [first-round response](REVIEW-gpt-6.1-sol-pro.fix.md); [matched summary](../evidence/R1/tables/matched_summary.csv).

The primary random-forest conditional mean is **−0.0135796**, while its seed-paired mean is **−0.0146107**: the difference is **0.0010311**, just over 0.001. The filtered random-forest difference is **0.00121863**; filtered LightGBM differs by **0.00100671**.

This does not materially change the interpretation. It does make the repeated exact statement false at the saved numerical precision.

**Required change:** say “within about 0.0013” if covering both analyses, or “closely agrees, without changing the interpretation.” Do not infer predictive equivalence from the agreement between these two estimators.

### 5. Close the remaining definition and algorithm gaps

**Priority: low to medium.**  
**Locations:** [reach and quality definitions](../manuscript/sections/03-problem-and-metrics.tex), §3.3; [Algorithm 1 and pilot](../manuscript/sections/04-experimental-design.tex), §§4.2 and 4.4.

These are specification gaps, not demonstrated errors in the experiments:

1. **Neither configuration reaches a limit.** Both conditional means are undefined, so copying the other's mean does not define either $\tilde c$. The prose says the contribution is zero, which is enough operationally but not a complete definition of the displayed formula. Define both substituted means as zero when both reach rates are zero, or explicitly define both component contributions as zero in that case.
2. **Undefined ratios.** State what happens when the denominator of $S$ or $A$ is zero. Reporting the ratio as undefined is sufficient; do not silently imply these summaries always exist.
3. **Incomplete seeds.** Reach is defined over finished seeds, but a rate of at least 0.6 is immediately glossed as “at least three of five seeds.” Those are different eligibility rules when seeds are missing. All datasets currently included in the matched-size table have five finished seeds in both arms, so this does not alter that table. Nevertheless, specify which rule is implemented.
4. **Forced-flip boundaries.** The pilot's equal-probability addition/removal description omits singleton and full-subset exceptions, although the response says these were documented. State the actual boundary rule and restrict the zero expected size-change statement to cases in which both moves are feasible under that rule. The empty-subset behavior should also be explicit for the forced-flip arm.
5. **Budget exhaustion during MIIP.** Algorithm 1 explicitly drops ordinary children requiring a new fit after the budget is exhausted, but then improves and scores MIIP candidates without the same explicit guard. The surrounding text says all MIIP fits count. State that MIIP scoring obeys the remaining-fit cap and how a partially evaluated improvement batch is handled. This is a clarification request, not a finding that the implementation overspends.

## Remaining submission and interpretation concerns

### Figure legibility remains a real submission issue

The figure script sets labels to 8 pt and ticks to 7 pt. The first-round response records a journal recommendation of approximately 10 pt and reports that a global increase caused collisions. Restoring the old figures leaves the issue unresolved.

Before submission, inspect the figures at final printed size and fix the problematic layouts individually: shorten labels, simplify ticks, move legends, or redistribute panels. Do not merely increase all fonts and assume the result is readable. Check distinguishability without relying exclusively on hue where configurations share a panel. This review did not establish new visual defects beyond the documented unresolved problem.

### Reproducibility is improved, but not complete

The implementation subsection now documents training-only preprocessing for mutual information, final evaluation fits, the port's departures, and the source repositories. Those are meaningful improvements.

It also admits that exact historical library versions were not logged and that random-forest runs used a source copy outside version control. Distinguish verified versions from approximate or reconstructed versions: “scikit-learn 1.9” must not imply an independently verified per-run environment if that is unavailable. Link exact analysis commits, split-generation settings, and available environment records in a small reproduction entry point. If historical information cannot be recovered, retain the limitation rather than inventing precision.

The R1 manifest hashes validate the current deposited artifacts. They do not resolve the missing historical random-forest source snapshot or establish fidelity to the authors' MATLAB implementation. Continue saying “our implementation of NSGAII-MIIP,” including in interpretive headings or captions where otherwise ambiguous.

### Statistical families should be identifiable table by table

The main criterion table uses the four-group family for the sparse-versus-OBL reach comparison; Supplementary Table S1 uses the three-pair family within each benchmark group. Consequently, the same raw comparison can have different adjusted values. For example, random-forest reach has approximately **0.000012** in the main criterion table and **0.000009** under the pairwise-family calculation.

This is not evidence of an arithmetic mistake. The methods and captions should make the two families unmistakable and explain their distinct purposes so readers do not mistake them for inconsistent calculations or freely interchangeable corrections.

### The time-to-reach convention is safe for the deposited completed runs, but should be qualified

The methods censor runs that never reach the limit at the full budget, while some runs end early through stagnation. Inspection of the saved run-measure table found **no completed stagnation-stopped run that had not already reached the limit**. Thus the early-stop rule does not create a demonstrated censoring error in the reported completed-run analysis.

State that empirical condition, or clarify the convention as a budget-normalized descriptive measure. If future data include an early-stopped run without reach, it should not automatically be treated as observed through the nominal budget without justification. Missing timed-out runs remain outside this completed-run check.

### Keep the mechanism and pilot claims descriptive

The revised text appropriately says that the pilot cannot isolate selection or establish budget scaling. Maintain that discipline in short claims such as “the start decides whether the front reaches small sizes” and “the forced flip ... controls cost rather than improving the search.” These are findings for the tested budgets and four pilot datasets, not universal statements. Similar pilot AUF values do not establish exact equality or equivalence.

There is no need to demand new survival ablations or new datasets unless stronger causal or general predictive-equivalence claims are retained.

## Strengths to preserve

- The reach/quality split is now explicit, with signed and absolute summaries and an honest one-sided-support convention.
- Dataset-level analysis avoids presenting the five search seeds as independent datasets.
- The primary unfiltered random-forest result is visible rather than hidden by the post hoc exclusion.
- The manuscript separates validation selection from test reporting and now recognizes that the test curve need not be monotone.
- The sparse-start cost is reported at the large-subset end, rather than presenting a small-limit AUF win as universal superiority.
- Failed pilot expectations are reported transparently, and additional budget demonstrably restores reach on the four tested datasets.
- Missing-run scenarios are no longer described as universal robustness bounds.
- Proposal counts, fit counts, and elapsed time expose a genuine difference between an evaluation budget and computational cost.

## Minimal next revision

1. Repair the attribution wording throughout the prominent summaries.
2. Remove the proportion-based F1 precision justification; keep the filtered analysis explicitly exploratory.
3. Correct the individual-effect maximum and seed-pair agreement claim.
4. Finish the short mathematical and algorithmic boundary specifications.
5. Resolve final-size figure readability and clearly mark remaining historical reproducibility gaps.
6. Rebuild both documents, inspect the rendered figures and tables, and verify the page limit and numerical summaries.

**Bottom line:** R1 addresses most of the original substantive objections. The remaining work is mainly accurate reporting, complete specification, and submission presentation—not a reason to abandon the paper or expand it into a new optimizer study.
