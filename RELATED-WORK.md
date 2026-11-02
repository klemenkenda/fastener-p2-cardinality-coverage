# Critical related-work review for P2

Verified on 2 November 2026. Catalogue: **42 distinct papers**, including all eight supplied items and all four named leads. Bibliographic identity is verified for every catalogue entry; substantive access is weaker for some records and is stated individually. None is labelled full-text-read merely because a PDF was available. Three records in group F are deliberately provisional in content.

## Main assessment

P2 should be framed as a controlled empirical diagnosis of a known design problem. The literature already establishes sparse and size-aware initialisation, changes to the cardinality dynamics of variation, duplicate handling, and front metrics sensitive to extent. What still looks potentially useful is the joint measurement of threshold access, exact-size quality and proposal/cache overhead within the same controlled selector. Whether that combination is sufficiently informative depends on the unrun pilot, not on the large H1 AUF differences alone.

The strongest added risks are [Cong2026](https://doi.org/10.3390/bioengineering13101229) for a recent finite-budget sparse-access ablation, [Koprivec2020](https://doi.org/10.3390/e22111198) for the exact AUF formula, and [Li2026CORAL](https://doi.org/10.3390/info17060593) for size-stratified survival. The 2026 extension [Miyandoab2026](https://doi.org/10.1007/s13042-025-02921-5) also strengthens the overlap with the already identified 2024 initialiser. See the [novelty and experimental-design assessment](related-work/NOVELTY.md) for the claim-by-claim judgement and experimental requirements.

## Local H1 comparison and limits on claims

Algorithm 2 of [Miyandoab2024](https://arxiv.org/html/2407.17795v2) first samples an integer cardinality uniformly between `minVars` and `maxVars`, then selects that many feature indices without replacement. The local `sparse_initialization` uses the same sampling procedure with bounds `1` and `min(30, d)`. This compares sampling distributions; it does not establish that code was copied.

The published algorithm starts over `1..d` and later inserts new solutions; H1 uses a bounded initial range without that reinsertion step. Operators and evaluation measures also differ. These differences justify controlled comparisons, but do not establish a new general initialiser. Li2025 supplies the local OBL/crossover/SSOM starting point; expected cardinality preservation is already stated there. The local implementation and its evidence limits are discussed in [EVIDENCE.md](EVIDENCE.md).

| Candidate claim | Assessment |
|---|---|
| We propose sparse initialisation of NSGA-II for feature selection. | Too broad as a novelty claim; direct precedents already exist. |
| We first choose a subset size, then select random features. | An existing published procedure. |
| Initialisation can determine which front region is reached. | An established motivation; P2 needs an additional quantitative or methodological finding. |
| Our local OBL + SSOM rarely reaches k <= 10 under the H1 budget. | Supported only for the final fronts and the particular implementation examined in H1. |
| H1 proves that NSGA-II generally performs poorly at small k. | Unsupported: NSGA-II does not prescribe these operators or this initialisation. |
| Evaluation should separate reach, improvement after initialisation, and quality conditional on size. | A useful methodological question whose independent novelty remains unproven. |

The earlier targeted review of 31 October 2026 rejected the broad new-initialiser claim. The expanded review below retains that conclusion and updates the reading depth and follow-up status of the original leads. Neither review reproduces the competing methods or establishes an exhaustive absence of prior work. The bibliography is consolidated in [references.bib](manuscript/references.bib).

## Verified core list

All supplied DOIs identify the intended papers. The major corrections are full-title expansions and added author/publication details, rather than mistaken DOI identities. The Jiao lead's missing DOI is supplied. DOI routing is distinguished from publisher-page access in the [corrections and verification audit](related-work/CORRECTIONS.md).

| Supplied item | Catalogue key | Publication details | Verification / reading depth |
|---|---|---|---|
| 1 | [Deniz2019](https://doi.org/10.1016/j.eswa.2019.06.063) | Expert Systems with Applications 137: 11-21 (2019) | specific sections: 2.1-2.2; abstract and experimental framing |
| 2 | [Deniz2022](https://doi.org/10.1109/IJCNN55064.2022.9892123) | 2022 International Joint Conference on Neural Networks (IJCNN) : 1-8 (2022) | specific sections: II-III, Algorithms 3-6 |
| 3 | [Kropp2022](https://doi.org/10.1016/j.swevo.2021.101025) | Swarm and Evolutionary Computation 69: 101025 (2022) | abstract only; publisher highlights and introduction snippets |
| 4 | [Xue2022](https://doi.org/10.1016/j.asoc.2022.109420) | Applied Soft Computing 127: 109420 (2022) | abstract only; publisher highlights and section snippets |
| 5 | [Miyandoab2024](https://doi.org/10.1109/CEC60901.2024.10612084) | 2024 IEEE Congress on Evolutionary Computation (CEC) : 1-8 (2024) | specific sections: III, Algorithms 1-2; IV-A/B and conclusion; arXiv v2 |
| 6 | [Li2025](https://doi.org/10.1016/j.ejor.2024.12.036) | European Journal of Operational Research 323(3): 952-965 (2025) | specific sections: 4.2-4.3, 5 parameter settings, 7.1; abstract and improvement-phase description |
| 7 | [Xu2025AIMEA](https://doi.org/10.1007/s40747-025-01941-6) | Complex & Intelligent Systems 11(7): 310 (2025) | specific sections: 3 adaptive initialisation/reproduction/merging; 4 metrics/settings; rights statement |
| 8 | [Wang2026](https://doi.org/10.3390/electronics15010236) | Electronics 15(1): 236 (2026) | specific sections: 3.4 and framework/duplicate handling; sparse-start ablation excerpts and licence |
| Lead 1 | [Oh2004](https://doi.org/10.1109/TPAMI.2004.105) | IEEE Transactions on Pattern Analysis and Machine Intelligence 26(11): 1424-1437 (2004) | specific sections: 3.1-3.5; printed page 1427 visually checked |
| Lead 2 | [Kropp2024](https://doi.org/10.1109/TEVC.2023.3256183) | IEEE Transactions on Evolutionary Computation 28(2): 460-473 (2024) | abstract only; paper abstract as indexed, publisher metadata and author CV |
| Lead 3 | [AsilianBidgoli2020](https://doi.org/10.7717/peerj-cs.261) | PeerJ Computer Science 6: e261 (2020) | specific sections: proposed method initialisation; evaluation criteria and comparative Pareto-front discussion; Europe PMC XML |
| Lead 4 | [Jiao2024PRDH](https://doi.org/10.1109/TEVC.2022.3215745) | IEEE Transactions on Evolutionary Computation 28(4): 846-860 (2024) | abstract only; publisher-indexed abstract and author publication record |


## How to interpret the catalogue

Each paper below has a full reference, inspected source, reading depth, method summary, overlap and a limit on what the inspected evidence establishes. **Direct** means it addresses at least one P2 component explicitly, not that it duplicates the entire paper. **Partial** means related mechanisms or a broader sparse-optimisation setting. **Background** supplies context, measurement or reporting practice.

The five topic codes in COMPARISON.csv are D (direct), P (partial), B (background), - (not established in the inspected material), and ? (unverified). A dash is not a claim that the complete paper never discusses the topic. An abstract-only record cannot establish a precise operator implementation or an absence claim.

The fixed-budget experiments and numerical outcomes of H1-E02 are author-supplied evidence, not verified literature results. The proposed factorial pilot has not been run.


## Initialisation, size allocation and access to sparse regions


### Deniz2019 — direct overlap

Ayça Deniz and Hakan Ezgi Kiziloz (2019). On initial population generation in feature subset selection. *Expert Systems with Applications* 137: 11-21. [doi:10.1016/j.eswa.2019.06.063](https://doi.org/10.1016/j.eswa.2019.06.063).

**Read:** specific sections: 2.1-2.2; abstract and experimental framing. [Inspected source](https://shura.shu.ac.uk/30147/1/initial_population_generation.pdf).

**What it does:** Compares five population-generation methods in multiobjective TLBO feature selection. Small Random builds nested random subsets of successively increasing sizes; information-gain and greedy starts also span sizes.

**Overlap with P2:** Direct precedent for investigating initialisation empirically, including a sparse random start. Duplicate removal also appears in the search flow.

**Critical limit:** Does not establish the proposed fixed-unique-fit reach/conditional-quality decomposition. Small Random is not IID uniform-cardinality sampling.


### Deniz2022 — direct overlap

Ayça Deniz and Hakan Ezgi Kiziloz (2022). Boosting Initial Population in Multiobjective Feature Selection with Knowledge-Based Partitioning. *2022 International Joint Conference on Neural Networks (IJCNN)*: 1-8. [doi:10.1109/IJCNN55064.2022.9892123](https://doi.org/10.1109/IJCNN55064.2022.9892123).

**Read:** specific sections: II-III, Algorithms 3-6. [Inspected source](https://shura.shu.ac.uk/31056/1/Boosting_Initial_Population_in_Multiobjective_Feature_Selection_with_Knowledge_Based_Partitioning.pdf).

**What it does:** Partitions candidate sizes into feature-ratio bands with controlled deviations, then samples features using information-gain quartiles. Contrasts random, ranked and segmented starts.

**Overlap with P2:** Strong size-stratified initialisation precedent: selected-feature counts are an explicit design variable.

**Critical limit:** Knowledge guidance and cardinality allocation are coupled; its aggregate performance cannot isolate the P2 mechanism.


### Kropp2022 — direct overlap

Ian Kropp and A. Pouyan Nejadhashemi and Kalyanmoy Deb (2022). Benefits of sparse population sampling in multi-objective evolutionary computing for large-Scale sparse optimization problems. *Swarm and Evolutionary Computation* 69: 101025. [doi:10.1016/j.swevo.2021.101025](https://doi.org/10.1016/j.swevo.2021.101025).

**Read:** abstract only; publisher highlights and introduction snippets. [Inspected source](https://www.sciencedirect.com/science/article/pii/S2210650221001875).

**What it does:** Introduces sparse population sampling as a replacement initialisation routine across population-based algorithms on sparse large-scale multiobjective problems; reports hypervolume benefits.

**Overlap with P2:** The general benefit of supplying sparse starting genomes, including NSGA-II comparisons, is already established.

**Critical limit:** General sparse optimisation is broader than wrapper FS. Exact SPS parameterisation and the full experimental protocol were not verified from full text.


### Xue2022 — direct overlap

Yu Xue and Xu Cai and Ferrante Neri (2022). A multi-objective evolutionary algorithm with interval based initialization and self-adaptive crossover operator for large-scale feature selection in classification. *Applied Soft Computing* 127: 109420. [doi:10.1016/j.asoc.2022.109420](https://doi.org/10.1016/j.asoc.2022.109420).

**Read:** abstract only; publisher highlights and section snippets. [Inspected source](https://www.sciencedirect.com/science/article/pii/S1568494622005506).

**What it does:** MOEA-ISa combines interval-based initialisation with a similarity-sensitive crossover that controls offspring nonzero counts and uses ReliefF weights.

**Overlap with P2:** Direct overlap with choosing initial and offspring cardinality distributions.

**Critical limit:** Do not infer an exact uniform 1..30 procedure, exact size coverage, or a missing-size convention from the accessible abstract.


### Miyandoab2024 — direct overlap

Sevil Zanjani Miyandoab and Shahryar Rahnamayan and Azam Asilian Bidgoli and Sevda Ebrahimi and Masoud Makrehchi (2024). Enhancing Diversity in Multi-Objective Feature Selection. *2024 IEEE Congress on Evolutionary Computation (CEC)*: 1-8. [doi:10.1109/CEC60901.2024.10612084](https://doi.org/10.1109/CEC60901.2024.10612084).

**Read:** specific sections: III, Algorithms 1-2; IV-A/B and conclusion; arXiv v2. [Inspected source](https://arxiv.org/html/2407.17795v2).

**What it does:** Algorithm 2 samples a cardinality uniformly in a supplied range and selects that many indices without replacement. Algorithm 1 begins over 1..d and replaces the last front using current minimum/maximum sizes.

**Overlap with P2:** P2 uses an existing initialiser with different bounds. The paper also argues for evaluation-count stopping and reports duplicate elimination.

**Critical limit:** It does not, in the inspected sections, separate threshold reach from quality at equal size or diagnose the SSOM/cache interaction. Full reinsertion must be distinguished from initialisation alone.


### Xu2025AIMEA — direct overlap

Hang Xu and Bing Xue and Mengjie Zhang (2025). An adaptive initialization and multitasking based evolutionary algorithm for bi-objective feature selection in classification. *Complex & Intelligent Systems* 11(7): article 310. [doi:10.1007/s40747-025-01941-6](https://doi.org/10.1007/s40747-025-01941-6).

**Read:** specific sections: 3 adaptive initialisation/reproduction/merging; 4 metrics/settings; rights statement. [Inspected source](https://link.springer.com/article/10.1007/s40747-025-01941-6).

**What it does:** AIMEA adaptively probes subpopulations at progressively smaller feature-selection probabilities, retains promising ones and merges tasks during evolution.

**Overlap with P2:** Explicitly links different initial size regions to search performance; also discusses duplicate subpopulations.

**Critical limit:** HV and selected-solution error/size are reported; inspected experiments stop after 100 generations, which is not P2 unique-fit accounting.


### Wang2026 — direct overlap

Ying Wang and Renjie Fan and Lei Cheng and Bo Gong and Jiahao Liu (2026). An Improved Adaptive NSGA-II with Multiple Filtering for High-Dimensional Feature Selection. *Electronics* 15(1): 236. [doi:10.3390/electronics15010236](https://doi.org/10.3390/electronics15010236).

**Read:** specific sections: 3.4 and framework/duplicate handling; sparse-start ablation excerpts and licence. [Inspected source](https://www.mdpi.com/2079-9292/15/1/236).

**What it does:** AF-NSGA-II uses ReliefF, maximal information coefficient and Fisher scores for initial feature weights, an adaptive crossover and decision-space duplicate removal.

**Overlap with P2:** Another direct sparse-initialisation/operator precedent with component ablations.

**Critical limit:** The prose and pseudocode require careful implementation checking; the random count parameter alone does not guarantee coverage of every small size.


### AsilianBidgoli2020 — direct overlap

Azam Asilian Bidgoli and Hossein Ebrahimpour-Komleh and Shahryar Rahnamayan (2020). An evolutionary decomposition-based multi-objective feature selection for multi-label classification. *PeerJ Computer Science* 6: e261. [doi:10.7717/peerj-cs.261](https://doi.org/10.7717/peerj-cs.261).

**Read:** specific sections: proposed method initialisation; evaluation criteria and comparative Pareto-front discussion; Europe PMC XML. [Inspected source](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7924502/fullTextXML).

**What it does:** Decomposition-based multi-label FS with local search and an operator pool. Discusses small-feature regions missed by NSGA-II, equal-feature-count comparisons, and wider fronts producing better HV.

**Overlap with P2:** Qualitative reach-versus-front-performance concerns already appear here; set coverage means dominance coverage.

**Critical limit:** The inspected initialisation text does not establish the exact uniform-cardinality Algorithm 2 used in the 2024 paper. Do not infer that procedure from a citation alone.


### Xue2014 — partial overlap

Bing Xue and Mengjie Zhang and Will N. Browne (2014). Particle swarm optimisation for feature selection in classification: Novel initialisation and updating mechanisms. *Applied Soft Computing* 18: 261-276. [doi:10.1016/j.asoc.2013.09.018](https://doi.org/10.1016/j.asoc.2013.09.018).

**Read:** specific sections: proposed initialisation mechanisms; computational-time discussion; abstract. [Inspected source](https://homepages.ecs.vuw.ac.nz/~xuebing/Papers/1-s2.0-S1568494613003128-main.pdf).

**What it does:** PSO feature selection studies three initialisation strategies and three best-solution update mechanisms, motivated by forward and backward selection.

**Overlap with P2:** Shows sparse/mixed initialisation and its effects on selected size, prediction and cost were studied well before P2.

**Critical limit:** PSO update dynamics differ from NSGA-II; it does not supply the proposed front-reach decomposition.


### Xu2020 — direct overlap

Hang Xu and Bing Xue and Mengjie Zhang (2020). Segmented initialization and offspring modification in evolutionary algorithms for bi-objective feature selection. *Proceedings of the 2020 Genetic and Evolutionary Computation Conference*: 444-452. [doi:10.1145/3377930.3390192](https://doi.org/10.1145/3377930.3390192).

**Read:** abstract only; segmented scheme corroborated in Deniz2022 Section II. [Inspected source](https://doi.org/10.1145/3377930.3390192).

**What it does:** Studies segmented initialisation and offspring modification for bi-objective FS. The cited segmented start uses groups with inclusion probabilities 0.25, 0.5 and 0.75.

**Overlap with P2:** Direct precedent for spreading initial populations across different size regions.

**Critical limit:** Density segments remain binomial within groups and are distinct from uniform cardinality or guaranteed occupancy.


### Xu2025PPI — direct overlap

Hang Xu and Bing Xue and Mengjie Zhang (2025). Probe Population-Based Initialization and Genetic Pool-Based Reproduction for Evolutionary Bi-Objective Feature Selection. *IEEE Transactions on Evolutionary Computation* 29(5): 1849-1863. [doi:10.1109/TEVC.2024.3403655](https://doi.org/10.1109/TEVC.2024.3403655).

**Read:** abstract only; publisher-indexed record. [Inspected source](https://ieeexplore.ieee.org/abstract/document/10536003).

**What it does:** Adds probe-population initialisation and genetic-pool reproduction to improve bi-objective evolutionary FS.

**Overlap with P2:** Further established coupling of initialisation and reproduction in this exact problem family.

**Critical limit:** Its precise cardinality law and evaluation accounting need full-text verification before reimplementation.


### Cong2026 — direct overlap

Yilei Cong and Tengfei Wu and Xinyu Yang and Yiyun Zhu and Min Tang and Hua Yang and Ping Liu (2026). Nested Evaluation of Sparse Multi-Objective Evolutionary Gene-Panel Discovery for Diabetic Nephropathy. *Bioengineering* 13(10): 1229. [doi:10.3390/bioengineering13101229](https://doi.org/10.3390/bioengineering13101229).

**Read:** specific sections: 3.4-3.5; 4.5/Table 6 and discussion excerpts; licence. [Inspected source](https://www.mdpi.com/2306-5354/13/10/1229).

**What it does:** Isolates harmonic sparse starts against IID harmonic, mean-matched/dense Bernoulli, bounded uniform and SparseEA controls at a fixed evaluation target. Reports access to compact fronts.

**Overlap with P2:** A major new novelty risk: finite-budget sparse-region access is already an explicit experimental question.

**Critical limit:** Its application and objectives differ; P2 must demonstrate additional reach/quality separation and SSOM/cache mechanisms rather than repeat its initialisation conclusion.


### Miyandoab2026 — direct overlap

Sevil Zanjani Miyandoab and Shahryar Rahnamayan and Azam Asilian Bidgoli and Masoud Makrehchi (2026). A comparative study on population-based multi-objective feature selection. *International Journal of Machine Learning and Cybernetics* 17(3): article 105. [doi:10.1007/s13042-025-02921-5](https://doi.org/10.1007/s13042-025-02921-5).

**Read:** abstract only; publisher preview and reference list. [Inspected source](https://link.springer.com/article/10.1007/s13042-025-02921-5).

**What it does:** Compares Diverse NSGA-II, Compact NSGA-II and multiobjective coordinate search, extending them with genuine uniform initialisation across nine high-dimensional datasets.

**Overlap with P2:** A later same-group study strengthens the initialiser/diversity overlap beyond the 2024 conference paper.

**Critical limit:** Subscription preview only; do not assume all 2024 settings or duplicate-counting semantics remain identical.


## Variation, balanced mutation and sparse-search algorithms


### Li2025 — direct overlap

An-Da Li and Zhen He and Qing Wang and Yang Zhang and Yanhui Ma (2025). A multi-objective evolutionary algorithm with mutual-information-guided improvement phase for feature selection in complex manufacturing processes. *European Journal of Operational Research* 323(3): 952-965. [doi:10.1016/j.ejor.2024.12.036](https://doi.org/10.1016/j.ejor.2024.12.036).

**Read:** specific sections: 4.2-4.3, 5 parameter settings, 7.1; abstract and improvement-phase description. [Inspected source](https://andali89.github.io/homepage/pubs/2025_NSGAIIMIIP_manuscript.pdf).

**What it does:** NSGAII-MIIP combines complementary OBL starts, modified single-point crossover, SSOM and an MI-guided improvement phase. Section 4.3 explicitly states SSOM preserves expected selected-feature count.

**Overlap with P2:** Direct source of P2 operators; Section 7.1 uses HV, IGD and dominance set coverage with empirical reference sets.

**Critical limit:** P2 omits the central improvement phase and changes the classifier/score/data. Its results are not a replication or refutation of the complete method.


### Oh2004 — direct overlap

Il-Seok Oh and Jin-Seon Lee and Byung-Ro Moon (2004). Hybrid genetic algorithms for feature selection. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 26(11): 1424-1437. [doi:10.1109/TPAMI.2004.105](https://doi.org/10.1109/TPAMI.2004.105).

**Read:** specific sections: 3.1-3.5; printed page 1427 visually checked. [Inspected source](https://sci2s.ugr.es/keel/pdf/specific/articulo/Oh_Hybrid_2004.pdf).

**What it does:** Hybrid GA with local search and subset-size control. Section 3.4 gives controlled mutation with p1=pm and p0=pm*n1/n0; initial bits use a target-size inclusion probability.

**Overlap with P2:** Confirms the balanced-mutation formula predates Li et al. The original terminology is controlled mutation.

**Critical limit:** Expected balance is not exact child-wise cardinality preservation. This is not a modern MOEA front-coverage study.


### Kropp2024 — partial overlap

Ian Kropp and A. Pouyan Nejadhashemi and Kalyanmoy Deb (2024). Improved Evolutionary Operators for Sparse Large-Scale Multiobjective Optimization Problems. *IEEE Transactions on Evolutionary Computation* 28(2): 460-473. [doi:10.1109/TEVC.2023.3256183](https://doi.org/10.1109/TEVC.2023.3256183).

**Read:** abstract only; paper abstract as indexed, publisher metadata and author CV. [Inspected source](https://doi.org/10.1109/TEVC.2023.3256183).

**What it does:** Proposes varied striped sparse population sampling (VSSPS), sparse simulated binary crossover and sparse polynomial mutation for sparse large-scale multiobjective optimisation.

**Overlap with P2:** Shows initialisation and variation must be considered together to retain and optimise sparsity.

**Critical limit:** Continuous sparse operators are not a drop-in binary SSOM baseline. Full operator derivations and exact protocol remain unverified.


### Li2026CORAL — direct overlap

Wei Li and Heming Jia and Chunyu Han (2026). CORAL: A Rank-Memory Search Framework for Multi-Objective Feature Selection. *Information* 17(6): 593. [doi:10.3390/info17060593](https://doi.org/10.3390/info17060593).

**Read:** specific sections: 3.1-3.3; ablation discussion and licence. [Inspected source](https://www.mdpi.com/2078-2489/17/6/593).

**What it does:** CORAL separates continuous feature priorities from an explicit cardinality variable, uses Top-K decoding, rank memory, local remove-add refinement and size-stratified environmental selection.

**Overlap with P2:** Direct prior art for maintaining coverage across sparsity regions during evolution.

**Critical limit:** It is a proposed algorithm, not the same diagnostic study. Its bounded cardinality setting must be disclosed in any comparison.


### Tian2020SparseEA — direct overlap

Ye Tian and Xingyi Zhang and Chao Wang and Yaochu Jin (2020). An Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems. *IEEE Transactions on Evolutionary Computation* 24(2): 380-393. [doi:10.1109/TEVC.2019.2918140](https://doi.org/10.1109/TEVC.2019.2918140).

**Read:** abstract only; original sparse initialisation corroborated in Chu2024 SparseEA section and Cong2026 Section 3.5. [Inspected source](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/An-Evolutionary-Algorithm-for-Large-Scale-Sparse/99515481102346).

**What it does:** SparseEA uses sparsity-aware encoding, variable scoring, initialisation and genetic operators for large-scale sparse MOO, including FS applications.

**Overlap with P2:** Essential sparse-search baseline family, beyond replacing a dense initial population.

**Critical limit:** The single-variable scoring cost must be charged. A binary-mask adaptation should be documented and distinguished from the full real/binary algorithm.


### Tian2021PSL — partial overlap

Ye Tian and Chang Lu and Xingyi Zhang and Kay Chen Tan and Yaochu Jin (2021). Solving Large-Scale Multiobjective Optimization Problems With Sparse Optimal Solutions via Unsupervised Neural Networks. *IEEE Transactions on Cybernetics* 51(6): 3115-3128. [doi:10.1109/TCYB.2020.2979930](https://doi.org/10.1109/TCYB.2020.2979930).

**Read:** abstract only; publisher/PubMed record. [Inspected source](https://pubmed.ncbi.nlm.nih.gov/32217494/).

**What it does:** MOEA/PSL learns a Pareto-optimal subspace using unsupervised neural networks to reduce sparse large-scale search difficulty.

**Overlap with P2:** Relevant background on locating sparse support within finite evaluation resources.

**Critical limit:** General sparse optimisation and learned continuous representations do not directly establish P2 binary size-axis measurements.


### Tian2022PM — partial overlap

Ye Tian and Chang Lu and Xingyi Zhang and Fan Cheng and Yaochu Jin (2022). A Pattern Mining-Based Evolutionary Algorithm for Large-Scale Sparse Multiobjective Optimization Problems. *IEEE Transactions on Cybernetics* 52(7): 6784-6797. [doi:10.1109/TCYB.2020.3041325](https://doi.org/10.1109/TCYB.2020.3041325).

**Read:** abstract only; publisher/PubMed record. [Inspected source](https://pubmed.ncbi.nlm.nih.gov/33378271/).

**What it does:** PM-MOEA mines lower/upper candidate nonzero-variable sets and designs binary crossover and mutation to retain sparsity.

**Overlap with P2:** Establishes that sparsity-aware reproduction and support restriction are active design choices.

**Critical limit:** Do not equate sparse support discovery with guaranteed coverage of every subset size.


### Zhang2023SparseEA2 — partial overlap

Yajie Zhang and Ye Tian and Xingyi Zhang (2023). Improved SparseEA for sparse large-scale multi-objective optimization problems. *Complex & Intelligent Systems* 9(2): 1127-1142. [doi:10.1007/s40747-021-00553-0](https://doi.org/10.1007/s40747-021-00553-0).

**Read:** abstract only; rights statement and bibliographic header. [Inspected source](https://link.springer.com/article/10.1007/s40747-021-00553-0).

**What it does:** Improved SparseEA couples real and binary encoding layers through variable grouping to balance sparsity maintenance with optimisation of nonzero variables.

**Overlap with P2:** Highlights a finite-budget trade-off between producing sparse points and optimising their contents.

**Critical limit:** Primarily general sparse LSMOPs, not a direct SSOM or exact-k study. Online 2021; journal issue 2023.


### Chu2024 — partial overlap

Shu-Chuan Chu and Zhongjie Zhuang and Jeng-Shyang Pan and Ali Wagdy Mohamed and Chia-Cheng Hu (2024). Enhanced SparseEA for large-scale multi-objective feature selection problems. *Complex & Intelligent Systems* 10(1): 485-507. [doi:10.1007/s40747-023-01177-2](https://doi.org/10.1007/s40747-023-01177-2).

**Read:** specific sections: abstract/introduction and SparseEA description; licence. [Inspected source](https://link.springer.com/article/10.1007/s40747-023-01177-2).

**What it does:** Enhances SparseEA for FS using ReliefF filtering, adaptive feature scores and differential-evolution difference operators.

**Overlap with P2:** A feature-selection-specific sparse successor, showing why a complete sparse algorithm can outperform a borrowed start.

**Critical limit:** Filtering changes the candidate feature universe; account for that and for all scoring/preprocessing work in a fair comparison. Online 2023; issue 2024.


### Qian2015 — background overlap

Chao Qian and Yang Yu and Zhi-Hua Zhou (2015). Subset Selection by Pareto Optimization. *Advances in Neural Information Processing Systems 28 (NIPS 2015)*. [Official proceedings](https://proceedings.neurips.cc/paper/2015/hash/b4d168b48157c623fbd095b4a565b5bb-Abstract.html); DOI unverified.

**Read:** abstract only; official proceedings record. [Inspected source](https://proceedings.neurips.cc/paper/2015/hash/b4d168b48157c623fbd095b4a565b5bb-Abstract.html).

**What it does:** POSS applies Pareto optimisation to small-subset selection and supplies approximation guarantees for sparse regression.

**Overlap with P2:** Relevant sparse-start/Pareto subset-selection lineage and a simple external baseline candidate.

**Critical limit:** Its theoretical results do not transfer automatically to decision-tree validation F1.


### Song2024 — direct overlap

Zhenshou Song and Handing Wang and Bing Xue and Mengjie Zhang (2024). Balancing Different Optimization Difficulty Between Objectives in Multiobjective Feature Selection. *IEEE Transactions on Evolutionary Computation* 28(6): 1824-1837. [doi:10.1109/TEVC.2023.3334233](https://doi.org/10.1109/TEVC.2023.3334233).

**Read:** abstract only; author repository README checked. [Inspected source](https://github.com/HandingWangXDGroup/TAEFS-Matlab).

**What it does:** TAEFS addresses unequal difficulty of the feature-count and classification objectives with two archives, dimensionality reduction and diversity-based mutation.

**Overlap with P2:** Strong precedent for distinguishing movement toward smaller subsets from improving their predictive content.

**Critical limit:** The README also cautions about evaluating selected training fronts on test data. It is not an exact AUF reach/quality decomposition.


## Front metrics, coverage and performance at a feature limit


### Koprivec2020 — direct overlap

Filip Koprivec and Klemen Kenda and Beno Šircelj (2020). FASTENER Feature Selection for Inference from Earth Observation Data. *Entropy* 22(11): 1198. [doi:10.3390/e22111198](https://doi.org/10.3390/e22111198).

**Read:** specific sections: 3.1-3.3; 5.1 AUF equation on printed page 16, visually checked. [Inspected source](https://pmc.ncbi.nlm.nih.gov/articles/PMC7712113/).

**What it does:** FASTENER defines AUF as the mean best score obtainable with at most k features for k=1..K; uses K=20. It also analyses size-sensitive genetic operations and tracks evaluations.

**Overlap with P2:** The name and mathematical form of P2 AUF are already published, not just a vaguely similar AUC.

**Critical limit:** The printed maximum does not explicitly specify the empty-feasible-set convention; do not attribute P2 zero-fill to it without checking code.


### Cattelani2024 — direct overlap

Luca Cattelani and Arindam Ghosh and Teemu J. Rintala and Vittorio Fortino (2024). A Comprehensive Evaluation Framework for Benchmarking Multi-Objective Feature Selection in Omics-Based Biomarker Discovery. *IEEE/ACM Transactions on Computational Biology and Bioinformatics* 21(6): 2432-2446. [doi:10.1109/TCBB.2024.3480150](https://doi.org/10.1109/TCBB.2024.3480150).

**Read:** abstract only; publisher/PubMed record. [Inspected source](https://pubmed.ncbi.nlm.nih.gov/39401114/).

**What it does:** Benchmarks seven MOFS methods on eight transcriptome datasets with external validation, reporting predictive performance, solution-set diversity/stability and a CV metric generalising HV.

**Overlap with P2:** Direct benchmarking/metric precedent at the level of solution sets as well as chosen subsets.

**Critical limit:** Its exact metric formula and missing-size treatment were not accessible; do not assume it matches AUF.


### Ishibuchi2015 — background overlap

Hisao Ishibuchi and Hiroyuki Masuda and Yuki Tanigaki and Yusuke Nojima (2015). Modified Distance Calculation in Generational Distance and Inverted Generational Distance. *Evolutionary Multi-Criterion Optimization (EMO 2015)* 9019: 110-125. [doi:10.1007/978-3-319-15892-1_8](https://doi.org/10.1007/978-3-319-15892-1_8).

**Read:** abstract only; publisher chapter record. [Inspected source](https://link.springer.com/chapter/10.1007/978-3-319-15892-1_8).

**What it does:** Introduces dominance-aware distance calculations underlying GD+ and IGD+ and explains Pareto-compliance issues in ordinary IGD.

**Overlap with P2:** Supports treating IGD/reference-set design as a substantive metric choice.

**Critical limit:** IGD+ does not itself solve an empirical reference front that omits small-size regions.


### Auger2012 — background overlap

Anne Auger and Johannes Bader and Dimo Brockhoff and Eckart Zitzler (2012). Hypervolume-based multiobjective optimization: Theoretical foundations and practical implications. *Theoretical Computer Science* 425: 75-103. [doi:10.1016/j.tcs.2011.03.012](https://doi.org/10.1016/j.tcs.2011.03.012).

**Read:** abstract only; publisher/author bibliographic record. [Inspected source](https://www.sciencedirect.com/science/article/pii/S0304397511002428).

**What it does:** Studies theoretical properties of hypervolume-based optimisation, including weighted HV and reference-point effects.

**Overlap with P2:** Background for explaining that area indicators integrate extent and objective quality.

**Critical limit:** The discrete AUF/HV identity in the [novelty assessment](related-work/NOVELTY.md) is an algebraic derivation for P2, not a theorem attributed to this paper.


## Duplicates, memoisation and wasted evaluation requests


### Jiao2024PRDH — direct overlap

Ruwang Jiao and Bing Xue and Mengjie Zhang (2024). Solving Multiobjective Feature Selection Problems in Classification via Problem Reformulation and Duplication Handling. *IEEE Transactions on Evolutionary Computation* 28(4): 846-860. [doi:10.1109/TEVC.2022.3215745](https://doi.org/10.1109/TEVC.2022.3215745).

**Read:** abstract only; publisher-indexed abstract and author publication record. [Inspected source](https://doi.org/10.1109/TEVC.2022.3215745).

**What it does:** PRDH reformulates FS with a performance constraint and handles duplication using both objective-space distribution and search-space similarity.

**Overlap with P2:** Direct prior art for duplicate-driven diversity loss and premature convergence in MOFS.

**Critical limit:** It is not evidence that exact-cardinality occupancy or unique-fit cache stagnation was measured. Full handling details were not available.


### Cattelani2022 — direct overlap

Luca Cattelani and Vittorio Fortino (2022). Improved NSGA-II algorithms for multi-objective biomarker discovery. *Bioinformatics* 38(Supplement_2): ii20-ii26. [doi:10.1093/bioinformatics/btac463](https://doi.org/10.1093/bioinformatics/btac463).

**Read:** abstract only; bounded-start detail corroborated in Cong2026 Section 3.5. [Inspected source](https://academic.oup.com/bioinformatics/article/38/Supplement_2/ii20/6702001).

**What it does:** NSGA2-CH and NSGA2-CHS improve biomarker search and compare internal/external predictive performance against NSGA-II and LASSO.

**Overlap with P2:** Clone handling and specialised mutation are close practical precedents. Cong et al. attribute their bounded 0..50 start to this work.

**Critical limit:** The exact start and operator implementation were not read in the original full text; that range attribution is secondary corroboration, not an independently verified algorithm reading.


### Li2020GADMS — direct overlap

An-Da Li and Bing Xue and Mengjie Zhang (2020). Multi-objective feature selection using hybridization of a genetic algorithm and direct multisearch for key quality characteristic selection. *Information Sciences* 523: 245-265. [doi:10.1016/j.ins.2020.03.032](https://doi.org/10.1016/j.ins.2020.03.032).

**Read:** specific sections: caching paragraph at end of 3.2; 4 settings; computation-time analysis. [Inspected source](https://andali89.github.io/homepage/pubs/2020_GADMS.pdf).

**What it does:** GADMS combines genetic search and direct multisearch. Explicit memoisation returns stored objective values for previously evaluated subsets; evaluation-count stopping is used.

**Overlap with P2:** Direct FS prior art for caching and its computational implications.

**Critical limit:** Caching avoids repeated fits but does not generate new solutions or solve stagnation. P2 must measure proposals as well as cache misses.


### Wang2023Dup — direct overlap

Peng Wang and Bing Xue and Jing Liang and Mengjie Zhang (2023). Differential Evolution With Duplication Analysis for Feature Selection in Classification. *IEEE Transactions on Cybernetics* 53(10): 6676-6689. [doi:10.1109/TCYB.2022.3213236](https://doi.org/10.1109/TCYB.2022.3213236).

**Read:** abstract only; publisher/PubMed record. [Inspected source](https://pubmed.ncbi.nlm.nih.gov/36279359/).

**What it does:** Uses niching DE, subset repair and diversity-sensitive selection to avoid duplicate feature subsets and recover different similarly accurate subsets.

**Overlap with P2:** Direct duplication-analysis precedent in evolutionary FS.

**Critical limit:** Alternative subsets with similar performance are distinct from exact same-genome cache hits and from objective-space ties.


## Surveys, benchmarking and reproducible reporting


### Jiao2024Survey — background overlap

Ruwang Jiao and Bach Hoai Nguyen and Bing Xue and Mengjie Zhang (2024). A Survey on Evolutionary Multiobjective Feature Selection in Classification: Approaches, Applications, and Challenges. *IEEE Transactions on Evolutionary Computation* 28(4): 1156-1176. [doi:10.1109/TEVC.2023.3292527](https://doi.org/10.1109/TEVC.2023.3292527).

**Read:** abstract only; publisher bibliographic record. [Inspected source](https://doi.org/10.1109/TEVC.2023.3292527).

**What it does:** MOFS-specific survey of approaches, applications, challenges and future directions.

**Overlap with P2:** Provides the main taxonomy and citation map; includes Nguyen as coauthor.

**Critical limit:** No claim is made here that the survey explicitly states P2 missing-size or cache-budget diagnosis: those sections were not read.


### Xue2016Survey — background overlap

Bing Xue and Mengjie Zhang and Will N. Browne and Xin Yao (2016). A Survey on Evolutionary Computation Approaches to Feature Selection. *IEEE Transactions on Evolutionary Computation* 20(4): 606-626. [doi:10.1109/TEVC.2015.2504420](https://doi.org/10.1109/TEVC.2015.2504420).

**Read:** specific sections: PSO initialisation discussion; VI-B computational cost, VI-H sample-size/selection bias. [Inspected source](https://homepages.ecs.vuw.ac.nz/~xuebing/Papers/BingsurveyPaper.pdf).

**What it does:** Broad EC-FS survey discusses computational expense, evaluation procedures, search mechanisms and feature-selection bias with small samples.

**Overlap with P2:** Direct support for reporting wrapper evaluation cost and protecting held-out evaluation.

**Critical limit:** It is not evidence for a new cardinality-coverage gap. The inspected version is an author manuscript.


### Nguyen2020Survey — background overlap

Bach Hoai Nguyen and Bing Xue and Mengjie Zhang (2020). A survey on swarm intelligence approaches to feature selection in data mining. *Swarm and Evolutionary Computation* 54: 100663. [doi:10.1016/j.swevo.2020.100663](https://doi.org/10.1016/j.swevo.2020.100663).

**Read:** abstract only; publisher record. [Inspected source](https://www.sciencedirect.com/science/article/pii/S2210650219303104).

**What it does:** Surveys swarm-intelligence FS with emphasis on representations, search mechanisms, strengths, limitations and future work.

**Overlap with P2:** Background showing that representations and update mechanisms are central to FS performance.

**Critical limit:** Broader than MOEAs; no specific missing-size or cache-accounting statement is attributed without full-text inspection.


### BartzBeielstein2020 — background overlap

Thomas Bartz-Beielstein and Carola Doerr and Daan van den Berg and Jakob Bossek and Sowmya Chandrasekaran and Tome Eftimov and Andreas Fischbach and Pascal Kerschke and William La Cava and Manuel López-Ibáñez and Katherine M. Malan and Jason H. Moore and Boris Naujoks and Patryk Orzechowski and Vanessa Volz and Markus Wagner and Thomas Weise (2020). Benchmarking in Optimization: Best Practice and Open Issues. *arXiv preprint arXiv:2007.03488*. [doi:10.48550/arXiv.2007.03488](https://doi.org/10.48550/arXiv.2007.03488).

**Read:** specific sections: 5.1 fixed budget/target and time; 9 reproducibility excerpts; arXiv v2. [Inspected source](https://arxiv.org/abs/2007.03488).

**What it does:** Benchmarking guidance distinguishes fixed-budget from fixed-target views and discusses evaluations, time, analysis and reproducibility.

**Overlap with P2:** Section 5.1 recommends reporting evaluations and CPU time and warns that generations alone obscure work.

**Critical limit:** General optimisation guidance; P2 cache-miss accounting is a domain-specific operationalisation.


### Beiranvand2017 — background overlap

Vahid Beiranvand and Warren Hare and Yves Lucet (2017). Best practices for comparing optimization algorithms. *Optimization and Engineering* 18(4): 815-848. [doi:10.1007/s11081-017-9366-1](https://doi.org/10.1007/s11081-017-9366-1).

**Read:** abstract only; publisher bibliographic record. [Inspected source](https://link.springer.com/article/10.1007/s11081-017-9366-1).

**What it does:** Reviews fair comparison of optimisation algorithms, benchmarking pitfalls and reporting methods.

**Overlap with P2:** Background for matching budgets, implementation conditions and reporting protocols.

**Critical limit:** No FS-specific conclusion is inferred from the abstract.


### Derrac2011 — background overlap

Joaquín Derrac and Salvador García and Daniel Molina and Francisco Herrera (2011). A practical tutorial on the use of nonparametric statistical tests as a methodology for comparing evolutionary and swarm intelligence algorithms. *Swarm and Evolutionary Computation* 1(1): 3-18. [doi:10.1016/j.swevo.2011.02.002](https://doi.org/10.1016/j.swevo.2011.02.002).

**Read:** abstract only; publisher record. [Inspected source](https://www.sciencedirect.com/science/article/pii/S2210650211000034).

**What it does:** Tutorial on nonparametric comparisons of evolutionary and swarm algorithms, including multiple-comparison procedures.

**Overlap with P2:** Background for paired experimental comparisons and multiplicity control.

**Critical limit:** Does not make five-seed outcomes conclusive; P2 should report effect sizes and uncertainty as well as tests.


### AlTashi2020 — background overlap

Qasem Al-Tashi and Said Jadid Abdulkadir and Helmi Md Rais and Seyedali Mirjalili and Hitham Alhussian (2020). Approaches to Multi-Objective Feature Selection: A Systematic Literature Review. *IEEE Access* 8: 125076-125096. [doi:10.1109/ACCESS.2020.3007291](https://doi.org/10.1109/ACCESS.2020.3007291).

**Read:** abstract only; publisher record. [Inspected source](https://ieeexplore.ieee.org/document/9133433/).

**What it does:** Systematic review of MOFS approaches, challenges and issues.

**Overlap with P2:** Additional MOFS taxonomy/context alongside Jiao and the broader Xue/Nguyen surveys.

**Critical limit:** No detailed assertion about size reach or missing-size conventions is supported by an abstract-only reading.


## Citation-tracing leads with incomplete substantive access


### Dehnad2025 — background overlap

Parastoo Dehnad and Azam Asilian Bidgoli and Shahryar Rahnamayan (2025). Validation-based Decision Making in Data-driven Evolutionary Computation: A Case Study in Multi-objective Feature Selection. *2025 IEEE Symposium on Computational Intelligence on Engineering/Cyber Physical Systems Companion (CIES Companion)*: 1-5. [doi:10.1109/CIESCompanion65073.2025.11010904](https://doi.org/10.1109/CIESCompanion65073.2025.11010904).

**Read:** metadata only: abstract and methods unverified. [Inspected source](https://doi.org/10.1109/CIESCompanion65073.2025.11010904).

**What it does:** Verified publication about validation-based decision making in MOFS; detailed method was not accessible.

**Overlap with P2:** Citation-tracing lead relevant to selecting a front member without using the test set.

**Critical limit:** Content overlap remains unverified; no novelty conclusion relies on this record.


### Rezazadeh2026 — partial overlap

Farzad Rezazadeh and Andreas Kroll (2026). Memory-Guided Search-Space Constrained NSGA-II-based Method for Stable Multi-Objective Feature Selection in Sparse Data. *2026 IEEE Congress on Evolutionary Computation (CEC)*: 1-8. [doi:10.1109/CEC69861.2026.11727296](https://doi.org/10.1109/CEC69861.2026.11727296).

**Read:** metadata only: abstract and methods unverified. [Inspected source](https://doi.org/10.1109/CEC69861.2026.11727296).

**What it does:** Verified memory-guided/search-space-constrained NSGA-II FS publication; method content unverified.

**Overlap with P2:** Forward-citation lead from Kropp2022; potentially relevant to sparse-data search and stability.

**Critical limit:** Memory guidance is not assumed to mean memoisation; further reading is required.


### Huang2026 — partial overlap

Wanting Huang and Lixin Cui and Lu Bai (2026). A Cluster and Historical-Frequency Guided Evolutionary Algorithm for High-dimensional Multi-Objective Feature Selection. *2026 International Annual Conference on Complex Systems and Intelligent Science (CSIS-IAC)*: 546-553. [doi:10.1109/CSIS-IAC70275.2026.11585066](https://doi.org/10.1109/CSIS-IAC70275.2026.11585066).

**Read:** abstract snippet only: publisher author-profile record; full abstract unverified. [Inspected source](https://doi.org/10.1109/CSIS-IAC70275.2026.11585066).

**What it does:** CHFEA is presented as a cluster- and historical-frequency-guided MOFS method for high-dimensional search.

**Overlap with P2:** Forward-citation lead from Li2025; related general exploration/diversity design.

**Critical limit:** No detailed cardinality, cache or metric claim can be established from the snippet.


## Synthesis across topics

### Initialisation: the general effect is established; its distribution matters

[Deniz2019](https://doi.org/10.1016/j.eswa.2019.06.063) already includes a small random start; [Deniz2022](https://doi.org/10.1109/IJCNN55064.2022.9892123) explicitly allocates counts across bands. Bitwise Bernoulli, cardinality-uniform and size-stratified sampling should not be treated as synonyms. The 1..30 start is an existing count-sampling procedure with a chosen range. Full-range uniform counts have broad support but can still place few individuals at small absolute sizes when d is large. P2's useful question is the resulting access profile under finite populations and fits, not whether initialisation can matter at all.

### Operators: expected balance, size preservation and active search differ

[Oh2004](https://doi.org/10.1109/TPAMI.2004.105) verifies the old balanced-mutation formula. [Li2025](https://doi.org/10.1016/j.ejor.2024.12.036) explicitly states its expected-size property. SparseEA and successors couple sparse generation with sparse variation; substituting only their starts is a component ablation, not a comparison with the complete methods. P2 can test whether very low sparse-child activity causes cache-heavy stagnation, but must separate that effect from mutation drift and selection.

### Metrics: useful utility is not a pure conditional-quality measure

P2 AUF is the established at-most-k envelope utility. No exact-k point is required if a smaller subset provides a score. Use NA for unmeasured exact-k quality, zero only for the declared empty feasible region of the utility, and avoid inventing linear interpolation. Whole-front HV has its own reference-point and normalisation dependence; ordinary “set coverage” in this literature usually denotes dominance, not occupancy along feature count.

For IGD, FS rarely has a known true front. Li2025 uses an estimated nondominated union, and Cong2026 also uses a pooled empirical reference. Such a reference can underrepresent small sizes that no compared method finds. State how it is constructed, use common scaling, show sensitivity to its size-axis density and optionally report IGD+. None of these indicators replaces explicit reach and exact-k curves.

### Duplicates and budgets: memoisation and diversity are separate

[Jiao2024PRDH](https://doi.org/10.1109/TEVC.2022.3215745) and [Wang2023Dup](https://doi.org/10.1109/TCYB.2022.3213236) make duplication a search issue. [Li2020GADMS](https://doi.org/10.1016/j.ins.2020.03.032) makes caching a computational issue. They overlap but are not identical: a cache saves fits, while duplicate handling changes the search. Equal unique fits does not imply equal objective requests, generations or time. Report them together and charge informed-start evaluations.

### Reporting: support from surveys is specific, not universal

The inspected Xue2016Survey sections explicitly support computational-cost and selection-bias concerns. Jiao2024Survey, Nguyen2020Survey and AlTashi2020 were read at abstract level: they support taxonomy and scope, not a claim that they expressly diagnose P2's missing-size convention. General benchmarking guidance supports transparent evaluation/time reporting. The combined evidence justifies careful measurement; it does not prove a previously unnoticed field-wide methodological failure.

## Access limits that matter before submission

Full implementations of SPS/VSSPS, MOEA-ISa, PPI/GPR, PRDH and NSGA2-CH/CHS should be read before those methods are reimplemented. In particular, Cattelani2022's bounded-start details here are corroborated through Cong2026, not checked in the original body. The 2024 paper's citation to an Ebrahimi thesis did not yield a verified thesis record; no independent thesis entry or invention-date claim is supplied.

The three final leads have verified identities but incomplete substantive text. They are retained for follow-up and do not carry the novelty conclusion. A targeted, access-limited search cannot establish that no other direct study exists. Recheck citations and new publications before submission.
