# Search log

Search date: **2 November 2026**, Europe/Ljubljana. Coverage: approximately 2010 through the review date, retaining Oh2004 as an explicitly requested foundational exception. This is a targeted critical review, **not an exhaustive systematic review or a claim of search saturation**.

## Search mechanism and count definitions

The review used live web search, publisher/repository opening, DOI redirection and Crossref metadata, plus Semantic Scholar graph queries. Search terms were refined adaptively and both references and forward citations of the three specified anchors were examined. Papers were retained for a concrete overlap with initialisation, variation/cardinality dynamics, size reach, set evaluation, duplicates or budget/reporting practice.

There were **100 logged web queries in 27 batches**, including the initial verification batch. The 26 subsequent batches returned **917 result records** representing **729 distinct raw URLs**. These returned records were processed for title/source triage, including duplicate/aggregation records and peripheral results. The initial batch's exact returned count was not preserved and is excluded from these totals. Counts are bounded tool-returned records, **not total database hits, unique papers, or 917 full-text readings**. Queries in a batch were issued together; per-query hit allocation is unavailable. No artificial Google Scholar hit estimates are reported.

The retained catalogue has **42 papers**: 12 supplied references/leads and 30 additions. Three additions have incomplete substantive access and are explicitly marked. The other 39 received abstract or specific-section review; availability of a PDF was never equated with full-text reading. The complete returned-title inventory below permits auditing of the screening scope.

## Databases and access

| Database/source | How it was used and limitation |
|---|---|
| Google Scholar | An explicit Scholar title-search URL for Kropp2022 and a Scholar-domain citation query for Miyandoab2024 were attempted. The direct Scholar URL was inaccessible to the tool; no native Scholar results/citation export were obtained. This part of the requested coverage remains limited. |
| Semantic Scholar | Direct Graph API calls by DOI succeeded for Kropp2022, Miyandoab2024 and Li2025. The returned forward edges numbered 41, 5 and 17 respectively. Miyandoab returned 40 reference records; the others returned null references. These are API snapshots, not audited global citation totals. Later individual-paper API requests were rate-limited. |
| IEEE Xplore | Indexed publisher abstracts and records were searched; DOI destinations were checked. Direct pages often returned challenge/202/418 responses. Public author manuscripts and PubMed reproductions of abstracts supplied lawful alternatives; no subscription bypass was used. |
| ScienceDirect | Publisher abstract/highlights, section snippets and references/citing-paper lists were searched. Direct body access was sometimes 403. No full-text reading is claimed for SPS or MOEA-ISa. |
| SpringerLink | Article/chapter records, accessible article sections, rights statements and two permitted PDFs were examined. Subscription previews were retained as abstract-only. |
| arXiv | Miyandoab2024 v2 HTML/PDF and Bartz-Beielstein2020 v2 were inspected; version and licence were recorded. An arXiv posting was not treated as automatically redistributable. |
| DBLP | Bibliographic corroboration, issue years, author names and links; particularly Kropp2022, Xue2022, the 2026 comparative study and the relevant journal issue records. DBLP metadata is not substantive algorithm evidence. |
| Crossref / DOI | Full deposited author/title/venue/issue/page metadata and actual DOI redirect destinations. Temporary 429 responses were retried selectively. Printed issue years take precedence over years embedded in DOI strings. |
| Author/institutional repositories, PubMed, PMC/Europe PMC | Accessible manuscripts and original article text/abstracts. Europe PMC XML supplied PeerJ full article sections after direct PMC/PeerJ access failed. Author manuscripts for Oh and Li were read but not redistributed without an allowed licence. |

## Citation and reference tracing


### Kropp2022

