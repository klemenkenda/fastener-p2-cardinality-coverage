Klemen Kenda
Jožef Stefan Institute
Jamova cesta 39, 1000 Ljubljana, Slovenia
klemen.kenda@ijs.si

4 November 2026

The Editor
*Computer Science and Information Systems (ComSIS)*

Dear Editor,

I am submitting the manuscript **"Cardinality Coverage in Evolutionary Feature Selection: A Budget-Aware Study of Initialization and Search Operators"** for consideration as a research paper in *Computer Science and Information Systems*.

Multi-objective evolutionary feature selection is often compared at small feature limits, for example by the area under the front (AUF) at ten features. Such a score mixes two things: whether a method returns any subset within the limit, and how well its subsets predict. The manuscript separates the two for three NSGA-II configurations that share the operators of NSGAII-MIIP: its opposition-based start, a sparse start, and our implementation of the complete method. The comparison covers 46 datasets with 16 to 192,000 features and up to three classifiers. It is followed by a registered pilot on four datasets and a confirmatory test on seven datasets that had not been used before.

The main findings are:

- At a limit of ten features, reach accounts for 98 to 100 percent of the AUF difference between the two starts. At sizes both starts reach, the mean test F1 difference lies within 0.02 under two classifiers and is inconclusive under the third.
- At the benchmark budgets, the opposition-based start never reaches ten features beyond 512 features. The number of model fits it needs grows as about d^1.7 with the number of features d. A prediction fitted on the pilot and registered before the runs held within a factor of two on all seven new datasets.
- The sparse start pays for its reach among large subsets, and the mutual-information improvement phase of NSGAII-MIIP raises reach only slightly.
- From these results, the paper derives a short list of quantities to report alongside AUF: reach, scores at matched sizes, the budget, and computing cost.

The paper does not propose a new algorithm. Its contribution is to how comparisons of evolutionary feature selection are read and reported, which I believe fits the journal's readership in evolutionary computation and machine learning. The claims are limited to the tested configurations, budgets, and classifiers, and the paper states which analyses are exploratory and which are confirmatory.

I confirm that the manuscript is original, has not been published before, and is not under consideration elsewhere. The code, run logs, derived tables, and a reproduction guide will be made publicly available. The use of generative AI tools, and its purpose, is disclosed in the acknowledgments as the journal's policy requires.

For double-anonymous review, I attach an anonymized manuscript and supplementary material, together with the non-anonymous versions.

Thank you for considering this submission.

Yours sincerely,

Klemen Kenda
Jožef Stefan Institute
