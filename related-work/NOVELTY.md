# P2 novelty and experimental-design assessment

Review date: 2 November 2026. Venue calibration: a modest empirical/methodological J.UCS submission, with ComSIS or SN Computer Science as alternatives. This is an assessment, not a prediction of editorial acceptance. H1-E02 numbers below are supplied by the author; no experiment, code port, cache implementation or result file was independently reproduced in this review.

## Verdict

**The current two-start comparison is not yet a convincing paper contribution. A carefully controlled diagnostic study could be.** Sparse starts, explicit size allocation, balanced mutation, duplicate handling, evaluation budgets and AUF all have substantial prior art. The potentially useful contribution is a reproducible account of how initial size support, variation activity and duplicate handling interact under a stated budget, with separate evidence for access to small subsets and quality conditional on size.

The most consequential additional overlap is [Cong et al. (2026)](https://doi.org/10.3390/bioengineering13101229): its initialisation ablation already asks about finite-budget compact-front access. The initialiser overlap with [Miyandoab et al. (2024)](https://arxiv.org/html/2407.17795v2) remains exact. [FASTENER (2020)](https://doi.org/10.3390/e22111198) already supplies the AUF formula and name. These discoveries substantially narrow the contribution; none establishes that P2's complete proposed diagnostic protocol has already been published.

## Claims to retain, qualify or drop

| Proposed claim | Assessment and defensible wording |
|---|---|
| Initialisation and operators decide which sizes are reached | Replace deterministic language with: **under a finite budget, these choices can strongly affect the probability and time of accessing particular cardinality regions, and the sizes retained in the output.** Selection, archive policy, classifier landscape and repair also matter. |
| Sparse start gives a better feature selector | H1 only establishes a substantial advantage for a specified small-size utility in these configurations. Report unrestricted predictive performance separately, including the five datasets where it loses maximum test F1. |
| A new sparse initialiser | Drop. Uniform cardinality followed by uniform sampling without replacement is existing work; 1..30 is a parameter choice. |
| Discovery of balanced SSOM | Drop. The formula is in Oh2004 and the expected-size property is explicit in Li2025 Section 4.3. |
| SSOM preserves subset size | Reword: **preserves expected size for interior cardinalities under the stated independent-bit implementation**. Individual children can gain or lose features. |
| New AUF/AUC evaluation metric | Drop. Attribute AUF to Koprivec2020. Present the zero fallback, K and diagnostic decomposition as explicit reporting choices. |
| First study of initialisation, sparse reach, diversity or fit budgets | Unsupported. Do not use a priority claim. |
| Evidence about NSGAII-MIIP performance | Reword as evidence about **NSGA-II using the borrowed genetic operators without MIIP**. Do not present it as a comparison against Li's complete algorithm. |
| Initialisation determines the attainable front | Too strong. Distinguish support in principle, practical accessibility within budget, and survival in the returned front. |
| A reproducible measurement protocol for these interactions | Plausible methodological contribution if the pilot validates it, prior work is acknowledged and the paper supplies useful negative results and practical reporting guidance. |

## The metric issue must be stated precisely

For evaluated, valid, nonempty subsets A, define

\[
q_A(k)=\begin{cases}\max_{x\in A:\,|x|\le k}s(x),&\text{if such a subset exists},\\0,&\text{otherwise},\end{cases}
\qquad AUF_K(A)=K^{-1}\sum_{k=1}^{K}q_A(k).
\]

**A missing exact size k is not automatically a zero.** A subset of size 3 contributes to every threshold k >= 3. Write “no evaluated subset of size at most k” rather than “size k was never reached” when explaining this fallback. A run can reach k=10 yet have zero coverage at k=1..9.

Let I_A(k) indicate that at least one feasible subset exists under threshold k. Define threshold feasibility coverage R_K = sum I_A(k)/K and C_K = sum q_A(k)/sum I_A(k), where the denominator is nonzero. Then, by definition,

\[
AUF_K=R_K C_K.
\]

When R_K=0, report C_K as **undefined**, not zero. Compute this per run: the mean of products is generally not the product of mean coverage and mean conditional quality. Conditional means are descriptive and can be affected by which runs reach the region; they do not establish a causal quality effect.

If m is the smallest evaluated nonempty subset size, R_K = max(0, K-m+1)/K. This threshold statistic therefore reflects the minimum attained size; it is **not occupancy of the whole cardinality axis**. Also report exact-size occupancy, minimum size, threshold success P(m<=K), and a per-k visitation map.

### AUF is a restricted hypervolume in this setting

This is an algebraic observation for P2, not an empirical literature finding. Minimise the coordinates (|x|, 1-s(x)), assume scores in [0,1], restrict to |x|<=K and use reference point (K+1,1). For every integer interval [k,k+1), the height of the dominated region is q_A(k). Consequently,

\[
HV_{(K+1,1)}(A_{\le K})=\sum_{k=1}^{K}q_A(k)=K\,AUF_K.
\]

This uses **stepwise** envelopes and that particular reference/baseline. Trapezoidal interpolation, reference K instead of K+1, a different score baseline, or whole-front HV need not give the same number. The zero convention is the empty dominated-region convention, not evidence of a classifier achieving zero F1. Existing HV theory already concerns both front extent and objective values; P2 can make this interpretation useful for FS, not claim a general discovery about area indicators. See [Auger2012](https://doi.org/10.1016/j.tcs.2011.03.012).

### Keep four observations separate

1. **Visited:** a subset was proposed; additionally distinguish valid from invalid/empty proposals.
2. **Evaluated:** it received a real fit or a valid cache retrieval. Keep first-fit indices separately.
3. **Retained:** it survives in the final population/front or a historical archive.
4. **Competitive at size k:** its score relative to other evaluated subsets of exactly k features.

A final Pareto front omits dominated sizes intentionally. Absence there does not prove a size was never visited. A historical nondominated archive preserves the at-most-k envelope of all evaluations under fixed deterministic objectives; a population-limited final front can lose it. Keep a best-exact-k historical table in addition to the algorithm's native output.

## What H1-E02 currently demonstrates

The supplied experiment uses population 100, five seeds and 6000 unique model fits (12,000 on arcene), a decision tree, weighted validation F1 and a final test evaluation. The datasets span satimage (36 features), eodata (182), USPS (256), har (561), COIL20 (1024), gisette (5000), Prostate_GE (5966) and arcene (10,000). On all seven datasets with d>=182, the bounded start wins all five AUF comparisons, with reported mean differences of +0.49 to +0.89. Satimage reverses the ordering in all five seeds, with mean sparse-minus-OBL AUF -0.0065. These are the author's reported observations, not independently audited results.

The reported 34/35 OBL fronts without any subset <=10 make the large AUF differences primarily evidence of an output-region access failure under this configuration. They do not estimate OBL's predictive quality at k<=10. The satimage reversal and unrestricted-F1 losses are valuable boundary cases and must remain in the paper.

Five of five paired wins should not be called decisive statistical evidence on each dataset. Under an independent equal-win-probability null, an exact two-sided sign test gives 2/2^5 = 0.0625. Treat datasets and data splits as the units relevant to generalisation; do not turn five seeds on seven datasets into 35 interchangeable independent datasets. This calculation is the reviewer's derivation, not a test performed on the unavailable raw results.

The reported 250,000-560,000 generations indicate that a unique-fit budget alone can permit considerable search overhead. They do not by themselves identify which operator produces duplicates, or prove that the sparse start is more efficient in elapsed time.

## Mechanistic calculations and controls

For 0<k<d and pm=1/d, SSOM has expected deletion count k/d and addition count k/d. Hence E[delta k]=0 and E[flips]=2k/d. At (d,k)=(10,000,10), the expected flips are 0.002 and the probability of any flip is at most 0.002. Audit boundary handling for k=0 and k=d, and whether probabilities use the pre-mutation count. Repair or sequential recomputation can alter the calculation. The expected-size property is established prior art; the application to observed duplicate overhead is a hypothesis to test. Sources: [Oh2004, Section 3.4](https://doi.org/10.1109/TPAMI.2004.105), [Li2025, Section 4.3](https://doi.org/10.1016/j.ejor.2024.12.036).

Symmetric independent bit-flip at 1/d instead has E[flips]=1 and E[delta k]=1-2k/d. It both activates sparse children more often and drifts them upward. **The planned SSOM/bit-flip comparison confounds mutation activity and drift.** Add a balanced, activity-matched control: for interior k, p(1->0)=1/(2k), p(0->1)=1/[2(d-k)]. It has zero expected drift and one expected flip. This is a diagnostic rescaling of balanced mutation, not a proposed new method. Define boundary/repair rules in advance. An exactly-one-swap mutation is an optional control for within-size mixing, with exactly two flips and no direct change of k.

Reciprocal segment crossover conserves the total number of ones across the two children, but can change each child's size. It therefore does not prove a run is confined to its initial sizes. Audit identical parents, Hamming distance 1, the cut-point edge cases, feature-order sensitivity, and whether one or both children are kept. The code was not available here; these are checks to perform, not diagnosed implementation bugs.

OBL complementary pairs have the same Binomial(d,0.5) size marginal as Bernoulli(0.5), but their members are dependent and a complete paired population has mean size exactly d/2. The Bernoulli arm usefully separates pairing from density. Uniform cardinality on 1..d still has mean (d+1)/2; it is not a sparse start merely because its size distribution is broad.

For 100 independent draws from uniform cardinality 1..d, the probability of at least one initial subset <=10 is 1-(1-10/d)^100: about 0.9965 at d=182, 0.1814 at d=5000 and 0.0952 at d=10,000. Full support therefore does not imply finite-population coverage. These are analytic initialisation probabilities, not predicted final-front results.

## Baselines the pilot needs

Keep the proposed **4 x 2 x 3 x 5 = 120 runs** as a mechanism-screening pilot. Separate this factorial experiment from a smaller external-method comparison, so complete algorithms are not confused with component substitutions.

| Priority | Baseline/control | Why and budget treatment |
|---|---|---|
| Required | Existing four starts with both SSOM and symmetric bit-flip | Retain OBL versus IID Bernoulli, full-range uniform and bounded uniform. Charge the initial population. State that bounded uniform is existing work. |
| Required | Activity-matched balanced mutation | Needed to distinguish the SSOM flip-rate effect from directional drift. Run with representative dense and sparse starts; it need not double every cell initially. |
| Required | Miyandoab2024 complete Diverse NSGA-II, plus its initialisation-only ablation | Use Algorithm 1's 1..d initial start and current-min/max reinsertion, including the single-front bypass. Count all replacement evaluations. A 1..30 variant is an adaptation, not the published full method. Verify probability semantics in its implementation. |
| Required | SparseEA-style scored initialisation alone and a complete binary SparseEA comparator | Separates benefit of a start from its accompanying variation. Count all d single-feature scoring fits. On gisette, d=5000 already consumes most of a 6000-fit budget; report this rather than giving the method uncharged preprocessing. |
| Required after this review | Cong2026 harmonic start, with an IID/stratified distinction | Low-cost, directly motivated access baseline. Use P(k)=1/(k H_d). Reproduce its initialisation law in the common selector; a complete GO-guided biomarker pipeline is unnecessary for this different task. |
| Required | Uniform random sampling at fixed small k, with fits allocated explicitly across k=1..K | Establishes whether evolution improves the quality of subsets once their sizes are supplied. Include an equal-size random baseline and a fixed-k swap-search control where practical. |
| Required diagnostic | No-crossover arm on selected dense/sparse cells; standard crossover sensitivity | The current factorial holds crossover fixed, so it cannot attribute effects to crossover or all operators generally. A small ablation is enough initially. |
| Strongly recommended | Initial size-stratified random start; a Bernoulli start with mean size matched to the sparse start | Distinguishes guaranteed finite-population allocation, distribution breadth and mean density. Cite Deniz2022/Xu2020 and Cong2026; do not market this as a new initialiser. |
| For broader algorithm claims | NSGA2-CH/CHS, PRDH and a recent size-maintenance method such as CORAL or MOEA-ISa | Useful if claiming competitiveness or generality. Not all are required for a narrowly framed operator diagnosis. Obtain and inspect full specifications before implementation. |
| Optional scope check | Full NSGAII-MIIP and/or its add/eliminate/interchange improvement control | Required if the manuscript explicitly criticises or compares the source algorithm. Otherwise clearly delimit the borrowed-operator configuration. |

## Measurements and reporting needed for a credible submission

- Log initial occupancy and minimum size before search; many sparse-start first-reach events will occur during initialisation. Report first reach in cumulative real fits **including startup**, and distinguish “already present at startup” from new evolutionary reach. Never reset the fit counter after paying for an informed initialiser.
- Record per-k first visit, first real evaluation and retention; threshold hit probability; right-censored fits-to-reach; exact-k best validation score; native-front AUF and historical-envelope AUF; full-range HV with common fixed normalisation; and unrestricted predictive performance. Use several prespecified K values, including 10, rather than selecting the most favourable threshold afterwards.
- Report exact-k quality on a prespecified common support. If one method never reaches k, quality there is **not estimable**. Conditional comparisons restricted to survivors can be biased; fixed-k interventions supply stronger evidence than deleting failed runs.
- Separate identical-genome duplicates within a generation, unchanged offspring relative to parents, historical cache hits, objective-space ties and different but similarly accurate feature sets. Track these before crossover, after crossover, after mutation and after repair when applicable. Cache keys must include split/fold, classifier configuration and evaluation randomness; use the same cache policy across methods.
- Count proposals, objective requests, cache hits/misses, unique subset evaluations, actual classifier fits and elapsed time. Cross-validation has multiple fits per subset evaluation. A cache hit is an objective request but not a new fit. Preprocessing/filter time and singleton scoring are part of the costs. For stochastic fits, define the cached estimand before treating repeats as redundant.
- Report both equal-fit and equal-time views. Add a generous, prespecified proposal/time cap to terminate pathological runs; retain unfinished runs as censored/partial-budget outcomes. Do not silently treat a capped run as having spent all 6000 fits. Plot new-fit yield against proposals and time.
- Keep outer data separate from all feature ranking and search. Fix validation rules and select deployable subsets using training/validation only. Maximum test F1 across a front is an oracle descriptive statistic: evaluating all candidates once on test does not make selecting the best test score an unbiased model-selection protocol. Resolve that ambiguity in H1 reporting.
- Use common splits and paired seeds where meaningful, with separate random streams for initialisation and variation. Confirm the important interactions with more seeds (e.g. 20 where feasible), repeat data splits, and a second classifier. Optimiser seeds alone do not measure data-sampling uncertainty. Prioritise independent splits on the small-n gene-expression datasets.
- Publish split indices, dataset versions, preprocessing, seed lists, all operator and repair details, fit-count rules, cache definitions, stopping reasons and per-evaluation traces. Report paired effects and intervals; control multiplicity for confirmatory contrasts. The three-dataset pilot screens mechanisms; it does not establish universality.

## Review risks and decision gate

Highest risk: the study merely rediscovers that sparse initialisation reaches sparse regions, already explicit in recent work. Other material risks are the exact pre-existing AUF formula; removal of MIIP; a mutation-rate confound; interpreting front absence as non-visitation; and a unique-fit budget that hides extreme overhead. The fixed K=10 and range 1..30 also encode an application preference that must be justified.

Proceed toward a J.UCS-level methodological paper if the controls reveal a reproducible interaction and the reach/quality accounting changes a scientifically relevant interpretation. If the expanded pilot shows only that starting below 30 features immediately improves a <=10 utility, present a limited replication/benchmarking result or merge it into a broader study. A smaller target venue does not remove the need to distinguish the work from the directly overlapping literature.