[Anchor DOI](https://doi.org/10.1016/j.swevo.2021.101025); [Semantic Scholar request](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.swevo.2021.101025?fields=title,authors,year,references.title,citations.title). Returned 41 citing records; reference field null, not zero known references. Crossref supplied 29 deposited reference records.

Forward titles screened:

- An imitation-based framework for large-scale sparse multi-objective optimization
- Combining sparse evolutionary operators and deep reinforcement learning for large-scale sparse multiobjective optimization problems
- Large-Scale Sparse Multi-Objective Optimization via Customized Individual Learning
- Turning Sparse Large-Scale Multiobjective Optimization Into Evolutionary Multitasking
- Memory-Guided Search-Space Constrained NSGA-II-based Method for Stable Multi-Objective Feature Selection in Sparse Data
- Integrating interactive decision making into evolutionary multiobjective agricultural optimization
- A Generative Adversarial Network Guided Evolutionary Algorithm for Large-scale Sparse Multiobjective Optimization
- An Jaccard similarity coefficient-based evolutionary algorithm for sparse large-scale multi-objective optimization problems
- A Thompson Sampling-Based Sparse Evolutionary Operator for Sparse Large-Scale Multiobjective Optimization
- Dynamic multi-knowledge evolutionary algorithm for sparse large-scale multi-objective optimization
- Investigating quality inconsistencies in the ultra-high performance concrete manufacturing process using a search-space constrained non-dominated sorting genetic algorithm II
- A dynamic multi-objective optimization approach for integrated timetabling and vehicle scheduling
- Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey
- SFE-EANDS: a simple, fast, and efficient algorithm with external archive and normalized distance-based selection for high-dimensional feature selection
- A sparse large-scale multi-objective evolutionary algorithm based on sparsity detection
- Adaptive sparsity detection-based evolutionary algorithm for large-scale sparse multi-objective optimization problems
- Efficient Sparse Large-Scale Multiobjective Optimization Based on Cross-Scale Knowledge Fusion
- An enhanced competitive swarm optimizer with strongly robust sparse operator for large-scale sparse multi-objective optimization problem
- A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges
- A co-evolutionary algorithm based on sparsity clustering for sparse large-scale multi-objective optimization
- Improving two-layer encoding of evolutionary algorithms for sparse large-scale multiobjective optimization problems
- A Two-Layer Encoding Learning Swarm Optimizer Based on Frequent Itemsets for Sparse Large-Scale Multi-Objective Optimization
- Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems
- A modified competitive swarm optimizer guided by space sampling for large-scale multi-objective optimization
- A multi-granularity clustering based evolutionary algorithm for large-scale sparse multi-objective optimization
- Multi-Objective Multi-Satellite Imaging Mission Planning Algorithm for Regional Mapping Based on Deep Reinforcement Learning
- An enhanced multiobjective bacterial foraging algorithm for the compaction parameter optimization of earth-rock dams
- Objective-hierarchy based large-scale evolutionary algorithm for improving joint sparsity-compression of neural network
- A quadratic association vector and dynamic guided operator search algorithm for large-scale sparse multi-objective optimization problem
- Designing problem-specific operators for solving the Cell Switch-Off problem in ultra-dense 5G networks with hybrid MOEAs
- Multi-swarm improved Grey Wolf Optimizer with double adaptive weights and dimension learning for global optimization problems
- Coarse-to-fine evolutionary search for large-scale multi-objective optimization: An application to ratio error estimation of voltage transformers
- An improved large-scale sparse multi-objective evolutionary algorithm using unsupervised neural network
- Agricultural Innovization: An Optimization-Driven solution for sustainable agricultural intensification in Michigan
- Large-Scale Binary Matrix Optimization for Multimicrogrids Network Structure Design
- Multi-swarm improved moth-flame optimization algorithm with chaotic grouping and Gaussian mutation for solving engineering optimization problems
- A two-stage evolutionary algorithm for large-scale sparse multiobjective optimization problems
- Structural damage identification using inverse analysis through optimization with sparsity
- Efficient optimization for sparse large-scale problems: A Markov chain Monte Carlo-driven population sampling strategy
- A two-stage evolutionary framework with structural-parametric decoupling for sparse large-scale multi-objective optimization
- Equivalence of Solutions for Two Two-Dimensional Multi-Parameter Absolute Value Optimization Problems

### Miyandoab2024

[Anchor DOI](https://doi.org/10.1109/CEC60901.2024.10612084); [Semantic Scholar request](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/CEC60901.2024.10612084?fields=title,authors,year,references.title,citations.title). Returned 5 citing records; 40 reference records. Crossref supplied 40 deposited reference records.

Forward titles screened:

- Enhancing sustainability and cost-efficiency in urban rail-road bridge: A Bayesian-optimized surrogate-assisted framework
- Multi-objective optimization of hydrogen-integrated hybrid renewable energy systems using an adaptive evolutionary framework
- A comparative study on population-based multi-objective feature selection
- Validation-based Decision Making in Data-driven Evolutionary Computation: A Case Study in Multi-objective Feature Selection
- Multi-Stage Dimension Reduction for Large-Scale Multi-Objective Feature Selection

### Li2025

[Anchor DOI](https://doi.org/10.1016/j.ejor.2024.12.036); [Semantic Scholar request](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.ejor.2024.12.036?fields=title,authors,year,references.title,citations.title). Returned 17 citing records; reference field null, not zero known references. Crossref supplied 59 deposited reference records.

Forward titles screened:

- Flatness prediction of hot-rolled dual-phase steel after laminar cooling using a mechanism-data fusion-driven decomposed attention linear network
- A Distributed Feature Selection Approach Based on Granular Computing Technique
- Key quality characteristic identification in complex production processes using bi-criteria Bayesian additive regression trees
- An evolutionary multi-objective ensemble learning algorithm for quality prediction in complex manufacturing processes
- Hierarchical Causality Graph Informed Quality Soft Sensing for Multirate Multistage Manufacturing Processes
- Lightweight feature selection with statistical priors for industrial quality monitoring
- A Cluster and Historical-Frequency Guided Evolutionary Algorithm for High-dimensional Multi-Objective Feature Selection
- A dual-orientation framework integrating explicit and silent information for Mobile game improvement and publicity: An asymmetry and term-level CR analysis based on online reviews
- Mutual information-guided causal feature selection method for quality prediction of complex products
- A Multistage Manufacturing Process Path Planning Method Based on AEC-FU Hybrid Decision-Making
- Key quality characteristic selection incorporating customer attention under imbalanced data for popular products
- An adaptive online learning scheme for anomaly detection in IIoT data streams under varying operating conditions
- Automated Identification, Warning, and Visualization of Vortex-Induced Vibration
- A decomposition-based evolutionary algorithm with multiple reference points strategy for multiobjective optimization
- A quality propagation path and implementation resolution-aware bidirectional operational parameter optimization framework for multistage manufacturing processes
- Cooperative Coevolutionary Probability-Based Binary Particle Swarm Optimization for High-Dimensional Feature Selection
- Stacking-enhanced label structure prior-guided feature selection for multi-label learning

Tracing decisions: Kropp led to sparse-operator successors, the MOFS survey and a memory-guided FS lead. Miyandoab's body/reference list led to AsilianBidgoli2020 and the unverified Ebrahimi thesis; forward tracing added the 2026 comparison and the validation-decision lead. Li's full reference list led to Oh2004, GADMS caching, surveys and duplication work; its forward list supplied CHFEA as a provisional lead. General application citations were excluded where they did not address the diagnostic questions.

Reference records were screened as titles/metadata and followed selectively; this does not mean every referenced full text was obtained. Semantic Scholar included non-paper/noise records in the 40-reference response (e.g. a licence string and an incomplete thesis); these were not promoted to verified papers.

## Inclusion and exclusion rules

Include: a verified paper with an explicit relevant mechanism, metric, empirical observation or reporting rationale; retain named user leads even where access is weak. Prefer primary paper text, publisher metadata and public author manuscripts. Use broad surveys for context and locating sources, not as substitutes for verifying algorithms. A small number of recent incomplete-access leads are retained visibly rather than silently discarded.

Exclude from the main catalogue: duplicate records/preprint-versus-journal copies of the same work, bibliographic aggregations as separate studies, unrelated application papers, papers whose AUC is only ROC-AUC, and additional general sparse optimisers that add no distinct mechanism beyond the representative families already covered. This is a relevance/space decision, not evidence those excluded studies lack useful content.

| Screened candidate/family | Decision and reason |
|---|---|
| Ebrahimi/Rahnamayan/Asilian Bidgoli thesis cited by Miyandoab2024 | Deferred: independent title/degree/year/institution record unverified. No invented thesis year or BibTeX entry. |
| Parallel fractional dominance MOEAs for feature subset selection in big data | Not retained: retrieved AUC refers to ROC performance and objectives differ; does not establish an AUC-over-k precedent. |
| Feature Selection via Pareto Multi-objective Genetic Algorithms (2018) | Not retained after preview: feature-importance criteria and general Pareto use; weaker fit to the specific cardinality-access/budget question. |
| Permutation-based multi-objective evolutionary feature selection (2026) | Not retained after abstract preview: changes the predictive objective through permutation degradation; no verified new size-reach accounting. |
| Two-stage sparse MOEA for BCI channel selection (2024) | Not retained: application-specific sparsity example; representative general sparse methods cover the mechanism needed here. |
| Additional clustering, reinforcement-learning, GAN and two-layer sparse optimisers | Title/abstract leads screened selectively; representative SparseEA, SparseEA2, PM-MOEA, MOEA/PSL, Kropp and a FS-specific successor retained. An exhaustive sparse-optimisation catalogue was outside this review. |
| Broad 2024 EC-FS survey and generic feature-selection surveys | Not retained as additional catalogue rows: overlapping background scope; the requested Xue/Jiao/Nguyen surveys and Al-Tashi review provide the principal map. |
| Dehnad2025 / Rezazadeh2026 / Huang2026 | Retained provisionally with metadata-only or incomplete-abstract labels. No algorithm or novelty conclusion is inferred from inaccessible text. |
| Shadow-library / document-request pages | Not used for obtaining papers. Search-discovered secondary records were used only as leads; no shadow-library download or access-control bypass. |

## Query batches

All batches below were run on 2 November 2026. The query text is preserved, including queries that used an approximate title before the correct one was found. Source filters describe the restrictions supplied to the web tool; unrestricted queries could return sources outside the named scholarly databases.


### Batch 00 — count not preserved; excluded from totals returned records

1. `"10.1016/j.eswa.2019.06.063"`

2. `"10.1109/IJCNN55064.2022.9892123"`

3. `"10.1016/j.swevo.2021.101025"`

4. `"10.1016/j.asoc.2022.109420"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 01 — 54 returned records

1. `"Enhancing Diversity in Multi-objective Feature Selection"`

2. `"10.1016/j.ejor.2024.12.036"`

3. `"10.1007/s40747-025-01941-6"`

4. `"10.3390/electronics15010236"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 02 — 57 returned records

1. `"10.1109/TPAMI.2004.105"`

2. `"10.1109/TEVC.2023.3256183"`

3. `"10.7717/peerj-cs.261"`

4. `"Solving multiobjective feature selection problems in classification via problem reformulation and duplication handling"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 03 — 28 returned records

1. `"feature selection" initialization "Nguyen" "survey" evolutionary multiobjective`

2. `"multiobjective feature selection" survey "Jiao"`

3. `"PM-MOEA" "MOEA/PSL"`

4. `"feature selection" "initialization" "Xue" "2014"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 04 — 45 returned records

1. `"An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems"`

2. `"A Multiobjective Evolutionary Algorithm Driven by Pattern Mining"`

3. `"MOEA/PSL" "Pareto"`

4. `"A Survey on Evolutionary Multiobjective Feature Selection" doi`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 05 — 40 returned records

1. `"MOEA/PSL" Tian Lu Zhang Tan Jin`

2. `"A Pattern Mining-Based Evolutionary Algorithm" doi`

3. `"A Survey on Evolutionary Computation Approaches to Feature Selection"`

4. `"Particle swarm optimisation for feature selection" "Novel" "2014"`

Q1: IEEE Xplore, DBLP, PubMed, GitHub. Q2: IEEE Xplore, PubMed, DBLP. Q3: IEEE Xplore and Wellington author/research sites. Q4: ScienceDirect and Wellington sites.

### Batch 06 — 50 returned records

1. `"feature selection" "area under" "Pareto" evolutionary`

2. `"feature selection" "cardinality" "hypervolume" evaluation`

3. `"multiobjective feature selection" "missing" "IGD"`

4. `"feature selection" "cache" "duplicate" evolutionary`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 07 — 46 returned records

1. `"feature selection" "uniform covering" initialization Rahnamayan`

2. `"feature selection" "cardinality" "stratified" evolutionary initialization`

3. `"feature selection" "cache" genetic algorithm repeated evaluations`

4. `"evolutionary" "benchmarking" "best practices" evaluation budget reproducibility`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 08 — 43 returned records

1. `"Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery"`

2. `"CORAL: A Rank-Memory"`

3. `"MOEA/PSL" "Tian" "2020" "doi"`

4. `"Benchmarking in Optimization: Best Practice and Open Issues"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 09 — 35 returned records

1. `"Improved Evolutionary Operators" Kropp pdf`

2. `"Benefits of sparse population sampling" pdf Kropp`

3. `"Solving Multiobjective Feature Selection" Jiao pdf site:ecs.wgtn.ac.nz`

4. `"A Survey on Evolutionary Multiobjective" pdf site:ecs.wgtn.ac.nz`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 10 — 30 returned records

1. `"hypervolume" "inverted generational distance" feature selection survey Jiao performance indicators`

2. `"Benchmarking" "optimization" "Beiranvand" "2017"`

3. `"A practical tutorial on the use of nonparametric statistical tests" evolutionary algorithms`

4. `"MOEA/PSL" "learning" Tian 2020`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 11 — 51 returned records

1. `"Solving Multiobjective Feature Selection Problems" filetype:pdf`

2. `"A Survey on Evolutionary Multiobjective Feature Selection" filetype:pdf`

3. `"MOEA/PSL" "A" "2020" "Tian" doi`

4. `"Subset selection by Pareto optimization" 2015`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 12 — 44 returned records

1. `"Hybrid genetic algorithms for feature selection" "subset size" mutation pdf Oh`

2. `"A multi-objective evolutionary algorithm with interval" pdf Xue Cai Neri`

3. `"Sparse Large-Scale" "Subspace" Tian Lu Tan 2020`

4. `"A survey on swarm intelligence approaches to feature selection" doi`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 13 — 42 returned records

1. `"MOEA/PSL"`

2. `"Sparse" "Pareto Optimal Subspace" Tian`

3. `"Probe Population-Based Initialization" feature selection`

4. `"Cattelani" "Fortino" "multi-objective" "2022"`

Q1: PubMed, IEEE Xplore, cs.surrey.ac.uk. Other queries unrestricted.

### Batch 14 — 55 returned records

1. `"A comprehensive evaluation framework for benchmarking multi-objective feature selection" doi`

2. `"Probe Population-Based Initialization and Genetic Pool-Based Reproduction" DOI authors`

3. `"Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions" doi`

4. `"hypervolume indicator" "theoretical" Auger Bader Brockhoff Zitzler 2009`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 15 — 35 returned records

1. `"Segmented initialization and offspring modification" doi`

2. `"A modified distance calculation in generational distance" IGD plus`

3. `"Hypervolume-based multiobjective optimization: Theoretical foundations" doi`

4. `"Approaches to multi-objective feature selection: A systematic literature review" DOI`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 16 — 38 returned records

1. `"Segmented initialization and offspring modification" "10.1145"`

2. `"Modified Distance Calculation in Generational Distance and Inverted Generational Distance" doi`

3. `"Approaches to Multi-Objective Feature Selection" "10.1109"`

4. `"SparseEA" "semantic scholar"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 17 — 12 returned records

1. `"10.1016/j.swevo.2021.101025"`

2. `"Enhancing Diversity in Multi-objective Feature Selection"`

3. `"10.1016/j.ejor.2024.12.036"`

4. `"Benefits of sparse population sampling" cited initialization`

Q1-Q3: semanticscholar.org. Q4: ScienceDirect, SpringerLink, arXiv. Domain-filtered Semantic Scholar web queries returned no separate Semantic Scholar records; direct API was used later.

### Batch 18 — 38 returned records

1. `"A comparative study on population-based multi-objective feature selection"`

2. `"Validation-based Decision Making in Data-driven Evolutionary Computation: A Case Study in Multi-objective Feature Selection"`

3. `"Memory-Guided Search-Space Constrained NSGA-II-based Method for Stable Multi-Objective Feature Selection in Sparse Data"`

4. `"A Cluster and Historical-Frequency Guided Evolutionary Algorithm for High-dimensional Multi-Objective Feature Selection"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 19 — 19 returned records

1. `"A comparative study on population-based multi-objective feature selection" DOI`

2. `"Memory-Guided Search-Space Constrained NSGA-II" doi`

3. `"Enhancing Diversity in Multi-objective Feature Selection" citations`

Q1: SpringerLink, DBLP. Q3: scholar.google.com. Q2 unrestricted.

### Batch 20 — 5 returned records

1. `"10.1109/TEVC.2023.3256183" "Abstract"`

2. `"10.1016/j.asoc.2022.109420" "interval" "ReliefF"`

3. `"Solving Multiobjective Feature Selection" "duplication" "objective"`

4. `"Differential Evolution With Duplication Analysis" abstract`

Q1: IEEE Xplore and iankropp.com. Q2: ScienceDirect and Surrey repository. Q3: IEEE Xplore. Q4: IEEE Xplore and PubMed.

### Batch 21 — 41 returned records

1. `"Balancing Different Optimization Difficulty Between Objectives in Multi-Objective Feature Selection"`

2. `"Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems" abstract`

3. `"Validation-based Decision Making" "11010904" abstract`

4. `"A comparative study on population-based multi-objective feature selection" "cardinality"`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 22 — 38 returned records

1. `"Balancing Different Optimization Difficulty Between Objectives" "10.1109"`

2. `"A Comprehensive Evaluation Framework" "objective" "hypervolume"`

3. `"Improved NSGA-II algorithms for multi-objective biomarker discovery" "PMC"`

4. `"An evolutionary decomposition-based multi-objective feature selection" "genuine"`

Q2: PubMed and IEEE Xplore. Others unrestricted.

### Batch 23 — 40 returned records

1. `"An evolutionary decomposition-based multi-objective feature selection" "initialization"`

2. `"Improved Evolutionary Operators for Sparse Large-Scale" "striped"`

3. `"Balancing Different Optimization Difficulty Between Objectives" "two" "archive"`

4. `"Validation-based Decision Making" "feature selection" "validation" abstract`

Unrestricted web queries; primary sources prioritised during follow-up.

### Batch 24 — 0 returned records

1. `"Balancing Different Optimization Difficulty" "10323115"`

2. `"Validation-based Decision Making" "Dehnad" "overfitting"`

Both queries restricted to IEEE Xplore.

### Batch 25 — 1 returned records

1. `"An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems" "Abstract"`

Restricted to IEEE Xplore; returned an unrelated constrained-MOO paper, excluded.

### Batch 26 — 30 returned records

1. `"SparseEA" "Tian" "Jin" abstract`

2. `"An Evolutionary Algorithm for Large-Scale Sparse" Surrey`

Unrestricted web queries; primary sources prioritised during follow-up.

## Direct verification, retrieval and failed access

Actual DOI GET requests followed redirects for all 12 supplied items and the additional DOI-bearing records where available. DOI routing for the supplied list is in CORRECTIONS.md. Crossref title queries verified the comparative, memory-guided, CHFEA and validation-decision records; wrong-title matches returned by those queries were discarded. Bartz-Beielstein's DOI is DataCite/arXiv; the official NIPS record did not provide a verified DOI for Qian2015.

Direct access failures included Google Scholar, several IEEE publisher pages, some ScienceDirect body pages, the original Cattelani2022 body and direct PeerJ PDF retrieval. Standard public alternatives were used where successful. The PDF source and licence manifest identifies exactly what is redistributed; neither all downloaded manuscripts nor automatically all open-access papers are in the ZIP.

## Returned-title audit inventory

The following is an inventory of the bounded web-returned records, not an additional bibliography. Repeated titles and multiple URLs for one paper are intentional. Query strings on result URLs are omitted here to avoid preserving temporary signed PDF links; counts above refer to the raw returned URLs. The retained-paper decisions and substantive reading depths are in ../RELATED-WORK.md/COMPARISON.csv. Other records were source corroboration, duplicate/aggregation records, peripheral results or deferred leads under the stated rules.


### Batch 01: returned titles

- 1. [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-025-01941-6)

- 2. [A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0377221724009780)

- 3. [Enhancing Diversity in Multi-objective Feature Selection](https://arxiv.org/abs/2407.17795)

- 4. [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification – DOAJ](https://doaj.org/article/50741f9288464e1eadcac99f0185d374)

- 5. [An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection](https://doi.org/10.3390/electronics15010236)

- 6. [(PDF) An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification](https://www.researchgate.net/publication/392229174_An_adaptive_initialization_and_multitasking_based_evolutionary_algorithm_for_bi-objective_feature_selection_in_classification)

- 7. [A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes](https://ideas.repec.org/a/eee/ejores/v323y2025i3p952-965.html)

- 8. [2024 IEEE Congress on Evolutionary Computation (CEC)](https://enmailab.org/resource/Realising%20Chiller%20Plant%20Optimisation%20via%20Artificial%20Neural%20Networks%20and%20Hybrid%20Genetic%20Algorithm%20and%20Particle%20Swarm%20Optimisation%20Algorithm.pdf)

- 9. [A multi-objective evolutionary algorithm with mutual-information-guided](https://andali89.github.io/homepage/pubs/2025_NSGAIIMIIP_manuscript.pdf)

- 10. [dblp: A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes.](https://dblp1.uni-trier.de/rec/journals/eor/LiHWZM25.html)

- 11. [Enhancing Diversity in Multi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/382989404_Enhancing_Diversity_in_Multi-Objective_Feature_Selection)

- 12. [July 2, 2024](https://confcats-siteplex.s3.us-east-1.amazonaws.com/wcci24/IEEE_WCCI_2024_Program_d597587f62.pdf)

- 13. [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification / CoLab](https://colab.ws/articles/10.1007%2Fs40747-025-01941-6)

- 14. [A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes / Request PDF](https://www.researchgate.net/publication/387476680_A_multi-objective_evolutionary_algorithm_with_mutual-information-guided_improvement_phase_for_feature_selection_in_complex_manufacturing_processes)

- 15. [Publications 2025 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2025)

- 16. [Publications All - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/PublicationsAll)

- 17. [An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection](https://www.mdpi.com/2079-9292/15/1/236)

- 18. [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification — Lacuna](https://lacuna.tiptreesystems.com/work/an-adaptive-initialization-and-multitasking-based)

- 19. [Enhancing Diversity in Multi-objective Feature Selection /...](https://arxivlens.com/paperview/details/enhancing-diversity-in-multi-objective-feature-selection-2521-2522443)

- 20. [Electronics / January-1 2026 - Browse Articles](https://www.mdpi.com/2079-9292/15/1)

- 21. [2024 IEEE Congress on Evolutionary Computation (CEC 2024) (Table of Contents)](https://www.proceedings.com/content/075/075666webtoc.pdf)

- 22. [马彦辉-管理学院](https://ms.tjut.edu.cn/content.jsp)

- 23. [An Improved Adaptive NSGA-II with Multiple Filtering for… / Minicod](https://www.minicod.com/papers/an-improved-adaptive-nsga-ii-with-multiple-filtering-for-high-dimensional-feature-selection-1f150aa0)

- 24. [Enhancing Diversity in Multi-objective Feature Selection / Request PDF](https://www.researchgate.net/publication/382560393_Enhancing_Diversity_in_Multi-objective_Feature_Selection)

- 25. [Differentiable channel pruning guided via attention mechanism: a novel neural network pruning approach](https://ouci.dntb.gov.ua/en/works/9jARMbgl/)

- 26. [An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection — Lei Cheng, Bo Gong, et al. · Electronics (2026) / TGRS Research Map](https://globalresearchspace.com/space)

- 27. [Sevda Ebrahimi](https://www.catalyzex.com/author/Sevda%20Ebrahimi)

- 28. [Enhanced SparseEA for large-scale multi-objective feature selection problems](https://ouci.dntb.gov.ua/en/works/42aYp3B7/)

- 29. [au:Miyandoab_S in:cs - SciRate Search](https://scirate.com/search)

- 30. [ORCID](https://orcid.org/0009-0008-3226-9190)

- 31. [(PDF) An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection](https://www.researchgate.net/publication/399459649_An_Improved_Adaptive_NSGA-II_with_Multiple_Filtering_for_High-Dimensional_Feature_Selection)

- 32. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 33. [Azam Asilian Bidgoli](https://www.catalyzex.com/author/Azam%20Asilian%20Bidgoli)

- 34. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 35. [Katalog Plus der Bibliothek der Frankfurt UAS: Artikel & mehr...](https://hds.hebis.de/fuas/EBSCO/Search)

- 36. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 37. [Evolutionary auxiliary optimization for feature selection with multi-indicator task construction](https://ouci.dntb.gov.ua/en/works/986AWv0R/)

- 38. [dblp: Azam Asilian Bidgoli](https://dblp.org/pid/236/3867.html)

- 39. [Enhanced differential evolution for high-dimensional feature selection / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-00593-x)

- 40. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for la…](https://ouci.dntb.gov.ua/en/works/4bVRZkB4/)

- 41. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selecti…](https://ouci.dntb.gov.ua/en/works/lDprMbLl/)

- 42. [李岸达-天津商业大学研究生处（学科办公室）](https://gs.tjcu.edu.cn/info/1211/4500.htm)

- 43. [Azam Asilian Bidgoli](https://www.csauthors.net/azam-asilian-bidgoli/)

- 44. [CMC / Free Full-Text / Metaheuristic-Based SDN Intrusion Detection Model Based on Adaptive Chinese Pangolin Optimizer Algorithm](https://www.techscience.com/cmc/v89n3/69344/html)

- 45. [Azam Asilian Bidgoli - Research Papers & Publications /...](https://arxivlens.com/author/details/azam-asilian-bidgoli-6823-44149282)

- 46. [Feature Selection - Domain Research Papers - Arxiv Search - Page 18 / Arxiv - DeepPaper](https://arxiv.deeppaper.ai/domain_tags/Feature%20Selection)

- 47. [(PDF) An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection](https://www.researchgate.net/publication/399459649_An_Improved_Adaptive_NSGA-II_with_Multiple_Filtering_for_High-Dimensional_Feature_Selection)

- 48. [Lightweight feature selection with statistical priors for industrial quality monitoring](https://ouci.dntb.gov.ua/en/works/42018LQw/)

- 49. [A Multistage Manufacturing Process Path Planning Method Based on AEC-FU Hybrid Decision-Making](https://ouci.dntb.gov.ua/en/works/731xnYN6/)

- 50. [A dual-orientation framework integrating explicit and silent information for Mobile game improvement and publicity: An …](https://ouci.dntb.gov.ua/en/works/4kEvZrLg/)

- 51. [Industrial Internet of Things-based mechanism-data fusion driven decomposed attention linear network for flatness predi…](https://ouci.dntb.gov.ua/works/loNrrPOQ/)

- 52. [Hierarchical Causality Graph Informed Quality Soft Sensing for Multirate Multistage Manufacturing Processes - Cui - 2026 - Quality and Reliability Engineering International - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1002/qre.70316)

- 53. [Homepage / An-Da Li / Tianjin University of Commerce](https://andali89.github.io/homepage/index.html)

- 54. [This is an electronic reprint of the original article.](https://aaltodoc.aalto.fi/server/api/core/bitstreams/a7332520-1e71-4122-bc2d-23cba2da272f/content)

### Batch 02: returned titles

- 1. [Hybrid genetic algorithms for feature selection - PubMed](https://pubmed.ncbi.nlm.nih.gov/15521491/)

- 2. [Solving Multiobjective Feature Selection Problems in Classification…](https://tlooto.com/paper/150259695739)

- 3. [Hybrid genetic algorithms for feature selection / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/document/1335448/)

- 4. [(PDF) Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling](https://www.researchgate.net/publication/364653518_Solving_Multiobjective_Feature_Selection_Problems_in_Classification_via_Problem_Reformulation_and_Duplication_Handling)

- 5. [An evolutionary decomposition-based multi-objective feature selection for multi-label classification.](https://pubmed.ncbi.nlm.nih.gov/33816913/)

- 6. [Solving Multiobjective Feature Selection Problems in Clas… / Minicod](https://www.minicod.com/papers/solving-multiobjective-feature-selection-problems-in-classification-via-problem-reformulation-and-duplication-handling-326f28ea)

- 7. [dblp: Hybrid Genetic Algorithms for Feature Selection.](https://dblp1.uni-trier.de/rec/journals/pami/OhLM04.html)

- 8. [Hybrid genetic algorithms for feature selection](https://openalex.org/W2100253618)

- 9. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Request PDF](https://www.researchgate.net/publication/369219815_Improved_Evolutionary_Operators_for_Sparse_Large-Scale_Multiobjective_Optimization_Problems)

- 10. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective...](https://bishtref.com/articles/10.1109/tevc.2023.3256183)

- 11. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 12. [Hybrid genetic algorithms for feature selection](https://explore.metascienceobservatory.org/papers/W2100253618)

- 13. [Hybrid genetic algorithms for feature selection](https://www.researchgate.net/publication/8199995_Hybrid_genetic_algorithms_for_feature_selection)

- 14. [IEEE Computational Intelligence Society: August 2024](https://ieee-cis.blogspot.com/2024/08/)

- 15. [Hybrid genetic algorithms for feature selection - JBNU Researchers Portal - Pure](https://pure.jbnu.ac.kr/en/publications/hybrid-genetic-algorithms-for-feature-selection/)

- 16. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 28, Issue 4, August 2024](https://ieee-cis.blogspot.com/2024/08/ieee-transactions-on-evolutionary.html)

- 17. [Hybrid Genetic Algorithms for Feature Selection (2004) —… / Minicod](https://www.minicod.com/papers/hybrid-genetic-algorithms-for-feature-selection-1efc1391)

- 18. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 19. [Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling - 科研通](https://www.ablesci.com/scholar/paper)

- 20. [Publications 2022 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2022)

- 21. [ORCID](https://orcid.org/0000-0001-7402-9939)

- 22. [An evolutionary decomposition-based multi-objective feature selection for multi-label classification](https://openalex.org/W3009458272)

- 23. [Multi-Strategy Assisted Multi-Objective Whale Optimization Algorithm for Feature Selection - ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S1526149224000158)

- 24. [未来科学与工程学院](https://web.suda.edu.cn/rwjiao/)

- 25. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 26. [/ PDF or Rental](https://articles.researchsolutions.com/hybrid-genetic-algorithms-for-feature-selection/doi/10.1109/tpami.2004.105)

- 27. [Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling - 科研通](https://www.ablesci.com/assist/detail)

- 28. [(PDF) Hybrid genetic algorithms for feature selection (2004) / Il-Seok Oh / 973 Citations](https://scispace.com/papers/hybrid-genetic-algorithms-for-feature-selection-421b9nybwa)

- 29. [Microsoft Word - bdia-09-020](https://www.aimspress.com/aimspress-data/bdia/2025/0/PDF/bdia-09-020.pdf)

- 30. [dblp: Ruwang Jiao](https://dblp.uni-trier.de/pid/204/4700.html)

- 31. [Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling｜AI 总结内容，参与点评并联系作者 - Peeref](https://www.peeref.com/zh/works/83308026)

- 32. [ISSN: 2182-2069 / E-ISSN: 2182-2077](https://jisis.org/wp-content/uploads/2026/03/2026.I1.038.pdf)

- 33. [IEEE Transactions on Evolutionary Computation](https://bishtref.com/journals/2331/ieee-transactions-on-evolutionary-computation)

- 34. [(PDF) Cuckoo Search híbrido aplicado al Problema Inverso Aditivo de Valores Singulares Hybrid Cuckoo Search applied to the Inverse Additive Singular Values Problem](https://www.researchgate.net/publication/268278164_Cuckoo_Search_hibrido_aplicado_al_Problema_Inverso_Aditivo_de_Valores_Singulares_Hybrid_Cuckoo_Search_applied_to_the_Inverse_Additive_Singular_Values_Problem)

- 35. [The IEEE Transactions on Evolutionary Computation Volume 28, Number 4 is now available.](https://www.linkedin.com/pulse/ieee-transactions-evolutionary-computation-volume-28-number-toscano-8elge)

- 36. [A Two-Layer Encoding Learning Swarm Optimizer Based on Frequent Itemsets for Sparse Large-Scale Multi-Objective Optimization](https://jas.ia.ac.cn/article/doi/10.1109/JAS.2024.124341)

- 37. [Thermal design optimization of electronic circuit board layout with transient heating chips by using Bayesian optimization and thermal network model](https://repositori.mypolycc.edu.my/jspui/bitstream/123456789/6826/1/International%20Journal%20of%20Heat%20and%20Mass%20Transfer.pdf)

- 38. [An evolutionary decomposition-bas... preview & related info / Mendeley](https://www.mendeley.com/catalogue/68d28bbe-114d-3ffd-9814-a3149b04d1d7/)

- 39. [Development of Corn Drying Process Optimization System Based on <fc>LSTM</fc> and <fc>NSGA</fc>‐<fc>II</fc> Algorithms - Yu - 2026 - Journal of Food Process Engineering - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/jfpe.70342)

- 40. [Received:  February 12, 2021.     Revised: March 11, 2021.                                                                                             332](https://www.inass.org/2021/2021063028.pdf)

- 41. [Frontiers / Two-stage sparse multi-objective evolutionary algorithm for channel selection optimization in BCIs](https://doi.org/10.3389/fnhum.2024.1400077)

- 42. [An overview of artiﬁcial intelligence techniques for](https://research.usq.edu.au/download/1e354702f9e3229e463f04c3259994abb0ff4f34cf11b4f52a97e30f0d79a51c/10321368/2103.03081.pdf)

- 43. [An evolutionary decomposition-based multi-objective feature selection for multi-label classification](https://pmc.ncbi.nlm.nih.gov/articles/PMC7924502/)

- 44. [Frontiers / Two-stage sparse multi-objective evolutionary algorithm for channel selection optimization in BCIs](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1400077/full)

- 45. [Multiobjective feature selection for microarray data via distributed parallel algorithms](https://eprints.whiterose.ac.uk/id/eprint/150796/8/FGCS_FS_MicArr1.pdf)

- 46. [A Generative Adversarial Network Guided Evolutionary Algorithm for Large-scale Sparse Multiobjective Optimization / Machine Intelligence Research / Springer Nature Link](https://doi.org/10.1007/s11633-025-1559-z)

- 47. [Robust proportional overlapping analysis for feature selection in binary classification within functional genomic experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC8176540/)

- 48. [Feature selection](https://en.wikipedia.org/wiki/Feature_selection)

- 49. [Multi-strategy synthetized equilibrium optimizer and application](https://pmc.ncbi.nlm.nih.gov/articles/PMC10803088/)

- 50. [Отбор признаков](https://ru.wikipedia.org/wiki/%D0%9E%D1%82%D0%B1%D0%BE%D1%80_%D0%BF%D1%80%D0%B8%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2)

- 51. [一种基于进化分解的多标签分类多目标特征选择方法。 - Suppr / 超能文献](https://suppr.wilddata.cn/browses/detail/pubmed/33816913)

- 52. [Selección de variable](https://es.wikipedia.org/wiki/Selecci%C3%B3n_de_variable)

- 53. [(PDF) Robust proportional overlapping analysis for feature selection in binary classification within functional genomic experiments](https://www.researchgate.net/publication/352037134_Robust_proportional_overlapping_analysis_for_feature_selection_in_binary_classification_within_functional_genomic_experiments)

- 54. [(2020) PeerJ Computer Science Vol. 6. PeerJ](https://zh.mindat.org/reference.php)

- 55. [schizophrenia / psychosis (population): OSCR](https://openscicode.org/browse/population/schizophrenia/)

- 56. [Q2 Dergilerde Yayımlanan Makaleler - 2026 / Balıkesir Üniversitesi Akademik Bilgi Sistemi](https://akbis.balikesir.edu.tr/dilim.php)

- 57. [Niu, Yang, Tao, Xue, Chang, Qinyuan, Hu, Mingming, Li, Xin, Gao, Xiaoping (2025) Machine learning-based feature selection and classification for cerebral infarction screening: an experimental study. PeerJ Computer Science, 11. doi:10.7717/peerj-cs.2704](https://zh.mindat.org/reference.php)

### Batch 03: returned titles

- 1. [Multiobjective Feature Selection Survey / PDF / Mathematical Optimization / Theoretical Computer Science](https://www.scribd.com/document/726578051/A-Survey-on-Evolutionary-Multiobjective-Feature-Selection-in-Classification-Approaches-Applications-and-Challenges)

- 2. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / NDL Search / National Diet Library](https://ndlsearch.ndl.go.jp/en/books/R100000136-I1360588389326737152)

- 3. [(PDF) A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges](https://www.researchgate.net/publication/372152809_A_Survey_on_Evolutionary_Multiobjective_Feature_Selection_in_Classification_Approaches_Applications_and_Challenges)

- 4. [A Survey on Evolutionary Multiobjective Feature Selection…](https://lacuna.tiptreesystems.com/work/a-survey-on-evolutionary-multiobjective-feature-selection)

- 5. [Particle swarm optimisation for feature selection in classification](https://abcdocz.com/doc/1287506/particle-swarm-optimisation-for-feature-selection-in-clas...)

- 6. [Benefiting From Single-Objective Feature Selection to Multiobjective Feature Selection: A Multiform Approach - PubMed](https://pubmed.ncbi.nlm.nih.gov/36346857/)

- 7. [安徽大学田野教授应邀为学院师生作学术报告-电气与信息工程学院](https://dqxx.ahut.edu.cn/info/1083/3680.htm)

- 8. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/scholar/paper)

- 9. [Particle swarm optimization based on filter-based population initialization method for feature selection in classification / Journal of Ambient Intelligence and Humanized Computing / Springer Nature Link](https://doi.org/10.1007/S12652-022-04444-1)

- 10. [Particle swarm optimisation for feature selection in classification: Novel initialisation… (2013) – Applied Soft Computing / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W1543715688)

- 11. 1342 

- 12. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - researchr publication](https://researchr.org/publication/JiaoNXZ24)

- 13. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 14. [A Prior-Guided Structure-Aware Multi-Objective Differential Evolution Method for High-Dimensional Feature Selection](https://www.mdpi.com/1999-4893/19/9/797)

- 15. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 16. [Improved SparseEA for sparse large-scale multi-objective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-021-00553-0)

- 17. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 18. [(PDF) Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling](https://www.researchgate.net/publication/364653518_Solving_Multiobjective_Feature_Selection_Problems_in_Classification_via_Problem_Reformulation_and_Duplication_Handling)

- 19. [A survey on swarm intelligence approaches to feature selection in data mining - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650219303104)

- 20. [An embedded vertical‐federated feature selection algorithm based on particle swarm optimisation - Zhang - 2023 - CAAI Transactions on Intelligence Technology - Wiley Online Library](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cit2.12122)

- 21. [Evolutionary computation for feature selection in classification: A comprehensive survey of solutions, applications and challenges - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650224001998)

- 22. [Benefiting From Single-Objective Feature Selection to Multiobjective Feature Selection: A Multiform Approach](https://oamonitor.ireland.openaire.eu/rpo/rcsi/search/publication)

- 23. [A knowledge-guided dimensionality reduction multiobjective evolutionary algorithm for large-scale sparse multiobjective optimization / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-01347-5)

- 24. [dblp: Bing Xue 0001](https://dblp.org/pid/40/6434-1.html)

- 25. [An Evolutionary Computation Based Feature Selection Method for Intrusion Detection - Xue - 2018 - Security and Communication Networks - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1155/2018/2492956)

- 26. [Towards multi-objective high-dimensional feature selection via evolutionary multitasking - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650224001561)

- 27. [(PDF) Large-scale multimodal multiobjective evolutionary optimization based on hybrid hierarchical clustering](https://www.researchgate.net/publication/368656035_Large-scale_multimodal_multiobjective_evolutionary_optimization_based_on_hybrid_hierarchical_clustering)

- 28. [Particle Swarm Optimization based Feature Selection](https://www.ijcaonline.org/archives/volume146/number6/25401-2016910789/)

### Batch 04: returned titles

- 1. [A Pattern Mining-Based Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://pubmed.ncbi.nlm.nih.gov/33378271/)

- 2. [Combining sparse evolutionary operators and deep reinforcement learning for large-scale sparse multiobjective optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494626006150)

- 3. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / NDL Search / National Diet Library](https://ndlsearch.ndl.go.jp/en/books/R100000136-I1360588389326737152)

- 4. [A two-stage evolutionary algorithm for large-scale sparse multiobjective optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650222000633)

- 5. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems (2019) – IEEE Transactions on Evolutionary Computation / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W2946739419)

- 6. [An Evolution Algorithm with Objective-Wise Variable Analysis for Sparse Large-Scale Multi-Objective Optimization / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-01230-3)

- 7. [An evolutionary algorithm based on dynamic sparse grouping for sparse large scale multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025523002517)

- 8. [A Survey on Evolutionary Multiobjective Feature Selection…](https://lacuna.tiptreesystems.com/work/a-survey-on-evolutionary-multiobjective-feature-selection)

- 9. [dblp: An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://dblp.uni-trier.de/rec/journals/tec/TianZWJ20.html)

- 10. [dblp: An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://dblp.dagstuhl.de/rec/journals/tec/TianZWJ20.html)

- 11. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems — Lacuna](https://lacuna.tiptreesystems.com/work/an-evolutionary-algorithm-for-large-scale-sparse-multiobjective-optimization/wrk_4e1ed4fc7318d6a4c57761d6901522af)

- 12. [A Generative Adversarial Network Guided Evolutionary Algorithm for Large-scale Sparse Multiobjective Optimization / Machine Intelligence Research / Springer Nature Link](https://doi.org/10.1007/s11633-025-1559-z)

- 13. [Multiple sparse detection-based evolutionary algorithm for large-scale sparse multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-022-00963-8)

- 14. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/)

- 15. [(PDF) A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges](https://www.researchgate.net/publication/372152809_A_Survey_on_Evolutionary_Multiobjective_Feature_Selection_in_Classification_Approaches_Applications_and_Challenges)

- 16. [An enhanced sparse multiobjective evolutionary algorithm in large-scale multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025525006085)

- 17. [Publications](https://homepages.ecs.vuw.ac.nz/~xuebing/Publications.html)

- 18. [A knowledge-guided dimensionality reduction multiobjective evolutionary algorithm for large-scale sparse multiobjective optimization / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-01347-5)

- 19. [Multiobjective Feature Selection Survey / PDF / Mathematical Optimization / Theoretical Computer Science](https://www.scribd.com/document/726578051/A-Survey-on-Evolutionary-Multiobjective-Feature-Selection-in-Classification-Approaches-Applications-and-Challenges)

- 20. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/scholar/paper)

- 21. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 22. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426028964)

- 23. [A Large-Scale Multi-Objective Evolutionary](https://openreview.net/attachment)

- 24. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 25. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 26. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 27. [A co-evolutionary algorithm based on sparsity clustering for sparse large-scale multi-objective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S095219762400352X)

- 28. [Improved SparseEA for sparse large-scale multi-objective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-021-00553-0)

- 29. [dblp: IEEE Transactions on Evolutionary Computation, Volume 28](https://dblp.dagstuhl.de/db/journals/tec/tec28.html)

- 30. [Hot off the Press: Proven Runtime Guarantees for How the MOEA/D Computes the Pareto Front From the Subproblem Solutions - Institut Polytechnique de Paris](https://researchportal.ip-paris.fr/fr/publications/hot-off-the-press-proven-runtime-guarantees-for-how-the-moead-com/)

- 31. [An adjoint feature-selection-based evolutionary algorithm for sparse large-scale multiobjective optimization / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-024-01752-1)

- 32. [We provide more discussion, details of the proposed algorithm and problem, and extra experimental](https://papers.neurips.cc/paper_files/paper/2022/file/7a583691ccfcf8945ab714b677ccbf0b-Supplemental-Conference.pdf)

- 33. [Large-Scale Sparse Multimodal Multiobjective Optimization via Multi-Stage Search and RL-Assisted Environmental Selection](https://www.mdpi.com/2079-9292/15/3/616)

- 34. [(PDF) Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks](https://www.researchgate.net/publication/339782398_Solving_Large-Scale_Multiobjective_Optimization_Problems_With_Sparse_Optimal_Solutions_via_Unsupervised_Neural_Networks)

- 35. [Attention-Guided Black-box Adversarial Attacks with Large-Scale Multiobjective Evolutionary Optimization](https://openreview.net/pdf)

- 36. [A multi-stage knowledge-guided evolutionary algorithm for large-scale sparse multi-objective optimization problems](https://www.researchgate.net/profile/Lei-Chen-315/publication/361317626_A_multi-stage_knowledge-guided_evolutionary_algorithm_for_large-scale_sparse_multi-objective_optimization_problems/links/63dfa6d4c97bd76a826ec4ba/A-multi-stage-knowledge-guided-evolutionary-algorithm-for-large-scale-sparse-multi-objective-optimization-problems.pdf)

- 37. [A conjugate gradient-assisted multi-objective evolutionary algorithm for fluence map optimization in radiotherapy treatment / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-022-00697-7)

- 38. ech

- 39. [An evolutionary algorithm based on dynamic sparse grouping for sparse large scale multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0020025523002517)

- 40. [ISSN 1870-4069](https://www.rcs.cic.ipn.mx/2025_154_8/Differential%20Evolution%20for%20Feature%20Selection_%20A%20Systematic%20Literature%20Review.pdf)

- 41. [(PDF) Multiple sparse detection-based evolutionary algorithm for large-scale sparse multiobjective optimization problems](https://www.researchgate.net/publication/366965955_Multiple_sparse_detection-based_evolutionary_algorithm_for_large-scale_sparse_multiobjective_optimization_problems)

- 42. [A Generative Adversarial Network Guided Evolutionary Algorithm for Large-scale Sparse Multiobjective Optimization / Request PDF](https://www.researchgate.net/publication/400380238_A_Generative_Adversarial_Network_Guided_Evolutionary_Algorithm_for_Large-scale_Sparse_Multiobjective_Optimization)

- 43. [dblp: Rui Wang 0017](https://dblp.org/pid/06/2293-17.html)

- 44. [(PDF) Multipopulation-Based Differential Evolution for Large-Scale Many-Objective Optimization](https://www.researchgate.net/publication/361479874_Multipopulation-Based_Differential_Evolution_for_Large-Scale_Many-Objective_Optimization)

- 45. [Yaochu Jin](https://www.csauthors.net/yaochu-jin/)

### Batch 05: returned titles

- 1. [Particle swarm optimisation for feature selection in classification: Novel initialisation and updating mechanisms - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494613003128)

- 2. [A Pattern Mining-Based Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://pubmed.ncbi.nlm.nih.gov/33378271/)

- 3. [A Survey on Evolutionary Computation Approaches to Feature Selection / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/document/7339682/)

- 4. [Particle swarm optimisation for feature selection in classification: Novel initialisation and updating mechanisms - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494613003128)

- 5. [Particle swarm optimisation for feature selection in classification: Novel initialisation and updating mechanisms](https://homepages.ecs.vuw.ac.nz/~xuebing/Papers/1-s2.0-S1568494613003128-main.pdf)

- 6. [A distributed PSO–SVM hybrid system with feature selection and parameter optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494607001299)

- 7. [JOURNAL OF LATEX CLASS FILES, VOL. , NO. ,](https://homepages.ecs.vuw.ac.nz/~xuebing/Papers/BingsurveyPaper.pdf)

- 8. [Publications 2014 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2014)

- 9. [A binary linear predictive evolutionary algorithm with feature analysis for multiobjective feature selection in classification - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S095219762500733X)

- 10. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/)

- 11. [Publications List - Users/BingXue / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://homepages.ecs.vuw.ac.nz/Users/BingXue/PublicationsList)

- 12. [PSO for FS: initialisation and updating](https://homepages.ecs.vuw.ac.nz/~xuebing/Papers/BingGECCO2016Tutorial.pdf)

- 13. [Publications](https://homepages.ecs.vuw.ac.nz/~xuebing/Publications.html)

- 14. [PSOLDA: A particle swarm optimization approach for enhancing classification accuracy rate of linear discriminant analysis - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494609000180)

- 15. [A two-dimensional (2-D) learning framework for Particle Swarm based feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0031320317304818)

- 16. [Teaching and Supervison](https://homepages.ecs.vuw.ac.nz/~xuebing/TeachingAndSupervison.html)

- 17. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/index.shtml)

- 18. [Publications All - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/PublicationsAll)

- 19. [Feature selection using bare-bones particle swarm optimization with mutual information - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320320306075)

- 20. [dblp: Xingyi Zhang 0001](https://dblp.org/pid/93/1107.html)

- 21. [Publications 2016 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2016)

- 22. [dblp: Fan Cheng 0001](https://dblp.org/pid/46/10961-1.html)

- 23. [Bib files](https://homepages.ecs.vuw.ac.nz/~xuebing/bib.html)

- 24. [dblp: Ye Tian 0009](https://dblp.org/pid/32/5495-9)

- 25. [dblp: Xi Pei](https://dblp.org/pid/36/8346.html)

- 26. [Publications 2022 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2022)

- 27. [Publications 2020 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2020)

- 28. [GitHub - thuiar/Adaptive-Batch-ParEGO: This repository contains Matlab implementation of the algorithm framework for adaptive batch-ParEGO · GitHub](https://github.com/thuiar/Adaptive-Batch-ParEGO)

- 29. [Talks - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Talks)

- 30. [PlatEMO/Doc/releasenote.md at master · BIMK/PlatEMO · GitHub](https://github.com/BIMK/PlatEMO/blob/master/Doc/releasenote.md)

- 31. [Publications 2018 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2018)

- 32. [dblp: Wei Fang 0001](https://dblp.org/pid/48/2709-1.html)

- 33. [dblp: Hau-San Wong](https://dblp.org/pid/69/2987)

- 34. [dblp: Yang Cao (disambiguation)](https://dblp.org/pid/25/7045.html)

- 35. [dblp: Yaochu Jin](https://dblp.org/pid/j/YaochuJin.html)

- 36. [dblp: Journal of Intelligent and Fuzzy Systems, Volume 34](https://dblp.org/db/journals/jifs/jifs34.html)

- 37. [dblp: IEEE International Conference on Granular Computing 2008](https://dblp.org/db/conf/grc/grc2008)

- 38. [dblp: Complex and Intelligent Systems, Volume 11](https://dblp.org/db/journals/comintsys/comintsys11.html)

- 39. [Releases · BIMK/PlatEMO · GitHub](https://github.com/BIMK/PlatEMO/releases)

- 40. [GitHub - ckshang/CoPSL: [IJCNN 2024 Oral] Collaborative Pareto Set Learning in Multiple Multi-Objective Optimization Problems https://arxiv.org/abs/2404.01224 · GitHub](https://github.com/ckshang/CoPSL)

### Batch 06: returned titles

- 1. [(PDF) Multi-Objective Feature Selection With Missing Data in Classification](https://www.researchgate.net/publication/351288956_Multi-Objective_Feature_Selection_With_Missing_Data_in_Classification)

- 2. [AMOFS: An Adversary-Aware Multi-Objective Evolutionary Feature Selection Framework with Convergence Guarantees for Malicious URL Detection by hui edward :: SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/518982b1-0b04-4b59-b4dc-7514c75e1e1c-MECA.pdf)

- 3. [Multiobjective evolutionary feature selection and fuzzy classification of contact centre data](https://sfera.unife.it/handle/11392/2404715)

- 4. [FASTENER Feature Selection for Inference from Earth Observation Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC7712113/)

- 5. [Permutation-based multi-objective evolutionary feature selection for high-dimensional data / Knowledge and Information Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s10115-026-02734-0)

- 6. [Full article: Feature Selection via Pareto Multi-objective Genetic Algorithms](https://doi.org/10.1080%2F08839514.2018.1444334)

- 7. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://www.mdpi.com/2078-2489/17/6/593)

- 8. [Parallel fractional dominance MOEAs for feature subset selection in big data - ScienceDirect](https://doi.org/10.1016/j.swevo.2024.101687)

- 9. [Multi-phase evolutionary search space shrinking for large-scale multi-objective feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494625010683)

- 10. [BGR-FS: A bandit-guided redundancy-aware framework for high-dimensional multi-objective feature selection / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-00848-7)

- 11. [Parallel fractional dominance MOEAs for feature subset selection in big data - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650224002256)

- 12. [Parallel chaotic bi-objective evolutionary algorithms for scalable feature subset selection via migration strategy - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494625013225)

- 13. [Full article: Feature Selection via Pareto Multi-objective Genetic Algorithms](https://www.tandfonline.com/doi/full/10.1080/08839514.2018.1444334)

- 14. [Feature Selection via Pareto Multi-objective Genetic Algorithms](https://www.tandfonline.com/doi/pdf/10.1080/08839514.2018.1444334)

- 15. [6  Feature Selection – Applied Machine Learning Using mlr3 in R](https://mlr3book.mlr-org.com/chapters/chapter6/feature_selection.html)

- 16. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://doi.org/10.3390/info17060593)

- 17. [Comparison of Profit-Based Multi-Objective Approaches for Feature Selection in Credit Scoring](https://www.mdpi.com/1999-4893/14/9/260)

- 18. [Targeted Pareto Optimization for Subset Selection With Monotone Objective Function and Cardinality Constraint / Request PDF](https://www.researchgate.net/publication/382549576_Targeted_Pareto_Optimization_for_Subset_Selection_With_Monotone_Objective_Function_and_Cardinality_Constraint)

- 19. [Selection of investment portfolios with social responsibility: a multiobjective model and a Tabu search method / Applied Intelligence / Springer Nature Link](https://link.springer.com/article/10.1007/s10489-022-03169-0)

- 20. [FASTENER Feature Selection for Inference from Earth Observation Data](https://www.mdpi.com/1099-4300/22/11/1198)

- 21. [CN121880873A – High-dimensional evolutionary feature selection method fusing filtering and packaging strategies / Patsnap Eureka](https://eureka.patsnap.com/patent/CN121880873A)

- 22. [Biodata-centric cardiovascular disease prediction using multi-objective genetic algorithm-driven deep ensembles / Scientific Reports](https://www.nature.com/articles/s41598-025-28771-3)

- 23. [Multi-objective feature selection using hybridization of a genetic algorithm and direct multisearch for key quality characteristic selection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025520302139)

- 24. [Multiple objective metaheuristics for feature selection based on stakeholder requirements in credit scoring - ScienceDirect](https://www.sciencedirect.com/science/article/am/pii/S0167923621002244)

- 25. [(PDF) Multiobjective Optimization of Classifiers by Means of 3-D Convex Hull Based Evolutionary Algorithm](https://www.researchgate.net/publication/269706667_Multiobjective_Optimization_of_Classifiers_by_Means_of_3-D_Convex_Hull_Based_Evolutionary_Algorithm)

- 26. [Multi-objective based radiomic feature selection for lesion malignancy classification](https://pmc.ncbi.nlm.nih.gov/articles/PMC7193672/)

- 27. Abstract

- 28. [An active learning Gaussian modeling based multi-objective evolutionary algorithm using population guided weight vector evolution strategy](https://aimspress.com/article/doi/10.3934/mbe.2023878)

- 29. [An empirical study on pareto based multi-objective feature selection for software defect prediction](https://jacknichao.github.io/pdf/ni2019mofes.pdf)

- 30. [Elitism based Multi-Objective Differential Evolution for feature selection: A filter approach with an efficient redundancy measure / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1016/j.jksuci.2017.08.001)

- 31. [ROC with Cost Pareto Frontier Feature Selection Using Search Methods / Data-Enabled Discovery and Applications / Springer Nature Link](https://link.springer.com/article/10.1007/s41688-020-00040-4)

- 32. [Release Notes / sklearn-genetic-opt](https://sklearngeneticopt.rodrigo-arenas.com/versions/0.14/release-notes)

- 33. [Open Access proceedings Journal of Physics: Conference series](https://repositorio.ie.edu/bitstreams/7dc8157f-420d-46e3-81be-f3181cd2c6be/download)

- 34. [](https://academic.oup.com/bioinformatics/advance-article-pdf/doi/10.1093/bioinformatics/btad384/50628603/btad384.pdf)

- 35. algorithms

- 36. [A joint multiobjective optimization of feature selection and classifier design for high-dimensional data classification - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0020025523000695)

- 37. [(PDF) Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling](https://www.researchgate.net/publication/364653518_Solving_Multiobjective_Feature_Selection_Problems_in_Classification_via_Problem_Reformulation_and_Duplication_Handling)

- 38. [A Multimodal Multi-Objective Feature Selection Method for Intelligent Rating Models of Unmanned Highway Toll Stations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11506808/)

- 39. [Multiobjective Feature Selection Survey / PDF / Mathematical Optimization / Theoretical Computer Science](https://www.scribd.com/document/726578051/A-Survey-on-Evolutionary-Multiobjective-Feature-Selection-in-Classification-Approaches-Applications-and-Challenges)

- 40. [Full article: A feature-based intelligent deduplication compression system with extreme resemblance detection](https://www.tandfonline.com/doi/full/10.1080/09540091.2020.1862058)

- 41. [Metaheuristic Algorithms for Feature Selection (2014-2024) - ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S1947828326000019)

- 42. [A Comprehensive Survey on Symbolic Regression: State-of-the-Art Approaches, Key Applications, Benchmark Evaluations, and Future Research Directions / Archives of Computational Methods in Engineering / Springer Nature Link](https://link.springer.com/article/10.1007/s11831-026-10681-w)

- 43. [(PDF) Multiobjective feature selection for key quality characteristic identification in production processes using a nondominated-sorting-based whale optimization algorithm](https://www.researchgate.net/publication/344893154_Multiobjective_feature_selection_for_key_quality_characteristic_identification_in_production_processes_using_a_nondominated-sorting-based_whale_optimization_algorithm)

- 44. [(PDF) A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges](https://www.researchgate.net/publication/372152809_A_Survey_on_Evolutionary_Multiobjective_Feature_Selection_in_Classification_Approaches_Applications_and_Challenges)

- 45. [CN120277378A – Feature selection method based on differential evolution algorithm, medium and equipment / Patsnap Eureka](https://eureka.patsnap.com/patent/CN120277378A)

- 46. [US12547930B2 – Feature selection and hyperparameter optimization using LDS / Patsnap Eureka](https://eureka.patsnap.com/patent/US12547930B2)

- 47. [Software Defect Prediction With Quantum‐Inspired Feature Selection - Uddin - 2026 - Applied Computational Intelligence and Soft Computing - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1155/acis/8864479)

- 48. [](https://mail.openbioinformaticsjournal.com/VOLUME/19/ELOCATOR/e18750362389838/FULLTEXT/)

- 49. [Biodata-centric cardiovascular disease prediction using multi-objective genetic algorithm-driven deep ensembles - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12686456/)

- 50. [Multi-objective gold rush optimization algorithm: Theoretical Extensions and applications in UAV path planning](https://pmc.ncbi.nlm.nih.gov/articles/PMC13252791/)

### Batch 07: returned titles

- 1. [Frontiers / Architectural good practices for reproducible benchmarking in protein machine learning](https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2026.1925740/full)

- 2. [Critical assessment in the age of AI: challenges and opportunities for computational biology / Bioinformatics Advances / Oxford Academic](https://academic.oup.com/bioinformaticsadvances/article/6/1/vbag290/8931828)

- 3. [Critical assessment in the age of AI: challenges and opportunities for computational biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC13675102/)

- 4. [Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy](https://www.mdpi.com/2306-5354/13/10/1229)

- 5. [Simulation Tests of Methods in Evolution, Ecology, and Systematics: Pitfalls, Progress, and Principles / Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-ecolsys-102320-093722)

- 6. [Architectural good practices for reproducible benchmarking in protein machine learning / Frontiers](https://www.frontiersin.app/articles/fbinf-2026-1925740)

- 7. [Challenges and best practices in omics benchmarking / Nature Reviews Genetics](https://www.nature.com/articles/s41576-023-00679-6)

- 8. [Benchmarking Best Practices for Maintenance, Reliability and Asset Management, Third Edition](https://ndl.ethernet.edu.et/bitstream/123456789/25616/1/Benchmarking%20Best%20Practices%20for%20Maintenance%2C%20Reliability%20and%20Asset%20Management.pdf)

- 9. [Multi-objective feature selection using hybridization](https://andali89.github.io/homepage/pubs/2020_GADMS.pdf)

- 10. [Progressive sampling-based Bayesian optimization for efficient and automatic machine learning model selection - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5617811/)

- 11. [A white paper on good research practices in benchmarking: The case of cluster analysis - Van Mechelen - 2023 - WIREs Data Mining and Knowledge Discovery - Wiley Online Library](https://wires.onlinelibrary.wiley.com/doi/10.1002/widm.1511)

- 12. [Multi-objective feature selection using hybridization of a genetic algorithm and direct multisearch for key quality characteristic selection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025520302139)

- 13. [Measuring the microbiome: Best practices for developing and benchmarking microbiomics methods - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7744638/)

- 14. [Benchmarking](https://api.pageplace.de/preview/DT0400.9781136426575_A23846139/preview-9781136426575_A23846139.pdf)

- 15. [A short overview and common pitfalls of](https://www.gm.th-koeln.de/~naujoks/Pub.d/VIBN22.pdf)

- 16. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://doi.org/10.3390/info17060593)

- 17. [evo-gafs · PyPI](https://pypi.org/project/evo-gafs/0.1.1/)

- 18. [Benchmarking in Optimization: Best Practice and Open Issues — Lacuna](https://lacuna.tiptreesystems.com/work/benchmarking-in-optimization-best-practice-and-open-issues)

- 19. [Parallel fractional dominance MOEAs for feature subset selection in big data - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650224002256)

- 20. [Simulation Tests of Methods in Evolution, Ecology, and Systematics: Pitfalls, Progress, and Principles - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10723108/)

- 21. [BGR-FS: A bandit-guided redundancy-aware framework for high-dimensional multi-objective feature selection / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-00848-7)

- 22. [Alternative feature selection with user control / International Journal of Data Science and Analytics / Springer Nature Link](https://link.springer.com/article/10.1007/s41060-024-00527-8)

- 23. [Measuring the microbiome: Best practices for developing and benchmarking microbiomics methods / Computational and Structural Biotechnology Journal](https://spj.science.org/doi/10.1016/j.csbj.2020.11.049)

- 24. [Designing New Metaheuristics: Manual Versus Automatic Approaches / Intelligent Computing](https://doi.org/10.34133%2Ficomputing.0048)

- 25. [The evolutionary approach to benchmarking was illustrated in Figure 2.1, it clearly showed that benchmarking concepts and their meanings had to be seen as ever-changing, dynamic processes.](https://eprints.usm.my/47507/1/LEE%20YEAN%20PIN24.pdf)

- 26. [An innovative feature selection method for support vector machines and its test on the estimation of the credit risk of default - Sariev - 2019 - Review of Financial Economics - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/rfe.1049)

- 27. [CN121880873A – High-dimensional evolutionary feature selection method fusing filtering and packaging strategies / Patsnap Eureka](https://eureka.patsnap.com/patent/CN121880873A)

- 28. [GASearchCV / sklearn-genetic-opt](https://sklearngeneticopt.rodrigo-arenas.com/versions/0.14/api/gasearchcv)

- 29. [(PDF) Instance Selection-Based Surrogate-Assisted Genetic Programming for Feature Learning in Image Classification](https://www.researchgate.net/publication/354255353_Instance_Selection-Based_Surrogate-Assisted_Genetic_Programming_for_Feature_Learning_in_Image_Classification)

- 30. [Parallel fractional dominance MOEAs for feature subset selection in big data - ScienceDirect](https://doi.org/10.1016/j.swevo.2024.101687)

- 31. [An instance of a feature selection representation / Download Scientific Diagram](https://www.researchgate.net/figure/An-instance-of-a-feature-selection-representation_fig4_339629173)

- 32. [Feature subset selection for big data via parallel chaotic binary differential evolution and feature-level elitism - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0045790625001752)

- 33. [GitHub - vagnerereno/A-GRASPQ-FS · GitHub](https://github.com/vagnerereno/A-GRASPQ-FS)

- 34. [A multi-strategy framework for enhancing Harris hawks optimization for global optimization problems / Scientific Reports](https://www.nature.com/articles/s41598-026-45741-5)

- 35. [Non-revisiting stochastic search revisited: Results, perspectives, and future directions - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650220304818)

- 36. [Full article: Using genetic programming for context-sensitive feature scoring in classification problems](https://www.tandfonline.com/doi/full/10.1080/09540091.2011.630065)

- 37. [mlr3book/book/chapters/chapter6/feature_selection.qmd at main · mlr-org/mlr3book · GitHub](https://github.com/mlr-org/mlr3book/blob/main/book/chapters/chapter6/feature_selection.qmd)

- 38. [Feature Stability as a Trust Layer for Feature Selection: Resampling-Based Recurrence Profiles Beyond Predictive Performance / MDPI](https://www.mdpi.com/2227-7390/14/13/2372)

- 39. [Multi-phase evolutionary search space shrinking for large-scale multi-objective feature selection](https://ouci.dntb.gov.ua/en/works/lRr630J0/)

- 40. [Package 'mlr3fselect' reference manual](https://mlr-org.r-universe.dev/mlr3fselect/doc/manual.html)

- 41. [[Revue de papier] Enhancing Diversity in Multi-objective Feature Selection](https://www.themoonlight.io/fr/review/enhancing-diversity-in-multi-objective-feature-selection)

- 42. [Wrapper-based selection of genetic features in genome-wide association studies through fast matrix operations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3606421/)

- 43. [Help for package mlr3fselect](https://mirror.oit.ncsu.edu/cran/web/packages/mlr3fselect/refman/mlr3fselect.html)

- 44. [Grammar-guided genetic programming and dimensional consistency: Application to non-parametric identification in mechanics / Request PDF](https://www.researchgate.net/publication/223718942_Grammar-guided_genetic_programming_and_dimensional_consistency_Application_to_non-parametric_identification_in_mechanics)

- 45. [NeuroEvoBench: Benchmarking Evolutionary Optimizers for Deep Learning Applications](https://arxiv.org/abs/2311.02394)

- 46. [(PDF) Statistical Methods for Construction of Neural Networks.](https://www.researchgate.net/publication/221139559_Statistical_Methods_for_Construction_of_Neural_Networks)

### Batch 08: returned titles

- 1. [Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy](https://www.mdpi.com/2306-5354/13/10/1229)

- 2. [Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy / JoVE Visualize](https://visualize.jove.com/42939084-nested-evaluation-of-sparse-multi-objective-evolutionary-gene-panel-discovery-for-diabetic-nephropathy)

- 3. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://www.mdpi.com/2078-2489/17/6/593)

- 4. [Benchmarking in Optimization: Best Practice and Open Issues](https://arxiv.org/abs/2007.03488)

- 5. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://doi.org/10.3390/info17060593)

- 6. [Vol. 17, Issue 6 / Information / MDPI](https://www.mdpi.com/2078-2489/17/6)

- 7. [Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy - CiteDrive](https://www.citedrive.com/en/viewer/)

- 8. [Benchmarking in optimization: Best practice and open issues - Catalog - SLUB Dresden](https://katalog.slub-dresden.de/en/id/0-1745111069)

- 9. [Benchmarking in Optimization: Best Practice and Open Issues — Lacuna](https://lacuna.tiptreesystems.com/work/benchmarking-in-optimization-best-practice-and-open-issues)

- 10. [Benchmarking in Optimization: Best Practice and Open Issues / Department of Information Systems](https://www.wi.uni-muenster.de/research/publications/160334)

- 11. [OPUS 4 / Benchmarking in Optimization: Best Practice and Open Issues](https://cos.bibl.th-koeln.de/frontdoor/index/index/year/2020/docId/902)

- 12. [(PDF) CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://www.researchgate.net/publication/407119785_CORAL_A_Rank-Memory_Search_Framework_for_Multi-Objective_Feature_Selection)

- 13. [[PDF] Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy / CiteDrive](https://www.citedrive.com/en/discovery/nested-evaluation-of-sparse-multi-objective-evolutionary-gene-panel-discovery-for-diabetic-nephropathy/)

- 14. [Benchmarking in Optimization: Best Practice and Open Issues](https://www.catalyzex.com/paper/benchmarking-in-optimization-best-practice)

- 15. [Benchmarking in Optimization: Best Practice and Open Issues (2020) – arXiv (Cornell University) / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W3038891809)

- 16. [Benchmarking in Optimization: Best Practice and Open Issues / Institut für Wirtschaftsinformatik](https://www.wi.uni-muenster.de/de/forschung/publikationen/160334)

- 17. [Information / June 2026 - Browse Articles](https://www.mdpi.com/2078-2489/17/6)

- 18. Ciplus  

- 19. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection](https://ouci.dntb.gov.ua/en/works/9JQdZ85N/)

- 20. [Benchmarking in Optimization: Best Practice and Open Issues · paper-with-me](https://khansong-paper-with-me.hf.space/paper/benchmarking-in-optimization-best-practice)

- 21. [Benchmarking in Optimization: Best Practice and Open Issues · mlsanity](https://mlsanity.com/paper/2007.03488/)

- 22. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417426028964)

- 23. [dblp: Benchmarking in Optimization: Best Practice and Open Issues.](https://dblp.org/rec/journals/corr/abs-2007-03488.html)

- 24. [CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection - researchr publication](https://researchr.org/publication/LiJH26-0)

- 25. [(PDF) Benchmarking in Optimization: Best Practice and Open Issues](https://www.researchgate.net/publication/342763159_Benchmarking_in_Optimization_Best_Practice_and_Open_Issues)

- 26. [Search Results - "Han, Chunyu" :: Library Catalog](https://iris.sena.edu.co/EDS/Search)

- 27. [Benchmarking in Optimization: Best Practice and Open Issues · Pith Review](https://pith.science/paper/2007.03488)

- 28. [212  LfBA / WMA](https://www.th-koeln.de/mam/downloads/projekte_und_publikationen_2021_digital.pdf)

- 29. [Multi-phase evolutionary search space shrinking for large-scale multi-objective feature selection](https://ouci.dntb.gov.ua/en/works/lRr630J0/)

- 30. [Search Results - "Li, Heming" :: Library Catalog](https://iris.sena.edu.co/EDS/Search)

- 31. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 32. [A multi-objective evolutionary algorithm for feature selection incorporating dominance-based initialization and duplica…](https://ouci.dntb.gov.ua/en/works/7PMdGQzx/)

- 33. [Forschung und](https://www.th-koeln.de/mam/downloads/deutsch/forschung/projekte_und_publikationen_2021.pdf)

- 34. [An Evolution Algorithm with Objective-Wise Variable Analysis for Sparse Large-Scale Multi-Objective Optimization / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-01230-3)

- 35. [Benchmarking in Optimization:](https://cavalab.org/assets/papers/Bartz-Beielstein%20et%20al.%20-%202020%20-%20Benchmarking%20in%20Optimization%20Best%20Practice%20and%20Op.pdf)

- 36. [An adjoint feature-selection-based evolutionary algorithm for sparse large-scale multiobjective optimization / Complex & Intelligent Systems / Springer Nature Link](https://doi.org/10.1007/s40747-024-01752-1)

- 37. [Multiple sparse detection-based evolutionary algorithm for large-scale sparse multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-022-00963-8)

- 38. [Improved SparseEA for sparse large-scale multi-objective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-021-00553-0)

- 39. [Frontiers / Two-stage sparse multi-objective evolutionary algorithm for channel selection optimization in BCIs](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1400077/full)

- 40. [An adjoint feature-selection-based evolutionary algorithm for sparse large-scale multiobjective optimization / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-024-01752-1)

- 41. [(PDF) Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks](https://www.researchgate.net/publication/339782398_Solving_Large-Scale_Multiobjective_Optimization_Problems_With_Sparse_Optimal_Solutions_via_Unsupervised_Neural_Networks)

- 42. [A conjugate gradient-assisted multi-objective evolutionary algorithm for fluence map optimization in radiotherapy treatment / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-022-00697-7)

- 43. [Evolution algorithm with adaptive genetic operator and dynamic scoring mechanism for large-scale sparse many-objective optimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC11920420/)

### Batch 09: returned titles

- 1. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 2. [dblp: Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems.](https://dblp.org/rec/journals/swevo/KroppND22.html)

- 3. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 4. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Request PDF](https://www.researchgate.net/publication/369219815_Improved_Evolutionary_Operators_for_Sparse_Large-Scale_Multiobjective_Optimization_Problems)

- 5. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650221001875)

- 6. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems / Documentos - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64925ad817cf843cfd3)

- 7. [Kalyanmoy Deb / ScienceDirect](https://www.sciencedirect.com/author/7006019904/kalyanmoy-deb)

- 8. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 9. [CV · Ian Kropp](https://iankropp.com/cv/)

- 10. [dblp: A. Pouyan Nejadhashemi](https://dblp.org/pid/164/4251.html)

- 11. [CURRICULUM VITAE](https://ifas.ufl.edu/media/ifasufledu/docs/searches/chair-abe/nejadhashemi-CV.pdf)

- 12. [Publications 2026 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2026)

- 13. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64925ad817cf843cfd3)

- 14. [dblp: IEEE Transactions on Evolutionary Computation, Volume 28](https://dblp.org/db/journals/tec/tec28.html)

- 15. [A. Pouyan Nejadhashemi / ScienceDirect](https://www.sciencedirect.com/author/6504453135/a-pouyan-nejadhashemi)

- 16. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective...](https://bishtref.com/articles/10.1109/tevc.2023.3256183)

- 17. [Publications 2025 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2025)

- 18. [Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey / ACM Computing Surveys](https://doi.org/10.1145/3734865)

- 19. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems](https://agris.fao.org/search/en/providers/122535/records/65df81b87c7033e84bede227)

- 20. [Publications 2023 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2023)

- 21. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 28, Issue 2, April 2024](https://ieee-cis.blogspot.com/2024/05/ieee-transactions-on-evolutionary.html)

- 22. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems](https://agris.fao.org/search/ar/records/65df81b87c7033e84bede227)

- 23. [Benefits of sparse population sampling in multi-objective evolutionary...](https://bishtref.com/articles/10.1016/j.swevo.2021.101025)

- 24. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems / Dokumentuak - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64925ad817cf843cfd3)

- 25. [ISSN: 2182-2069 / E-ISSN: 2182-2077](https://jisis.org/wp-content/uploads/2026/03/2026.I1.038.pdf)

- 26. [An Jaccard similarity coefficient-based evolutionary algorithm for sparse large-scale multi-objective optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650225004262)

- 27. [Ian Kropp](https://www.csauthors.net/ian-kropp/)

- 28. [Operations Research and Fuzziology $Ê†](https://pdf.hanspub.org/orf20230200000_86798550.pdf)

- 29. [Digitized and Integrated Water Resources Management and Utilization by an](https://watermark02.silverchair.com/zkag016.pdf)

- 30. [Kalyanmoy Deb](https://www.egr.msu.edu/~kdeb/papers/kdebCV_Nov16.pdf)

- 31. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 32. [Publications All - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/PublicationsAll)

- 33. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems - 科研通](https://www.ablesci.com/assist/detail)

- 34. [Publications 2024 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2024)

- 35. [Progress Report 2023 - Groups/DataScienceForAquaculture / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/DataScienceForAquaculture/ProgressReport2023)

### Batch 10: returned titles

- 1. [Best practices for comparing optimization algorithms / Optimization and Engineering / Springer Nature Link](https://doi.org/10.1007%2Fs11081-017-9366-1)

- 2. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650211000034)

- 3. [Best practices for comparing optimization algorithms](https://arxiv.org/abs/1709.08242)

- 4. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://explore.openaire.eu/search/publication)

- 5. [Consistencies and contradictions of performance metrics in multiobjective optimization - PubMed](https://pubmed.ncbi.nlm.nih.gov/25415945/)

- 6. [Best practices for comparing optimization algorithms (2017) – Optimization and Engineering / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W3105968297)

- 7. [(PDF) Best Practices for Comparing Optimization Algorithms](https://www.researchgate.net/publication/317724973_Best_Practices_for_Comparing_Optimization_Algorithms)

- 8. [Best practices for comparing optimization algorithms / alphaXiv](https://www.alphaxiv.org/abs/1709.08242v1)

- 9. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms – ScienceOpen](https://www.scienceopen.com/document)

- 10. [dblp: A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms.](https://dblp.org/rec/journals/swevo/DerracGMH11.html)

- 11. [BGR-FS: A bandit-guided redundancy-aware framework for high-dimensional multi-objective feature selection / Journal of King Saud University Computer and Information Sciences / Springer Nature Link](https://link.springer.com/article/10.1007/s44443-026-00848-7)

- 12. [Rankless / A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://www.rankless.org/hit-papers/10.1016/j.swevo.2011.02.002)

- 13. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://oamonitor.ireland.openaire.eu/national/search/publication)

- 14. [Best Practices for Algorithm Benchmarking / PDF / Mathematical Optimization / Program Optimization](https://www.scribd.com/document/467758487/Best-Practices-for-Comparing-Optimization-Algorith)

- 15. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms / Documents - Universidad de Jaén](https://investigacion.ujaen.es/documentos/5f1ce1a429995265e44db608)

- 16. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms / Daniel Molina profile](https://dmolina.github.io/publication/derrac-20113/)

- 17. [au:Beiranvand_V in:math - SciRate Search](https://scirate.com/search)

- 18. [Fast Greedy Subset Selection From Large Candidate Solution Sets in Evolutionary Multiobjective Optimization](https://doi.org/10.1109%2FTEVC.2021.3103386)

- 19. [A Knowledge-Guided Competitive Co-Evolutionary Algorithm for Feature Selection](https://www.mdpi.com/2076-3417/14/11/4501)

- 20. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://oamonitor.ireland.openaire.eu/rfo/irish-research-elibrary2/search/publication)

- 21. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swar…](https://ouci.dntb.gov.ua/en/works/45mQe0j4/)

- 22. [Dynamic Shannon Performance in a Multiobjective Particle Swarm Optimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC7515356/)

- 23. [Best practices for comparing optimization algorithms / Request PDF](https://www.researchgate.net/publication/386916162_Best_practices_for_comparing_optimization_algorithms)

- 24. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://explore.metascienceobservatory.org/papers/W2096166399)

- 25. [Best practices for comparing optimization algorithms — Scifaro](https://scifaro.com/en/abs/best-practices-for-comparing-optimization-algorithms-1709.08242)

- 26. [A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms](https://sci2s.ugr.es/sites/default/files/ficherosPublicaciones/1374_2011-Derrac-SWEVO.pdf)

- 27. [Reliability of Indicator-Based Comparison Results of Evolutionary Multi-objective Algorithms - CityUHK Scholars](https://scholars.cityu.edu.hk/en/publications/reliability-of-indicator-based-comparison-results-of-evolutionary/)

- 28. [Evolutionary diversity optimization using multi-objective indicators](https://digital.library.adelaide.edu.au/items/9daf1dcd-6745-4f89-879f-ccd4ed1faecb)

- 29. [(Open Access) Best practices for comparing optimization algorithms (2017) / Vahid Beiranvand / 81 Citations](https://scispace.com/papers/best-practices-for-comparing-optimization-algorithms-1695nzutq0)

- 30. [A Survey on the Hypervolume Indicator in Evolutionary Multiobjective Optimization (2020) – IEEE Transactions on Evolutionary Computation / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W3046910774)

### Batch 11: returned titles

- 1. [Subset Selection by Pareto Optimization](https://proceedings.neurips.cc/paper/2015/hash/b4d168b48157c623fbd095b4a565b5bb-Abstract.html)

- 2. [Subset Selection by Pareto Optimization](https://papers.nips.cc/paper/2015/file/b4d168b48157c623fbd095b4a565b5bb-Paper.pdf)

- 3. [POSS - LAMDA](https://www.lamda.nju.edu.cn/code_POSS.ashx)

- 4. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / NDL Search / National Diet Library](https://ndlsearch.ndl.go.jp/en/books/R100000136-I1360588389326737152)

- 5. [(PDF) Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling](https://www.researchgate.net/publication/364653518_Solving_Multiobjective_Feature_Selection_Problems_in_Classification_via_Problem_Reformulation_and_Duplication_Handling)

- 6. [](https://www.lamda.nju.edu.cn/qianc/code_pocss.html)

- 7. [Subset Selection by Pareto Optimization with Recombination / Proceedings of the AAAI Conference on Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/5621)

- 8. [Export Reviews, Discussions, Author Feedback and Meta-Reviews](https://proceedings.neurips.cc/paper/2015/file/b4d168b48157c623fbd095b4a565b5bb-Reviews.html)

- 9. [Page History - Yang Yu](https://www.lamda.nju.edu.cn/yuy/%28X%281%29S%28fc4zqdfgz4ploa4qv024zkey%29%29/History.aspx)

- 10. [(PDF) A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges](https://www.researchgate.net/publication/372152809_A_Survey_on_Evolutionary_Multiobjective_Feature_Selection_in_Classification_Approaches_Applications_and_Challenges)

- 11. [](https://www.lamda.nju.edu.cn/qianc/code_poseqsel.html)

- 12. [Multiobjective Feature Selection Survey / PDF / Mathematical Optimization / Theoretical Computer Science](https://www.scribd.com/document/726578051/A-Survey-on-Evolutionary-Multiobjective-Feature-Selection-in-Classification-Approaches-Applications-and-Challenges)

- 13. [Subset selection by Pareto optimization](https://explore.metascienceobservatory.org/papers/W2187602868)

- 14. [](https://www.lamda.nju.edu.cn/qianc/code_porss.html)

- 15. [Subset Selection by Pareto Optimization - Conftrace](https://conftrace.com/papers/2954-subset-selection-by-pareto-optimization)

- 16. [Subset Selection by Pareto Optimization with Recombination](https://ojs.aaai.org/index.php/AAAI/article/download/5621/5477)

- 17. [Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey / ACM Computing Surveys](https://doi.org/10.1145/3734865)

- 18. [Subset selection by Pareto optimization / Request PDF](https://www.researchgate.net/publication/312274604_Subset_selection_by_Pareto_optimization)

- 19. [A Survey on Evolutionary Multiobjective Feature Selection…](https://lacuna.tiptreesystems.com/work/a-survey-on-evolutionary-multiobjective-feature-selection)

- 20. [Publications](https://homepages.ecs.vuw.ac.nz/~xuebing/Publications.html)

- 21. [Solving Multiobjective Feature Selection Problems in Classification…](https://tlooto.com/paper/150259695739)

- 22. [Solving Multiobjective Feature Selection Problems in Clas… / Minicod](https://www.minicod.com/papers/solving-multiobjective-feature-selection-problems-in-classification-via-problem-reformulation-and-duplication-handling-326f28ea)

- 23. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 24. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 25. [A multiple knowledge-based evolutionary algorithm for sparse large-scale multi-objective problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0952197625012825)

- 26. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417426028964)

- 27. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/scholar/paper)

- 28. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 29. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges (2023) / Ruwang Jiao / 55 Citations](https://scispace.com/papers/a-survey-on-evolutionary-multiobjective-feature-selection-in-a0cze92a)

- 30. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 31. [A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges - 科研通](https://www.ablesci.com/assist/detail)

- 32. [Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling - 科研通](https://www.ablesci.com/scholar/paper)

- 33. [Heterogeneous operator mechanism and stochastic configuration network-enhanced large-scale multi-objective evolutionary algorithm / Journal of Computational Design and Engineering / Oxford Academic](https://academic.oup.com/jcde/article/13/2/1/8407630)

- 34. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426028964)

- 35. [dblp: Ruwang Jiao](https://dblp.dagstuhl.de/pid/204/4700.html)

- 36. [Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling - 科研通](https://www.ablesci.com/assist/detail)

- 37. [Heterogeneous operator mechanism and stochastic configuration network-enhanced large-scale multi-objective evolutionary algorithm / Journal of Computational Design and Engineering / Oxford Academic](https://0-academic-oup-com.legcat.gov.ns.ca/jcde/article/13/2/1/8407630)

- 38. [dblp: Ruwang Jiao](https://dblp.uni-trier.de/pid/204/4700.html)

- 39. [A multiple knowledge-based evolutionary algorithm for sparse large-scale multi-objective problems - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0952197625012825)

- 40. [A Joint-Encoding Evolutionary Algorithm for Multimodal Multiobjective Feature Selection in Classification](https://www.connectedpapers.com/main/5591aef0b5e4da6ad28e8ed24fbc76e008c4101c)

- 41. [Multi-objective feature selection in high-dimensional classification: An importance-guided and historical information-a…](https://ouci.dntb.gov.ua/en/works/4aBpL5WN/)

- 42. [Multi-Objective Feature Selection: Reviewing Decades of Research](https://www.connectedpapers.com/main/9a3041f01ff358dc0ad472ba38bf1b3bcef6e471)

- 43. [Procedure of MOEA/PSL. / Download Scientific Diagram](https://www.researchgate.net/figure/Procedure-of-MOEA-PSL_fig1_339782398)

- 44. [A co-evolutionary algorithm based on sparsity clustering for sparse large-scale multi-objective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S095219762400352X)

- 45. [未来科学与工程学院 - www.优德88.cpm](https://www.sxmjet.com/web/rwjiao/)

- 46. [An evolutionary multiobjective method based on dominance and decomposition for feature selection in classification](https://www.connectedpapers.com/main/3378210748db1b5e08b7f358385bb8794089d940)

- 47. [Multiple sparse detection-based evolutionary algorithm for large-scale sparse multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-022-00963-8)

- 48. [Frontiers / Two-stage sparse multi-objective evolutionary algorithm for channel selection optimization in BCIs](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1400077/full)

- 49. [An adjoint feature-selection-based evolutionary algorithm for sparse large-scale multiobjective optimization / Complex & Intelligent Systems / Springer Nature Link](https://doi.org/10.1007/s40747-024-01752-1)

- 50. [GitHub - thuiar/Adaptive-Batch-ParEGO: This repository contains Matlab implementation of the algorithm framework for adaptive batch-ParEGO · GitHub](https://github.com/thuiar/Adaptive-Batch-ParEGO)

- 51. [Towards Multi-Objective High-Dimensional Feature Selection via Evolutionary Multitasking](https://arxiv.org/abs/2401.01563)

### Batch 12: returned titles

- 1. 1424

- 2. [A survey on swarm intelligence approaches to feature selection in data mining - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650219303104)

- 3. [Hybrid genetic algorithms for feature selection - PubMed](https://pubmed.ncbi.nlm.nih.gov/15521491/)

- 4. [Hybrid genetic algorithms for feature selection / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/document/1335448/)

- 5. [ORCID](https://orcid.org/0000-0002-6930-6863)

- 6. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/A-multi-objective-evolutionary-algorithm-with-interval/99683066102346)

- 7. [Hybrid genetic algorithms for feature selection](https://openalex.org/W2100253618)

- 8. [A survey on swarm intelligence approaches to feature selection in data mining / CiNii Research](https://cir.nii.ac.jp/crid/1360016869819097984)

- 9. [A survey on swarm intelligence approaches to feature selection in data mining](https://explore.metascienceobservatory.org/papers/W3004565805)

- 10. [Hybrid genetic algorithms for feature selection](https://www.researchgate.net/publication/8199995_Hybrid_genetic_algorithms_for_feature_selection)

- 11. [dblp: A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification.](https://dblp.org/rec/journals/asc/XueCN22.html)

- 12. [dblp: A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification.](https://dblp.dagstuhl.de/rec/journals/asc/XueCN22.html)

- 13. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - EdUHK Research Repository](https://repository.eduhk.hk/en/publications/a-multi-objective-evolutionary-algorithm-with-interval-based-init/)

- 14. [A survey on swarm intelligence approaches to feature...](https://www.canyam.com/en/article/a-survey-on-swarm-intelligence-approaches-to-feature-selection-in-data-mining/22121110)

- 15. [Hybrid genetic algorithms for feature selection - JBNU Researchers Portal - Pure](https://pure.jbnu.ac.kr/en/publications/hybrid-genetic-algorithms-for-feature-selection/)

- 16. [Finding R&D Trends and Experts Made Simple / Scinapse](https://www.scinapse.io/papers/3004565805)

- 17. [(PDF) A survey on swarm intelligence approaches to feature selection in data mining](https://www.researchgate.net/publication/339087761_A_survey_on_swarm_intelligence_approaches_to_feature_selection_in_data_mining)

- 18. [(PDF) Hybrid genetic algorithms for feature selection (2004) / Il-Seok Oh / 973 Citations](https://scispace.com/papers/hybrid-genetic-algorithms-for-feature-selection-421b9nybwa)

- 19. [A survey on swarm intelligence approaches to feature selection in data mining - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650219303104)

- 20. [A survey on swarm intelligence approaches to feature selection in data mining - researchr publication](https://researchr.org/publication/NguyenXZ20)

- 21. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for la…](https://ouci.dntb.gov.ua/en/works/4bVRZkB4/)

- 22. [A multi-objective evolutionary algorithm with interval based…](https://lacuna.tiptreesystems.com/work/a-multi-objective-evolutionary-algorithm-with-interval-based)

- 23. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - 科研通](https://www.ablesci.com/scholar/paper)

- 24. [Local search-embedded genetic algorithms for feature selection - JBNU Researchers Portal - Pure](https://pure.jbnu.ac.kr/en/publications/local-search-embedded-genetic-algorithms-for-feature-selection/)

- 25. [Bach Hoai Nguyen](https://www.csauthors.net/bach-hoai-nguyen/)

- 26. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - 科研通](https://www.ablesci.com/assist/detail)

- 27. [Full article: A conditional opposition-based particle swarm optimisation for feature selection](https://www.tandfonline.com/doi/full/10.1080/09540091.2021.2002266)

- 28. [Bach Hoai Nguyen - researchr alias](https://researchr.org/alias/bach-hoai-nguyen)

- 29. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - Fingerprint - EdUHK Research Repository](https://repository.eduhk.hk/en/publications/a-multi-objective-evolutionary-algorithm-with-interval-based-init/fingerprints/)

- 30. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification (2022) / Yu Xue / 80 Citations](https://scispace.com/papers/a-multi-objective-evolutionary-algorithm-with-interval-based-3fcoo7mc)

- 31. [Local search-embedded genetic algorithms for feature selection](https://www.researchgate.net/publication/3974313_Local_search-embedded_genetic_algorithms_for_feature_selection)

- 32. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - Fingerprint - EdUHK Research Repository](https://repository.eduhk.hk/en/publications/a-multi-objective-evolutionary-algorithm-with-interval-based-init/fingerprints/)

- 33. [A Review of the Evolution of Multi-Objective Evolutionary Algorithms - ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S1546221825009889)

- 34. [(PDF) A Guided Hybrid Genetic Algorithm for Feature Selection with Expensive Cost Functions](https://www.researchgate.net/publication/239523665_A_Guided_Hybrid_Genetic_Algorithm_for_Feature_Selection_with_Expensive_Cost_Functions)

- 35. [International Journal of Electrical and Computer Engineering (IJECE)](https://ijece.iaescore.com/index.php/IJECE/article/download/26800/15839)

- 36. ech

- 37. [Top 160 IEEE Transactions on Pattern Analysis and Machine Intelligence papers published in 2004](https://scispace.com/journals/ieee-transactions-on-pattern-analysis-and-machine-3qetrrfv/2004)

- 38. [Local search (optimization) / 17118 Publications / 89146 Citations / Top Authors / Related Topics](https://scispace.com/topics/local-search-optimization-2aqlqiz8)

- 39. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426028964)

- 40. [Developing Improved Algorithms for Detection and Analysis of Skin Cancer](https://opus.lib.uts.edu.au/bitstream/10453/52931/2/02whole.pdf)

- 41. [Fundação Getulio Vargas](https://repositorio.fgv.br/bitstreams/634f4c46-b2b2-422e-a7de-070855e0e575/download)

- 42. [2. Related works](https://www.aimspress.com/aimspress-data/mbe/2021/4/PDF/mbe-18-04-192.pdf)

- 43. [Subject based feature selection for hybrid brain computer interface using genetic algorithm and support vector machine - ScienceDirect](https://doi.org/10.1016/j.rineng.2025.105649)

- 44. [Evolution algorithm with adaptive genetic operator and dynamic scoring mechanism for large-scale sparse many-objective optimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC11920420/)

### Batch 13: returned titles

- 1. [Improved NSGA-II algorithms for multi-objective biomarker discovery / Bioinformatics / Oxford Academic](https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii20/6702001)

- 2. [dblp: Improved NSGA-II algorithms for multi-objective biomarker discovery.](https://dblp.uni-trier.de/rec/journals/bioinformatics/CattelaniF22.html)

- 3. [Improved NSGA-II algorithms for multi-objective biomarker discovery.](https://pubmed.ncbi.nlm.nih.gov/36124794/)

- 4. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10536003)

- 5. [Bioinformatics, 38, 2022, ii20–ii26](https://watermark02.silverchair.com/btac463.pdf)

- 6. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks.](https://pubmed.ncbi.nlm.nih.gov/32217494/)

- 7. [Solving Large-Scale Multi-Objective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks](https://eu-st01.ext.exlibrisgroup.com/44SUR_INST/upload/1781026397387/FINAL%20VERSION.pdf)

- 8. [Improved NSGA-II algorithms for m... preview & related info / Mendeley](https://www.mendeley.com/catalogue/4bb22f22-8739-3cb0-a295-201fa993338c/)

- 9. [Luca Cattelani - UEFConnect](https://uefconnect.uef.fi/en/luca.cattelani/)

- 10. [Solving Large-Scale Multi-Objective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks](https://eu-st01.ext.exlibrisgroup.com/44SUR_INST/upload/1775637151205/FINAL%20VERSION.pdf)

- 11. [Dual-stage optimizer for systematic overestimation adjustment applied to multi-objective genetic algorithms for biomarker selection](https://pmc.ncbi.nlm.nih.gov/articles/PMC11684899/)

- 12. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/380771896_Probe_Population-Based_Initialization_and_Genetic_Pool-Based_Reproduction_for_Evolutionary_Bi-Objective_Feature_Selection)

- 13. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks - CityUHK Scholars](https://scholars.cityu.edu.hk/en/publications/solving-large-scale-multiobjective-optimization-problems-with-spa/)

- 14. [Dual-stage optimizer for systematic overestimation adjustment applied to multi-objective genetic algorithms for biomarker selection.](https://pubmed.ncbi.nlm.nih.gov/39737563/)

- 15. [Slide: Improved NSGA-II algorithms for multi-objective biomarker discovery has been published by F1000Research.](https://f1000research.com/slides/11-1330)

- 16. [/ 21st European Conference on Computational Biology ECCB2022 Planetary Health and Biodiversity BOOK OF ABSTRACTS / --- / --- / --- / 21st European Conference on Computational Biology ECCB2022 Planetary Health and Biodiversity 12-21 September 2022 Sitges, Barcelona /eccb2022.org](https://eccb.org/2022/wp-content/uploads/2022/11/ECCB2022_Book-of-abstracts_oral-talks_v4_16092022_web_compressed.pdf)

- 17. [Volume 38 Issue Supplement_2 / Bioinformatics / Oxford Academic](https://academic.oup.com/bioinformatics/issue/38/Supplement_2)

- 18. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/380771896_Probe_Population_Based_Initialization_and_Genetic_Pool_Based_Reproduction_for_Evolutionary_Bi-Objective_Feature_Selection)

- 19. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selecti…](https://ouci.dntb.gov.ua/en/works/lDprMbLl/)

- 20. [Vittorio Fortino - UEFConnect](https://uefconnect.uef.fi/vittorio.fortino/)

- 21. [Improved NSGA-II algorithms for multi-objective biomarker discovery](https://openalex.org/W4296778072)

- 22. [Improved NSGA-II algorithms for multi-objective biomarker discovery-MedSci.cn](https://www.medsci.cn/sci/show_paper.asp)

- 23. [An Adaptive Multi-Granular Pareto-Optimal Subspace Learning Algorithm for Sparse Large-Scale Multi-Objective Optimization](https://register.eurekamag.com/research/095/881/095881243.php)

- 24. [Solving Large-Scale Multi-Objective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Solving-Large-Scale-Multi-Objective-Optimization-Problems-with/99513286502346)

- 25. [Solving Large-Scale Multiobjective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks](https://extensions.eurekamag.com/research/069/954/069954943.php)

- 26. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 29, Issue 5, October 2025](https://ieee-cis.blogspot.com/2025/10/ieee-transactions-on-evolutionary.html)

- 27. [Improving biomarker selection for cancer subtype classiﬁcation](https://d197for5662m48.cloudfront.net/documents/publicationstatus/172756/preprint_pdf/6be827d162bc4da94176f51693b4de4b.pdf)

- 28. [TEC2025](https://hongsong-wang.github.io/TEC2025/)

- 29. [IEEE Computational Intelligence Society: October 2025](https://ieee-cis.blogspot.com/2025/10/)

- 30. [スパース大規模多目的最適化のための適応多粒度パレート最適部分空間学習アルゴリズム〖JST機械翻訳〗 / 文献情報 / J-GLOBAL 科学技術総合リンクセンター](https://jglobal.jst.go.jp/detail)

- 31. [An Adaptive Multi-Granular Pareto-Optimal Subspace Learning Algorithm for Sparse Large-Scale Multi-Objective Optimization - researchr publication authors](https://researchr.org/publication/SunTSY025/authors)

- 32. [An Adaptive Initialization and Reproduction-Based Evolutionary Algorithm for Tackling Bi-Objective Feature Selection in Classification](https://doi.org/10.3390/sym17050671)

- 33. [An Adaptive Multi-Granular Pareto-Optimal Subspace Learning Algorithm for Sparse Large-Scale Multi-Objective Optimization - researchr publication](https://researchr.org/publication/SunTSY025)

- 34. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426028964)

- 35. [dblp: Chengze Sun](https://dblp.org/pid/360/4214.html)

- 36. [(PDF) Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks](https://www.researchgate.net/publication/339782398_Solving_Large-Scale_Multiobjective_Optimization_Problems_With_Sparse_Optimal_Solutions_via_Unsupervised_Neural_Networks)

- 37. [An Adaptive Initialization and Reproduction-Based Evolutionary Algorithm for Tackling Bi-Objective Feature Selection in Classification](https://www.mdpi.com/2073-8994/17/5/671)

- 38. [An Adaptive Multi-Granular Pareto-Optimal Subspace Learning Algorithm for Sparse Large-Scale Multi-Objective Optimization / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 39. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection - researchr publication](https://researchr.org/publication/XuXZ25-4)

- 40. [Elastic net–guided NSGA-II for scalable multi-objective feature selection in high-dimensional data analytics](https://ouci.dntb.gov.ua/works/4bPQWa0e/)

- 41. [IEEE Computational Intelligence Society: TEVC](https://ieee-cis.blogspot.com/search/label/TEVC)

- 42. [Under review as a conference paper at ICLR 2026](https://openreview.net/pdf)

### Batch 14: returned titles

- 1. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/39401114)

- 2. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks.](https://pubmed.ncbi.nlm.nih.gov/32217494/)

- 3. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery.](https://pubmed.ncbi.nlm.nih.gov/39401114/)

- 4. [A comprehensive evaluation framework for benchmarking multi-objective feature selection in omics-based biomarker discovery / Publications - UEF CRIS](https://uef.cris.fi/en/publications/2fdee8ce-da4c-450a-ad67-edf1e462536b)

- 5. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10716353)

- 6. [Solving Large-Scale Multi-Objective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Solving-Large-Scale-Multi-Objective-Optimization-Problems-with/99513286502346)

- 7. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks - CityUHK Scholars](https://scholars.cityu.edu.hk/en/publications/solving-large-scale-multiobjective-optimization-problems-with-spa/)

- 8. [Theory of the Hypervolume Indicator: Optimal](https://www.sop.tik.ee.ethz.ch/publicationListFiles/abbz2009a.pdf)

- 9. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks](https://openalex.org/W3012911890)

- 10. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery](https://openalex.org/W4403390230)

- 11. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304397511002428)

- 12. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks / CiNii Research](https://cir.nii.ac.jp/crid/1360579818129286144)

- 13. [Publications](https://bin.re/publications/)

- 14. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10536003)

- 15. [(PDF) A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery](https://www.researchgate.net/publication/384907267_A_comprehensive_evaluation_framework_for_benchmarking_multi-objective_feature_selection_in_omics-based_biomarker_discovery)

- 16. [Solving Large-Scale Multiobjective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks](https://extensions.eurekamag.com/research/069/954/069954943.php)

- 17. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selecti…](https://ouci.dntb.gov.ua/en/works/lDprMbLl/)

- 18. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/380771896_Probe_Population-Based_Initialization_and_Genetic_Pool-Based_Reproduction_for_Evolutionary_Bi-Objective_Feature_Selection)

- 19. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/380771896_Probe_Population_Based_Initialization_and_Genetic_Pool_Based_Reproduction_for_Evolutionary_Bi-Objective_Feature_Selection)

- 20. [Theory of the hypervolume indicator](https://ouci.dntb.gov.ua/en/works/73ZvLz09/)

- 21. [Bibliography – Hypervolume](https://hypervolume.org/bibliography.html)

- 22. [ETH - SOP - Publications](https://sop.tik.ee.ethz.ch/publications/indicators.html)

- 23. [ETH - SOP - Publications](https://www.sop.tik.ee.ethz.ch/publications/performanceAss.html)

- 24. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection: AI Summary, Post-Publication Reviews & Author Contact - Peeref](https://www.peeref.com/works/87505703)

- 25. [Dimo Brockhoff - Inria Saclay - Ile-de-France](https://researchers.lille.inria.fr/~brockhof/publications.php)

- 26. [[inria-00430540, v1] Theory of the Hypervolume Indicator: Optimal ?-Distributions and the Choice of the Reference Point](https://www.cmap.polytechnique.fr/~dimo.brockhoff/publicationListFiles/abbz2009a.pdf)

- 27. [Solving Large-Scale Sparse Multi-Objective Optimization Problems by Automated Decision Variable Clustering](https://ouci.dntb.gov.ua/en/works/4EeAkAz4/)

- 28. [Professional Report](https://www.isgec.org/gecco-2009/docs/gecco09-conference-program-final-plus2.pdf)

- 29. [Large‐Scale Multi‐Objective Optimization Algorithms: A Decade Survey - Wang - 2025 - Expert Systems - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/exsy.70157)

- 30. [ETH - SOP - Publications](https://sop.tik.ee.ethz.ch/publications/index.html)

- 31. [Large‐Scale Multi‐Objective Dual‐Population Co‐Evolutionary Algorithm Based on Decision Variable Boundary Penalty - Zhou - 2025 - Concurrency and Computation: Practice and Experience - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70443)

- 32. [Publications](https://www.cmap.polytechnique.fr/~anne.auger/publications.html)

- 33. [ETH - SOP - Dimo Brockhoff](https://www.sop.tik.ee.ethz.ch/people/brockho/publications.html)

- 34. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 29, Issue 5, October 2025](https://ieee-cis.blogspot.com/2025/10/ieee-transactions-on-evolutionary.html)

- 35. [Investigating and exploiting the bias of the weighted hypervolume to articulate user preferences - Institut Polytechnique de Paris](https://researchportal.ip-paris.fr/en/publications/investigating-and-exploiting-the-bias-of-the-weighted-hypervolume/)

- 36. [Theory of the Hypervolume Indicator: Optimal μ-Distributions and the Choice of the Reference Point / Request PDF](https://www.researchgate.net/publication/216457231_Theory_of_the_Hypervolume_Indicator_Optimal_m-Distributions_and_the_Choice_of_the_Reference_Point)

- 37. [Under review as a conference paper at ICLR 2026](https://openreview.net/pdf)

- 38. [Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks - Projects - CityUHK Scholars](https://scholars.cityu.edu.hk/en/publications/solving-large-scale-multiobjective-optimization-problems-with-spa/projects/)

- 39. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery - researchr publication](https://researchr.org/publication/CattelaniGRF24)

- 40. [Multiobjective Differential Evolution for Higher-Dimensional Multimodal Multiobjective Optimization](https://jas.ia.ac.cn/article/doi/10.1109/JAS.2024.124377)

- 41. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection - researchr publication](https://researchr.org/publication/XuXZ25-4)

- 42. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery / JoVE Visualize](https://visualize.jove.com/39401114-a-comprehensive-evaluation-framework-for-benchmarking-multi-objective-feature-selection-in-omics-based-biomarker-discovery)

- 43. [dblp: IEEE/ACM Transactions on Computational Biology and Bioinformatics, Volume 21](https://dblp.org/db/journals/tcbb/tcbb21)

- 44. [Evolutionary Multitasking With Multiple Knowledge Representations and Elite Vector Guidance for Solving Large-Scale Multi-Objective Optimization Problems](https://www.ieee-jas.net/en/article/doi/10.1109/JAS.2025.125483)

- 45. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery - 科研通](https://www.ablesci.com/assist/detail)

- 46. [A multi-granularity clustering based evolutionary algorithm for large-scale sparse multi-objective optimization](https://ouci.dntb.gov.ua/en/works/4kwJ2dN4/)

- 47. [Auger, A., Bader, J., Brockhoff, D., Zitzler, E., 2009. Theory of the hypervolume indicator: optimal distributions and the choice of the reference point. In Foundations of Genetic Algorithms (FOGA 2009) 87-102. ACM, New York, NY, USA.](https://sites.miamioh.edu/byran-smucker/files/2022/02/pub_2015_Cao_etal.pdf)

- 48. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery - 科研通](https://www.ablesci.com/assist/detail)

- 49. [IEEE Computational Intelligence Society: October 2025](https://ieee-cis.blogspot.com/2025/10/)

- 50. [Luca Cattelani](https://www.csauthors.net/luca-cattelani/)

- 51. [Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection - researchr publication references](https://researchr.org/publication/XuXZ25-4/references)

- 52. [Probe Population Based Initialization and Genetic Pool Based Reproduction for Evolutionary Bi-Objective Feature Selection - 科研通](https://www.ablesci.com/assist/detail)

- 53. [IEEE Computational Intelligence Society: TEVC](https://ieee-cis.blogspot.com/search/label/TEVC)

- 54. [Hypervolume indicator](https://en.wikipedia.org/wiki/Hypervolume_indicator)

- 55. [The Hypervolume Indicator: Problems and Algorithms](https://arxiv.org/abs/2005.00515)

### Batch 15: returned titles

- 1. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/document/9133433/)

- 2. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304397511002428)

- 3. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - researchr publication bibtex](https://researchr.org/publication/Al-TashiARMA20/bibtex)

- 4. [Bibliography – Hypervolume](https://hypervolume.org/bibliography.html)

- 5. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications - Institut Polytechnique de Paris](https://researchportal.ip-paris.fr/en/publications/hypervolume-based-multiobjective-optimization-theoretical-foundat/)

- 6. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - Torrens University Australia](https://research.torrens.edu.au/en/publications/approaches-to-multi-objective-feature-selection-a-systematic-lite/)

- 7. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - UTP Scholars](https://khub.utp.edu.my/scholars/13804/)

- 8. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - UT MD Anderson Cancer Center](https://mdanderson.elsevierpure.com/en/publications/approaches-to-multi-objective-feature-selection-a-systematic-lite/)

- 9. [Microsoft Word - EMO 2015 IGD Camera Ready](https://ci-labo-omu.github.io/assets/paper/pdf_file/multiobjective/EMO_2015_IGD_Camera-Ready.pdf)

- 10. [(PDF) Approaches to Multi-Objective Feature Selection: A Systematic Literature Review](https://www.researchgate.net/publication/342726662_Approaches_to_Multi-Objective_Feature_Selection_A_Systematic_Literature_Review)

- 11. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical… (2011) – Theoretical Computer Science / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W2144982506)

- 12. [Approaches to Multi-Objective Feature Selection: A...](https://www.canyam.com/en/article/approaches-to-multi-objective-feature-selection-a-systematic-literature-review/21033056)

- 13. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications / CiNii Research](https://cir.nii.ac.jp/crid/1360588384425624704)

- 14. [[inria-00638989, v1] Hypervolume-based Multiobjective Optimization: Theoretical Foundations and Practical Implications](https://www.cmap.polytechnique.fr/~dimo.brockhoff/publicationListFiles/abbz2012a.pdf)

- 15. [Publications](https://bin.re/publications/)

- 16. [Segmented initialization and offspring modification in evolutionary algorithms for bi-objective feature selection / Request PDF](https://www.researchgate.net/publication/342537209_Segmented_initialization_and_offspring_modification_in_evolutionary_algorithms_for_bi-objective_feature_selection)

- 17. [Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 18. [Publications 2020 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2020)

- 19. [Surrogate-assisted hyper-parameter search for portfolio optimisation: multi-period considerations / Neural Computing and Applications / Springer Nature Link](https://link.springer.com/article/10.1007/s00521-023-09176-7)

- 20. [MVMOO: Mixed variable multi-objective optimisation / Journal of Global Optimization / Springer Nature Link](https://doi.org/10.1007/s10898-021-01052-9)

- 21. [Hypervolume-based Multiobjective Optimization: Theoretical Foundations and Practical Implications / Request PDF](https://www.researchgate.net/publication/222889399_Hypervolume-based_Multiobjective_Optimization_Theoretical_Foundations_and_Practical_Implications)

- 22. [Bibliography - DispatchAtlas](https://dispatchatlas.ahmedgad.com/catalogue/bibliography/)

- 23. [dblp: Theoretical Computer Science, Volume 425](https://dblp.org/db/journals/tcs/tcs425.html)

- 24. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - researchr publication bibliographies](https://researchr.org/publication/Al-TashiARMA20/bibliographies)

- 25. [dblp: Theoretical Computer Science, Volume 425](https://dblp.dagstuhl.de/db/journals/tcs/tcs425.html)

- 26. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - researchr publication](https://researchr.org/publication/Al-TashiARMA20)

- 27. [A Survey on the Hypervolume Indicator in Evolutionary Multiobjective Optimization (2020) – IEEE Transactions on Evolutionary Computation / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W3046910774)

- 28. [MOFS-REPLS: A large-scale multi-objective feature selection algorithm based on real-valued encoding and preference lead…](https://ouci.dntb.gov.ua/en/works/ldGEpyY4/)

- 29. [Feature Selection Problem and Metaheuristics: A Systematic Literature Review about Its Formulation, Evaluation and Applications - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10813816/)

- 30. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - researchr publication reviews](https://researchr.org/publication/Al-TashiARMA20/reviews)

- 31. [Population diversity control based differential evolution algorithm using fuzzy system for noisy multi-objective optimization problems - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11294573/)

- 32. [Segmented initialization and offspring modification in evolutionary algorithms for bi-objective feature selection (2020) / Hang Xu / 27 Citations](https://scispace.com/papers/segmented-initialization-and-offspring-modification-in-5gg7o6bdo0)

- 33. [Sustainable Water Optimization Tool (SUWO): An Optimization Framework for the Water–Energy–Food–Ecosystem Nexus](https://www.mdpi.com/2073-4441/17/9/1280)

- 34. [A Parallel Multi-objective Memetic Algorithm Based on the IGD+ Indicator / Request PDF](https://www.researchgate.net/publication/307507585_A_Parallel_Multi-objective_Memetic_Algorithm_Based_on_the_IGD_Indicator)

- 35. [HypE: An Algorithm for Fast Hypervolume-Based Many-Objective Optimization](https://explore.metascienceobservatory.org/papers/W2108968575)

### Batch 16: returned titles

- 1. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/document/9133433/)

- 2. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance / CiNii Research](https://cir.nii.ac.jp/crid/1360013336413033088)

- 3. [Microsoft Word - EMO 2015 IGD Camera Ready](https://ci-labo-omu.github.io/assets/paper/pdf_file/multiobjective/EMO_2015_IGD_Camera-Ready.pdf)

- 4. [Approaches to Multi-Objective Feature Selection: A Systematic](https://research-repository.griffith.edu.au/server/api/core/bitstreams/dd781204-fc6d-40a1-8d12-09bd4ad05357/content)

- 5. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance](https://www.researchgate.net/publication/287406344_Modified_Distance_Calculation_in_Generational_Distance_and_Inverted_Generational_Distance)

- 6. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - Torrens University Australia](https://research.torrens.edu.au/en/publications/approaches-to-multi-objective-feature-selection-a-systematic-lite/)

- 7. [Modified distance calculation in generational distance and inverted generational distance](https://eurekamag.com/research/111/292/111292623.php)

- 8. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance (2015) – Lecture notes in computer science / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W224959492)

- 9. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - UT MD Anderson Cancer Center](https://mdanderson.elsevierpure.com/en/publications/approaches-to-multi-objective-feature-selection-a-systematic-lite/)

- 10. [Approaches to Multi-Objective Feature Selection: A Systematic Literature Review - researchr publication bibtex](https://researchr.org/publication/Al-TashiARMA20/bibtex)

- 11. [(PDF) Approaches to Multi-Objective Feature Selection: A Systematic Literature Review](https://www.researchgate.net/publication/342726662_Approaches_to_Multi-Objective_Feature_Selection_A_Systematic_Literature_Review)

- 12. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance - 百度学术](https://xueshu.baidu.com/usercenter/paper/show)

- 13. [A Study on Performance Evaluation Ability of a Modified Inverted Generational Distance… (2015) / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W2103176750)

- 14. [Segmented initialization and offspring modification in evolutionary algorithms for bi-objective feature selection (2020) / Hang Xu / 27 Citations](https://scispace.com/papers/segmented-initialization-and-offspring-modification-in-5gg7o6bdo0)

- 15. [Publications 2020 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2020)

- 16. [Segmented initialization and offspring modification in evolutionary algorithms for bi-objective feature selection / Request PDF](https://www.researchgate.net/publication/342537209_Segmented_initialization_and_offspring_modification_in_evolutionary_algorithms_for_bi-objective_feature_selection)

- 17. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance](https://bibbase.org/network/publication/ishibuchi-masuda-tanigaki-nojima-modifieddistancecalculationingenerationaldistanceandinvertedgenerationaldistance-2015)

- 18. [Evolution algorithm with adaptive genetic operator and dynamic scoring mechanism for large-scale sparse many-objective optimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC11920420/)

- 19. [Albaydha University جامعة البيضاء - الجمهورية اليمنية](https://baydaauniv.net/teacherdetails.php)

- 20. [(Open Access) Modified distance calculation in generational distance and inverted generational distance (2015) / Hisao Ishibuchi / 287 Citations](https://scispace.com/papers/modified-distance-calculation-in-generational-distance-and-4huylt1heo)

- 21. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance - researchr publication related](https://researchr.org/publication/IshibuchiMTN15/related)

- 22. [Modified distance calculation in generational distance and inverted generational distance - 科研通](https://www.ablesci.com/assist/detail)

- 23. [Approaches to Multi-Objective Feature Selection: A...](https://www.canyam.com/en/article/approaches-to-multi-objective-feature-selection-a-systematic-literature-review/21033056)

- 24. [Modified Distance Calculation in Generational Distance and Inverted Generational Distance (2015) / Hisao Ishibuchi / 422 Citations](https://scispace.com/papers/modified-distance-calculation-in-generational-distance-and-4qdo7qo5gu)

- 25. [Bibliography](https://www.ci.ovgu.de/is_media/PhDThesis/Javadi_Mahrokh_Dissertation_2023.pdf)

- 26. [Machine Learning Models for the Identification of Prognostic and Predictive Cancer Biomarkers: A Systematic Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/10178491/)

- 27. [DAFTAR PUSTAKA](https://repository.unjaya.ac.id/3801/8/Daftar%20Pustaka_202102007_Fathur%20Fakhriza_Informatika.pdf)

- 28. [A Comprehensive Survey of Feature Selection Techniques based](https://assets-eu.researchsquare.com/files/rs-2388306/v1/6c75bac7-3f16-4ba1-819b-4a91caaf5b46.pdf)

- 29. [(PDF) Approaches to Multi-Objective Feature Selection: A Systematic Literature Review (2020) / Qasem Al-Tashi / 143 Citations](https://scispace.com/papers/approaches-to-multi-objective-feature-selection-a-systematic-4kqno0g5ya)

- 30. [Feature selection techniques for machine learning: a survey of more than two decades of research](https://ouci.dntb.gov.ua/en/works/4Yw13D09/)

- 31. [An Adaptive Initialization and Reproduction-Based Evolutionary Algorithm for Tackling Bi-Objective Feature Selection in…](https://ouci.dntb.gov.ua/works/7PMMYnQO/)

- 32. [An Interpolation-Based Evolutionary Algorithm for Bi-Objective Feature Selection in Classification](https://ouci.dntb.gov.ua/en/works/ldOeZJq4/)

- 33. [Top 408 papers presented at Genetic and Evolutionary Computation Conference in 2020](https://scispace.com/conferences/genetic-and-evolutionary-computation-conference-1juywlit/2020)

- 34. [Paula Cruz's Profile / Wiley Online Library, MDPI, Lexology Journalist / Muck Rack](https://muckrack.com/paula-cruz)

- 35. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for la…](https://ouci.dntb.gov.ua/en/works/4bVRZkB4/)

- 36. [PSO-based feature selection techniques—challenges and methodologies: a review](https://ouci.dntb.gov.ua/en/works/4yNDorEr/)

- 37. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/index.shtml)

- 38. [An effective initialization for Fuzzy PSO with Greedy Forward Selection in feature selection](https://ouci.dntb.gov.ua/en/works/96GNjg8x/)

### Batch 17: returned titles

- 1. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650221001875)

- 2. [Kalyanmoy Deb / ScienceDirect](https://www.sciencedirect.com/author/7006019904/kalyanmoy-deb)

- 3. [A. Pouyan Nejadhashemi / ScienceDirect](https://www.sciencedirect.com/author/6504453135/a-pouyan-nejadhashemi)

- 4. [A sparse large-scale multi-objective evolutionary algorithm based on sparsity detection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650224003584)

- 5. [Evaluation of the impacts of hydrologic model calibration methods on predictability of ecologically-relevant hydrologic indices - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022169418305705)

- 6. [Improving two-layer encoding of evolutionary algorithms for sparse large-scale multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-024-01489-x)

- 7. [An Jaccard similarity coefficient-based evolutionary algorithm for sparse large-scale multi-objective optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650225004262)

- 8. [Designing problem-specific operators for solving the Cell Switch-Off problem in ultra-dense 5G networks with hybrid MOEAs - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650223000639)

- 9. [Environmental and Economic Optimization of Multi-Source Power Real-Time Dispatch Based on DGADE-HDJ - ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S0199859525000648)

- 10. [Dynamic multi-knowledge evolutionary algorithm for sparse large-scale multi-objective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0950705125018027)

- 11. [Agricultural Innovization: An Optimization-Driven solution for sustainable agricultural intensification in Michigan - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0168169922004604)

- 12. [Combining sparse evolutionary operators and deep reinforcement learning for large-scale sparse multiobjective optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494626006150)

### Batch 18: returned titles

- 1. [Lixin Cui - IEEE Xplore Author Profile](https://xplorestaging.ieee.org/author/37086015153)

- 2. [Validation-based Decision Making in Data-driven Evolutionary Computation: A Case Study in Multi-objective Feature Selection / Request PDF](https://www.researchgate.net/publication/392111313_Validation-based_Decision_Making_in_Data-driven_Evolutionary_Computation_A_Case_Study_in_Multi-objective_Feature_Selection)

- 3. [MOFS-REPLS: A large-scale multi-objective feature selection algorithm based on real-valued encoding and preference lead…](https://ouci.dntb.gov.ua/en/works/ldGEpyY4/)

- 4. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 5. [Tensor-based unsupervised feature selection for error-robust handling of unbalanced incomplete multi-view data](https://ouci.dntb.gov.ua/en/works/4KQRn5N9/)

- 6. [Search Results / Scholarly Articles, Journals, and E-Books / EBSCOhost](https://openurl.ebsco.com/results)

- 7. [dblp: International Journal of Machine Learning and Cybernetics, Volume 17](https://dblp.dagstuhl.de/db/journals/mlc/mlc17.html)

- 8. [Katalog Plus der Bibliothek der Frankfurt UAS: Artikel & mehr...](https://hds.hebis.de/fuas/EBSCO/Search)

- 9. [Untitled](https://www.ieee-ssci.org/assets/files/S2.pdf)

- 10. [Ensemblebasierte automatisierte Kalibriermodellerstellung für komplexe Sensorsysteme am Beispiel zerstörungsfreier mikromagnetischer Materialcharakterisierungsverfahren - MASCHINENBAU - Uni Kassel](https://www.uni-kassel.de/maschinenbau/institute/analyse-und-regelung-technischer-systeme/institute/analyse-und-regelung-technischer-systeme/mess-und-regelungstechnik/forschung/regelungstechnik/abgeschlossene-projekte-regelungstechnik/ensemblebasierte-automatisierte-kalibriermodellerstellung-fuer-komplexe-sensorsysteme-am-beispiel-zerstoerungsfreier-mikromagnetischer-materialcharakterisierungsverfahren.html)

- 11. [dblp: Masoud Makrehchi](https://dblp.org/pid/10/5941.html)

- 12. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction / Request PDF](https://www.researchgate.net/publication/393238855_An_evolutionary_multitasking_algorithm_for_multi-objective_feature_selection_using_dual-perspective_reduction)

- 13. [A comparative study on population-based multi-objective feature selection / International Journal of Machine Learning and Cybernetics / DeepDyve](https://www.deepdyve.com/lp/springer-journals/a-comparative-study-on-population-based-multi-objective-feature-2D5G9hlnIY)

- 14. [Compact Optimization Algorithms with Re-Sampled Inheritance](https://ouci.dntb.gov.ua/en/works/lo5zMye7/)

- 15. [2025 IEEE Symposium on](https://www.proceedings.com/content/080/080469webtoc.pdf)

- 16. [A comparative study on population-based multi-objective feature selection - 科研通](https://www.ablesci.com/assist/detail)

- 17. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S095219762500764X)

- 18. [Towards large-scale multi-objective feature selection: A two-stage evolutionary algorithm guided by dual feature weightings / Request PDF](https://www.researchgate.net/publication/401389096_Towards_large-scale_multi-objective_feature_selection_A_two-stage_evolutionary_algorithm_guided_by_dual_feature_weightings)

- 19. [Shahryar RAHNAMAYAN / Ontario Tech University, Oshawa / UOIT / Faculty of Engineering and Applied Science / Research profile](https://www.researchgate.net/profile/Shahryar-Rahnamayan)

- 20. [(PDF) A multi-stage knowledge-guided evolutionary algorithm for large-scale sparse multi-objective optimization problems](https://www.researchgate.net/publication/361317626_A_multi-stage_knowledge-guided_evolutionary_algorithm_for_large-scale_sparse_multi-objective_optimization_problems)

- 21. [Enhancing Diversity in Multi-Objective Feature Selection / Request PDF](https://www.researchgate.net/publication/382989404_Enhancing_Diversity_in_Multi-Objective_Feature_Selection)

- 22. [Evolutionary multi-feature construction for data reduction: a case study](https://settings.eurekamag.com/research/083/816/083816087.php)

- 23. [Beyond the Pareto Front: Utilizing the Entire Population for Decision-Making in Evolutionary Machine Learning / MDPI](https://www.mdpi.com/2227-7390/13/16/2579)

- 24. [259354 PDFs / Review articles in EVOLUTIONARY COMPUTATION](https://www.researchgate.net/topic/Evolutionary-Computation/publications/96)

- 25. [Optimal Data Splitting in Distributed Optimization for Machine Learning / Request PDF](https://www.researchgate.net/publication/379281125_Optimal_Data_Splitting_in_Distributed_Optimization_for_Machine_Learning)

- 26. [Compact NSGA-II for Multi-objective Feature Selection / Request PDF](https://www.researchgate.net/publication/377786702_Compact_NSGA-II_for_Multi-objective_Feature_Selection)

- 27. [EMOPG+FS: Evolutionary multi-objective prototype generation and feature selection](https://eurekamag.com/research/064/836/064836719.php)

- 28. [(PDF) Opposition-Based Multi-objective Binary Differential Evolution for Multi-label Feature Selection: 10th International Conference, EMO 2019, East Lansing, MI, USA, March 10-13, 2019, Proceedings](https://www.researchgate.net/publication/330835612_Opposition-Based_Multi-objective_Binary_Differential_Evolution_for_Multi-label_Feature_Selection_10th_International_Conference_EMO_2019_East_Lansing_MI_USA_March_10-13_2019_Proceedings)

- 29. [Publications / COLA-Lab@Exeter](https://colalab.ai/docs/research/publications/)

- 30. [Beyond the Pareto Front: Utilizing the Entire Population for Decision-Making in Evolutionary Machine Learning](https://doi.org/10.3390/math13162579)

- 31. [The principal role in data-driven decision making: using case-study data to develop multi-mediator models of educational reform](https://eurekamag.com/research/088/870/088870863.php)

- 32. [A Survey on Evolutionary Computation Approaches to Feature Selection](https://eurekamag.com/research/102/517/102517301.php)

- 33. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S095219762500764X)

- 34. [A Decomposition-Based Multi-Objective Flying Foxes Optimization Algorithm and Its Applications](https://www.mdpi.com/2313-7673/9/7/417/pdf)

- 35. [Open Math. 2017; 15: 261–280](https://ddd.uab.cat/pub/artpub/2017/a9384fbdf269/OM17.pdf)

- 36. [Threshold Adaptation for Improved Wrapper-Based Evolutionary Feature Selection](https://www.iztok-jr-fister.eu/static/publications/353.pdf)

- 37. [ISSN: 2229-6948(ONLINE)                                              ICTACT JOURNAL ON COMMUNICATION TECHNOLOGY, SEPTEMBER 2021, VOLUME: 12, ISSUE: 03](https://ictactjournals.in/paper/IJCT_Vol_12_Iss_3_Paper_10_2527_2537.pdf)

- 38. [Lu BAI / Professor (Full) / PhD / Beijing Normal University, Beijing / bnu / Research profile](https://www.researchgate.net/profile/Lu-Bai-33)

### Batch 19: returned titles

- 1. [dblp: Masoud Makrehchi](https://dblp.org/pid/10/5941.html)

- 2. [Ensemblebasierte automatisierte Kalibriermodellerstellung für komplexe Sensorsysteme am Beispiel zerstörungsfreier mikromagnetischer Materialcharakterisierungsverfahren - MASCHINENBAU - Uni Kassel](https://www.uni-kassel.de/maschinenbau/institute/analyse-und-regelung-technischer-systeme/institute/analyse-und-regelung-technischer-systeme/mess-und-regelungstechnik/forschung/regelungstechnik/abgeschlossene-projekte-regelungstechnik/ensemblebasierte-automatisierte-kalibriermodellerstellung-fuer-komplexe-sensorsysteme-am-beispiel-zerstoerungsfreier-mikromagnetischer-materialcharakterisierungsverfahren.html)

- 3. [Enhanced SparseEA for large-scale multi-objective feature selection problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-023-01177-2)

- 4. [A comparative study of many-objective optimizers on large-scale many-objective software clustering problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-021-00270-8)

- 5. [dblp: Shahryar Rahnamayan](https://dblp.org/pid/37/5203.html)

- 6. [dblp: Xiaojun Zhou 0001](https://dblp.org/pid/71/5561-1.html)

- 7. [dblp: Journal of King Saud University - Computer and Information Sciences, Volume 36](https://dblp.org/db/journals/jksucis/jksucis36.html)

- 8. [dblp: Juan Julián Merelo Guervós](https://dblp.org/pid/m/JJMereloGuervos.html)

- 9. [dblp: Bernd Bischl](https://dblp.org/pid/48/5326)

- 10. [dblp: CEC 2017](https://dblp.org/db/conf/cec/cec2017)

- 11. [dblp: IJCNN 2015](https://dblp.org/db/conf/ijcnn/ijcnn2015.html)

- 12. [GECCO '25: Proceedings of the Genetic and Evolutionary Computation Conference](https://www.sigevo.org/gecco-2025/toc.html)

- 13. [dblp: GECCO Companion 2022](https://dblp.org/db/conf/gecco/gecco2022c.html)

- 14. [dblp: IEEE Transactions on Emerging Topics in Computational Intelligence, Volume 9](https://dblp.org/db/journals/tetci/tetci9)

- 15. [An Intelligent Hybrid Metaheuristic for assessing Techno-economic and Environmental Performance in Renewable-integrated Multi-objective Power Flow Framework / Journal of Electrical Systems and Information Technology / Springer Nature Link](https://link.springer.com/article/10.1186/s43067-025-00291-0)

- 16. [GitHub - TimeDelta/learning-to-learn: Learning to learn: Memory-Guided Evolution of Computation Graphs via Self-Compressing Fitness-Regularized Latent Space · GitHub](https://download.plaud.ai/TimeDelta/learning-to-learn)

- 17. [arXivDaily每日学术速递，同步arXiv全量数据，AI总结、翻译，覆盖人工智能、机器人、计算机、金融、统计学、数学、物理学、生物学、经济学、电气&系统等方向。](https://www.arxivdaily.com/)

- 18. [Monte Carlo Tree Search research / The Latest in AI](https://thelatestinai.com/topics/monte-carlo-tree-search-2)

- 19. [Daily Papers - Hugging Face](https://huggingface.co/papers)

### Batch 20: returned titles

- 1. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494622005506)

- 2. [Differential Evolution With Duplication Analysis for Feature Selection in Classification.](https://pubmed.ncbi.nlm.nih.gov/36279359/)

- 3. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494622005506)

- 4. [A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/A-multi-objective-evolutionary-algorithm-with-interval/99683066102346)

- 5. [A differential evolution-based algorithm with maturity extension for feature selection in intrusion detection system - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1110016823008207)

### Batch 21: returned titles

- 1. [DPDEPSO: A particle swarm optimization for balancing different objectives in multi-objective feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417425023279)

- 2. [DPDEPSO: A particle swarm optimization for balancing different objectives in multi-objective feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417425023279)

- 3. [Balancing Different Optimization Difficulty Between Objectives in Multi-Objective Feature Selection : vTools Events / vTools IEEE](https://events.vtools.ieee.org/m/392641)

- 4. [GitHub - HandingWangXDGroup/TAEFS-Matlab: Balancing Different Optimization Difficulty Between Objectives in Multi-Objective Feature Selection · GitHub](https://github.com/HandingWangXDGroup/TAEFS-Matlab)

- 5. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 28, Issue 6](https://ieee-cis.blogspot.com/2024/12/ieee-transactions-on-evolutionary.html)

- 6. [R10 Section Report Form](https://www.ieeer10.org/wp-content/uploads/2024/03/IEEE-NZN-2023_Council_Final-.pdf)

- 7. [Handing Wang / OpenReview](https://openreview.net/profile)

- 8. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Request PDF](https://www.researchgate.net/publication/369219815_Improved_Evolutionary_Operators_for_Sparse_Large-Scale_Multiobjective_Optimization_Problems)

- 9. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 10. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Documents - Universitat de Lleida](https://portalrecerca.udl.cat/documentos/69e3b64625ad817cf843cf8e)

- 11. [IEEE NZ Central Section Report 2024](https://www.ieeer10.org/wp-content/uploads/2024/02/IEEE-NZ-Central-Section-Report-2024.pdf)

- 12. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Article Information / J-GLOBAL](https://jglobal.jst.go.jp/en/detail)

- 13. [Computational Intelligence: IEEE Transactions on Evolutionary Computation, Volume 28, Issue 6](https://computational-intelligence.blogspot.com/2024/12/ieee-transactions-on-evolutionary.html)

- 14. [IEEE Computational Intelligence Society: 2024](https://ieee-cis.blogspot.com/2024/)

- 15. [Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2210650221001875)

- 16. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective...](https://bishtref.com/articles/10.1109/tevc.2023.3256183)

- 17. [A two-stage evolutionary framework with structural-parametric decoupling for sparse large-scale multi-objective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426021767)

- 18. [A multiple knowledge-based evolutionary algorithm for sparse large-scale multi-objective problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0952197625012825)

- 19. [IEEE Computational Intelligence Society: IEEE Transactions on Evolutionary Computation, Volume 28, Issue 2, April 2024](https://ieee-cis.blogspot.com/2024/05/ieee-transactions-on-evolutionary.html)

- 20. [IEEE Transactions on Evolutionary Computation](https://bishtref.com/journals/2331/ieee-transactions-on-evolutionary-computation)

- 21. [Improving two-layer encoding of evolutionary algorithms for sparse large-scale multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-024-01489-x)

- 22. [Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey / ACM Computing Surveys](https://doi.org/10.1145/3734865)

- 23. [GEFS-AO: A novel graph-based evolutionary feature selection method from the view of auxiliary optimization](https://ouci.dntb.gov.ua/en/works/4YmmowY8/)

- 24. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction](https://ouci.dntb.gov.ua/en/works/7A55GXzm/)

- 25. [GEFS-AO: A novel graph-based evolutionary feature selection method from the view of auxiliary optimization / Request PDF](https://www.researchgate.net/publication/394203438_GEFS-AO_A_novel_graph-based_evolutionary_feature_selection_method_from_the_view_of_auxiliary_optimization)

- 26. [Rankless / Zhenshou Song](https://alpha.rankless.org/authors/zhenshou-song)

- 27. [ISSN: 2182-2069 / E-ISSN: 2182-2077](https://jisis.org/wp-content/uploads/2026/03/2026.I1.038.pdf)

- 28. [Ururiruirurturrurt  uiou iu I ui u](https://www.cs.put.poznan.pl/ewgmcda/newsletter/Spr25.pdf)

- 29. [JOURNAL OF COMPUTATIONAL BIOLOGY](https://journals.sagepub.com/doi/pdf/10.1089/cmb.2024.0931)

- 30. 1342 

- 31. [Identifying (Quasi) Equally Informative Subsets in Feature Selection Problems for Classification: A Max-Relevance Min-Redundancy Approach / Request PDF](https://www.researchgate.net/publication/279866511_Identifying_Quasi_Equally_Informative_Subsets_in_Feature_Selection_Problems_for_Classification_A_Max-Relevance_Min-Redundancy_Approach)

- 32. [dblp: Bernd Bischl](https://dblp.org/pid/48/5326)

- 33. [GECCO '23: Proceedings of the Genetic and Evolutionary Computation Conference](https://www.sigevo.org/gecco-2023/toc.html)

- 34. [Statistical Learning and Data Science Chair :: Research](https://www.slds.stat.uni-muenchen.de/research/)

- 35. [Multi-objective optimization 9789811314704, 9789811314711 - DOKUMEN.PUB](https://dokumen.pub/multi-objective-optimization-9789811314704-9789811314711.html)

- 36. [dblp: Bernd Bischl](https://dblp.org/pid/48/5326.html)

- 37. [A novel test-cost-sensitive attribute reduction approach using binary bat algorithm / Request PDF](https://www.researchgate.net/publication/330545483_A_novel_test-cost-sensitive_attribute_reduction_approach_using_binary_bat_algorithm)

- 38. [GECCO '25 Companion: Proceedings of the Genetic and Evolutionary Computation Conference Companion](https://www.sigevo.org/gecco-2025/toc-companion.html)

- 39. [Pattern Recognition Letters / Request PDF](https://www.researchgate.net/publication/280923127_Pattern_Recognition_Letters)

- 40. [dblp: Bernd Bischl](https://dblp.dagstuhl.de/pid/48/5326.html)

- 41. [EurekaMag Full Text Articles Chapter 111475](https://journals.eurekamag.com/research/111/474/)

### Batch 22: returned titles

- 1. [Balancing Different Optimization Difficulty Between Objectives in Multiobjective Feature Selection / Request PDF](https://www.researchgate.net/publication/375780390_Balancing_Different_Optimization_Difficulty_Between_Objectives_in_Multiobjective_Feature_Selection)

- 2. [Balancing Different Optimization Difficulty Between Objectives…](https://lacuna.tiptreesystems.com/work/balancing-different-optimization-difficulty)

- 3. [Publications 2024 - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/Publications2024)

- 4. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/)

- 5. [Publications All - Groups/ECRG / Te Kura Mātai Pūkaha, Pūrorohiko / School of Engineering and Computer Science / Te Herenga Waka—Victoria University of Wellington](https://ecs.wgtn.ac.nz/Groups/ECRG/PublicationsAll)

- 6. [Balancing Different Optimization Difficulty Between Objectives in Multiobjective Feature Selection - 科研通](https://www.ablesci.com/assist/detail)

- 7. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10716353)

- 8. [Balancing Different Optimization Difficulty Between Objectives in Multiobjective Feature Selection - 科研通](https://www.ablesci.com/assist/detail)

- 9. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery - PubMed](https://pubmed.ncbi.nlm.nih.gov/39401114)

- 10. [Dual-stage optimizer for systematic overestimation adjustment applied to multi-objective genetic algorithms for biomarker selection](https://pmc.ncbi.nlm.nih.gov/articles/PMC11684899/)

- 11. [A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery.](https://pubmed.ncbi.nlm.nih.gov/39401114/)

- 12. [Microsoft Word - ETASR_V15_N4_pp-26061-26066.docx](https://etasr.com/index.php/ETASR/article/download/11388/5399/61283)

- 13. [Ururiruirurturrurt  uiou iu I ui u](https://www.cs.put.poznan.pl/ewgmcda/newsletter/Spr25.pdf)

- 14. [A Random Forest-Assisted Evolutionary Algorithm for Data-Driven Constrained Multiobjective Combinatorial Optimization of Trauma Systems — CiteStamp](https://citestamp.com/paper/10.1109/tcyb.2018.2869674)

- 15. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction](https://ouci.dntb.gov.ua/en/works/7A55GXzm/)

- 16. [Hybrid Statistical-Spectral Sparse Feature Selection with Optimization for Robust and Generalizable Lung Adenocarcinoma Classification / Engineering, Technology & Applied Science Research](https://etasr.com/index.php/ETASR/article/view/11388)

- 17. [A Hybrid Food Recommendation System Based on MOEA/D Focusing on the Problem of Food Nutritional Balance and Symmetry](https://ouci.dntb.gov.ua/en/works/9JQDQbrq/)

- 18. [Under review as a conference paper at ICLR 2026](https://openreview.net/pdf)

- 19. [Multiomics with Evolutionary Computation to Identify Molecular and Module Biomarkers for Early Diagnosis and Treatment of Complex Disease - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11942451/)

- 20. [A multi-objective evolutionary algorithm with decomposition and the information feedback for high-dimensional medical data - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494623001205)

- 21. [(PDF) Feature selection on real-time application using hybrid of flamingo search algorithm and improved non-dominated sorting genetic algorithm III](https://www.researchgate.net/publication/382633384_Feature_selection_on_real-time_application_using_hybrid_of_flamingo_search_algorithm_and_improved_non-dominated_sorting_genetic_algorithm_III)

- 22. [GECCO '24 Companion: Proceedings of the Genetic and Evolutionary Computation Conference Companion](https://www.sigevo.org/gecco-2024/toc-companion.html)

- 23. [Biodata-centric cardiovascular disease prediction using multi-objective genetic algorithm-driven deep ensembles - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12686456/)

- 24. [Pseudo-code for the proposed method / Download Scientific Diagram](https://www.researchgate.net/figure/llustration-of-Tchebycheff-method-Full-size-DOI-107717-peerj-cs261-fig-1_fig1_339629173)

- 25. [An instance of a feature selection representation / Download Scientific Diagram](https://www.researchgate.net/figure/An-instance-of-a-feature-selection-representation_fig4_339629173)

- 26. [Surrogate-assisted evolutionary optimization using on-demand helper task for high-dimensional expensive multi-objective problems - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650225004304)

- 27. [Mengjie Zhang / ScienceDirect](https://www.sciencedirect.com/author/8729040400/mengjie-zhang)

- 28. [Mengjie Zhang 0001 · Demo Data from VLDB 2026](https://taxoreview.com/v/1/lake/expert/dblp%3Az/MengjieZhang)

- 29. [Multi-Objective Coordinate Search Optimization / Request PDF](https://www.researchgate.net/publication/374173218_Multi-Objective_Coordinate_Search_Optimization)

- 30. [Main Track – IJCAI 2023](https://ijcai-23.org/main-track-accepted-papers//)

- 31. [Arxiv Day: Article](https://arxivday.com/articles)

- 32. [ICAART 2026 Abstracts](https://icaart.scitevents.org/Abstract.aspx)

- 33. [Sistem Maklumat Pusat Penyelidikan](https://ppi.ums.edu.my/SMPPPI/Scopus.aspx)

- 34. [Cancer Chemistry Hub](https://www.cancerchem.com/posts/optimization-algorithms-for-cancer-biomarker-selection-a-comparative-review-of-ai-and-machine-learning-methods)

- 35. [University of Technology Sydney](https://web-tools.uts.edu.au/publications/search.cfm)

- 36. [Publications - Fakulta elektrotechniky a informatiky - VŠB-TUO](https://www.fei.vsb.cz/en/research/publications/)

- 37. [Soft Computing: Theories and Applications: Proceedings of SoCTA 2020, Volume 1 [1] 9789811617409, 9811617406 - DOKUMEN.PUB](https://dokumen.pub/soft-computing-theories-and-applications-proceedings-of-socta-2020-volume-1-1-9789811617409-9811617406.html)

- 38. [Biodata-centric cardiovascular disease prediction using multi-objective genetic algorithm-driven deep ensembles / Scientific Reports](https://www.nature.com/articles/s41598-025-28771-3)

### Batch 23: returned titles

- 1. [An evolutionary decomposition-based multi-objective feature selection for multi-label classification](https://pmc.ncbi.nlm.nih.gov/articles/PMC7924502/)

- 2. [Balancing Different Optimization Difficulty Between Objectives in Multiobjective Feature Selection / Request PDF](https://www.researchgate.net/publication/375780390_Balancing_Different_Optimization_Difficulty_Between_Objectives_in_Multiobjective_Feature_Selection)

- 3. [Validation-based Decision Making in Data-driven Evolutionary Computation: A Case Study in Multi-objective Feature Selection / Request PDF](https://www.researchgate.net/publication/392111313_Validation-based_Decision_Making_in_Data-driven_Evolutionary_Computation_A_Case_Study_in_Multi-objective_Feature_Selection)

- 4. [Untitled](https://www.ieee-ssci.org/assets/files/S2.pdf)

- 5. [An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-025-01941-6)

- 6. [dblp: Zhenshou Song](https://dblp.org/pid/218/2087.html)

- 7. [MPEA-FS: A decomposition-based multi-population evolutionary algorithm for high-dimensional feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417424001611)

- 8. [Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems / Request PDF](https://www.researchgate.net/publication/369219815_Improved_Evolutionary_Operators_for_Sparse_Large-Scale_Multiobjective_Optimization_Problems)

- 9. [Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey / ACM Computing Surveys](https://doi.org/10.1145/3734865)

- 10. [MPEA-FS: A decomposition-based multi-population evolutionary algorithm for high-dimensional feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417424001611)

- 11. [Zhenshou SONG / Master of Engineering / Xidian University, Xi’an / Research profile](https://www.researchgate.net/profile/Zhenshou-Song)

- 12. [2025 IEEE Symposium on](https://www.proceedings.com/content/080/080469webtoc.pdf)

- 13. [A Multi-Task Decomposition-Based Evolutionary Algorithm for Tackling High-Dimensional Bi-Objective Feature Selection](https://www.mdpi.com/2227-7390/12/8/1178)

- 14. [Symmetric uncertainty based decomposition multi-objective immune algorithm for feature selection - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210650223000597)

- 15. [Improving two-layer encoding of evolutionary algorithms for sparse large-scale multiobjective optimization problems / Complex & Intelligent Systems / Springer Nature Link](https://link.springer.com/article/10.1007/s40747-024-01489-x)

- 16. [Rankless / Zhenshou Song](https://alpha.rankless.org/authors/zhenshou-song)

- 17. [An Adaptive Initialization and Reproduction-Based Evolutionary Algorithm for Tackling Bi-Objective Feature Selection in Classification](https://www.mdpi.com/2073-8994/17/5/671)

- 18. [Ian Kropp / Michigan State University / 11 Publications / 2 Citations / Related Authors](https://scispace.com/authors/ian-kropp-4crjwn485t)

- 19. [A Random Forest-Assisted Evolutionary Algorithm for Data-Driven Constrained Multiobjective Combinatorial Optimization of Trauma Systems — CiteStamp](https://citestamp.com/paper/10.1109/tcyb.2018.2869674)

- 20. [(PDF) Improving two-layer encoding of evolutionary algorithms for sparse large-scale multiobjective optimization problems](https://www.researchgate.net/publication/381268470_Improving_two-layer_encoding_of_evolutionary_algorithms_for_sparse_large-scale_multiobjective_optimization_problems)

- 21. [Selected Refereed Publications](https://homepages.ecs.vuw.ac.nz/~mengjie/papers/)

- 22. [Improved Evolutionary Strategies for Sparse Large-Scale Many-objective Optimization Problems / Request PDF](https://www.researchgate.net/publication/377071949_Improved_Evolutionary_Strategies_for_Sparse_Large-Scale_Many-objective_Optimization_Problems)

- 23. [Shahryar Rahnamayan](https://www.csauthors.net/shahryar-rahnamayan/)

- 24. [A Hybrid Food Recommendation System Based on MOEA/D Focusing on the Problem of Food Nutritional Balance and Symmetry](https://ouci.dntb.gov.ua/en/works/9JQDQbrq/)

- 25. [(PDF) Reinforcement Learning Assisted Autonomous Selection of Sparsity-Aware Genetic Operators for Sparse Large-Scale Multi-Objective Optimization](https://www.researchgate.net/publication/388846791_Reinforcement_Learning_Assisted_Autonomous_Selection_of_Sparsity-Aware_Genetic_Operators_for_Sparse_Large-Scale_Multiobjective_Optimization)

- 26. [A relevant feature combination assisted bi-level evolutionary multi-objective algorithm for feature selection in classification - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12603099/)

- 27. [Handling Different Preferences Between Objectives for Multi-objective Feature Selection in Classification / Request PDF](https://www.researchgate.net/publication/365985910_Handling_Different_Preferences_Between_Objectives_for_Multi-objective_Feature_Selection_in_Classification)

- 28. [An evolutionary multitasking algorithm for multi-objective feature selection using dual-perspective reduction / Request PDF](https://www.researchgate.net/publication/393238855_An_evolutionary_multitasking_algorithm_for_multi-objective_feature_selection_using_dual-perspective_reduction)

- 29. [Elastic net–guided NSGA-II for scalable multi-objective feature selection in high-dimensional data analytics / Discover Computing / Springer Nature Link](https://link.springer.com/article/10.1007/s10791-026-10386-5)

- 30. [Expanding Horizons of Level Diversity via Multiobjective Evolutionary Learning / Request PDF](https://www.researchgate.net/publication/385538788_Expanding_Horizons_of_Level_Diversity_via_Multiobjective_Evolutionary_Learning)

- 31. [A multi-objective evolutionary algorithm with decomposition and the information feedback for high-dimensional medical data - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1568494623001205)

- 32. [is obtained when compared to Rnd and IGR methods. It provides three cluster points that increase the searching ability of the algorithm. Nevertheless, our proposed method (green markers) generates the most diverse individuals among all methods. It provides a large space for the search algorithm for exploration and exploitation. Moreover, it achieves the highest accuracy values among all methods as it leverages the information obtained from the information gain metric. As a result, when finding the most promising features, the evolutionary algorithm is challenged as the number of features increases. Therefore, a diverse initial population boosted with intrinsic knowledge can enhance the searching ability of the algorithm by broadening its exploration space.](https://shura.shu.ac.uk/31056/1/Boosting_Initial_Population_in_Multiobjective_Feature_Selection_with_Knowledge_Based_Partitioning.pdf)

- 33. [(PDF) Evolutionary Computation for Sparse Multi-Objective Optimization: A Survey](https://www.researchgate.net/publication/391319449_Evolutionary_Computation_for_Sparse_Multi-Objective_Optimization_A_Survey)

- 34. [Sparse knowledge guided multiobjective multimodal optimization for identification of personalized critical biomarkers in cancer - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025526000046)

- 35. [(PDF) Feature selection on real-time application using hybrid of flamingo search algorithm and improved non-dominated sorting genetic algorithm III](https://www.researchgate.net/publication/382633384_Feature_selection_on_real-time_application_using_hybrid_of_flamingo_search_algorithm_and_improved_non-dominated_sorting_genetic_algorithm_III)

- 36. [A Survey on Evolutionary Computation Approaches to Feature Selection](https://eurekamag.com/research/102/517/102517301.php)

- 37. [Neural network-assisted evolutionary search for large-scale sparse multiobjective optimization - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426028964)

- 38. [EMOPG+FS: Evolutionary multi-objective prototype generation and feature selection](https://eurekamag.com/research/064/836/064836719.php)

- 39. [Evolutionary multi-feature construction for data reduction: a case study](https://settings.eurekamag.com/research/083/816/083816087.php)

- 40. [The principal role in data-driven decision making: using case-study data to develop multi-mediator models of educational reform](https://changelog.eurekamag.com/research/088/870/088870863.php)

### Batch 24: returned titles

### Batch 25: returned titles

- 1. [An Indicator-Based Evolutionary Algorithm for Large-Scale Constrained Multiobjective Optimization / IEEE Journals & Magazine / IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10897802)

### Batch 26: returned titles

- 1. [Please do not remove this page](https://s3.eu-central-1.amazonaws.com/eu-st01.ext.exlibrisgroup.com/44SUR_INST/upload/1771391625258/An%20Evolutionary%20Algorithm%20for%20Large-Scale%20Sparse%20Multi-Objective%20Optimization%20Problems.pdf)

- 2. [An Evolutionary Algorithm for Large-Scale Sparse Multi-Objective Optimization Problems - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/An-Evolutionary-Algorithm-for-Large-Scale-Sparse/99515481102346)

- 3. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems / Synapse](https://synapsesocial.com/papers/6a0ec8f5a14f152feaf9d6bc)

- 4. [A survey on soft computing-based high-utility itemsets mining](https://repository.bothouniversity.ac.bw/buir/bitstream/handle/123456789/172/Kumar-Singhnew-compressed_compressed.pdf)

- 5. [A Pattern Mining-Based Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems - University of Surrey](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/A-Pattern-Mining-Based-Evolutionary-Algorithm-for/99771841002346)

- 6. [A multiple knowledge-based evolutionary algorithm for sparse large-scale multi-objective problems - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0952197625012825)

- 7. [Improved SparseEA for sparse large-scale multi-objective optimization problems](https://ouci.dntb.gov.ua/en/works/lmyO02ol/)

- 8. [GitHub - zongtingwei/SparseEA: code for "An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems" · GitHub](https://github.com/zongtingwei/SparseEA)

- 9. [dblp: An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://dblp.dagstuhl.de/rec/journals/tec/TianZWJ20.html)

- 10. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems - 科研通](https://www.ablesci.com/assist/detail)

- 11. [GitHub - CianSteenkamp96/PlatEMO_research · GitHub](https://github.com/CianSteenkamp96/PlatEMO_research)

- 12. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems (2019) – IEEE Transactions on Evolutionary Computation / Metascience Observatory Explorer](https://explore.metascienceobservatory.org/papers/W2946739419)

- 13. [dblp: An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://dblp.uni-trier.de/rec/journals/tec/TianZWJ20.html)

- 14. [(PDF) Attacking Evolutionary Algorithms via SparseEA](https://www.researchgate.net/publication/383378916_Attacking_Evolutionary_Algorithms_via_SparseEA)

- 15. [PlatEMO/PlatEMO/platemo.m at master · BIMK/PlatEMO · GitHub](https://github.com/BIMK/PlatEMO/blob/master/PlatEMO/platemo.m)

- 16. [Finding R&D Trends and Experts Made Simple / Scinapse](https://www.scinapse.io/papers/2946739419)

- 17. [An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems — Lacuna](https://lacuna.tiptreesystems.com/work/an-evolutionary-algorithm-for-large-scale-sparse-multiobjective-optimization/wrk_4e1ed4fc7318d6a4c57761d6901522af)

- 18. [An Evolutionary Algorithm For Large-Scale Sparse Multiobjective Optimization Problems / PDF / Pareto Efficiency / Algorithms](https://www.scribd.com/document/1062223139/An-Evolutionary-Algorithm-for-Large-Scale-Sparse-Multiobjective-Optimization-Problems)

- 19. [Integrating Conjugate Gradients Into Evolutionary Algorithms for Large-Scale Continuous Multi-Objective Optimization](https://www.ieee-jas.com/en/article/doi/10.1109/JAS.2022.105875)

- 20. [A Pattern Mining-Based Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems.](https://pubmed.ncbi.nlm.nih.gov/33378271/)

- 21. [Evolution algorithm with adaptive genetic operator and dynamic scoring mechanism for large-scale sparse many-objective optimization](https://pmc.ncbi.nlm.nih.gov/articles/PMC11920420/)

- 22. [A multi-objective sparse evolutionary framework for large-scale weapon target assignment based on a reward strategy - Xiaoping Shi, Shiqi Zou, Shenmin Song, Rui Guo, 2021](https://journals.sagepub.com/doi/abs/10.3233/JIFS-202679)

- 23. [A two-stage evolutionary algorithm for large-scale sparse multiobjective optimization problems](https://eurekamag.com/research/095/516/095516033.php)

- 24. [Enhanced SparseEA for large-scale multi-objective feature selection problems](https://ouci.dntb.gov.ua/en/works/42aYp3B7/)

- 25. [Ye Tian](https://www.csauthors.net/ye-tian-009/)

- 26. [Evolutionary Algorithms for Sparse Large‐Scale Multi‐Objective Optimization - Evolutionary Large‐Scale Multi‐Objective Optimization and Applications - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/9781394178445.ch4)

- 27. [sustainability](https://www.wisdomlib.org/uploads/journals/mdpi-sust/2023-volume-15-issue-12--2071-1050-15-12-9238-.pdf)

- 28. 1

- 29. [Solving Large-Scale Multi-Objective Optimization Problems with Sparse Optimal Solutions via Unsupervised Neural Networks](https://eu-st01.ext.exlibrisgroup.com/44SUR_INST/upload/1776250543628/FINAL%20VERSION.pdf)

- 30. [Evolutionary Large-scale Sparse Multi-objective Optimization for Collaborative Edge-cloud Computation Offloading](https://www.scitepress.org/PublishedPapers/2020/101455/101455.pdf)
