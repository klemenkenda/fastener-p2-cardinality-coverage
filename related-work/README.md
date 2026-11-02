# P2 related-work review

Prepared in English on **2 November 2026** for the planned paper *Cardinality Coverage in Evolutionary Feature Selection*.

## Start here

Read NOVELTY.md first for the assessment and required experimental controls, then ../RELATED-WORK.md for the source-level evidence. The conclusion is conditional: a controlled diagnostic study may be worthwhile at J.UCS level, but the initialiser, balanced mutation and AUF formula are established, and recent work directly overlaps the finite-budget access question.

## Contents

| File | Contents |
|---|---|
| ../RELATED-WORK.md | Verified core list and 42 annotated references grouped by topic, with source links, reading depth and overlap limits. |
| NOVELTY.md | Claim revisions, reach/quality definitions, AUF/HV relationship, pilot controls, budget/reporting requirements and review risks. |
| COMPARISON.csv | One row per catalogue paper; UTF-8 with BOM, quoted CSV fields and the requested columns. |
| ../references.bib | Matching BibTeX entries; verified bibliographic fields, UTF-8 names, and explicit notes for unverified content/DOI fields. |
| SEARCH-LOG.md | Queries, databases, counts, access limits, citation tracing and returned-title audit inventory. |
| OUTLINE.md | Five-paragraph related-work outline targeting about 1-1.5 manuscript pages. |
| CORRECTIONS.md | Reference corrections/completions and actual DOI-routing/access results for all supplied items and leads. |
| pdfs/ | Six unchanged CC BY 4.0 publisher PDFs. |
| pdfs/LICENCES.md | Attribution, exact source URL, version/permission evidence and SHA-256 for each PDF. |

## How the search was done

Live, adaptive web search covered initialisation, variation, cardinality/front evaluation, duplicates and computational accounting from about 2010 to the review date, plus the requested 2004 mutation source. Publisher records and Crossref verified metadata; public manuscripts/repository text supplied specific sections; Semantic Scholar supplied reference/citation edges for Kropp2022, Miyandoab2024 and Li2025. SpringerLink, ScienceDirect, IEEE Xplore, arXiv and DBLP were used. Google Scholar was attempted but unavailable. This limitation is recorded, not represented as a successful native Scholar search.

There are 100 logged web queries; 917 later-batch returned records (729 distinct raw URLs) underwent title/source triage. These are not total indexed database hits or unique studies. The initial batch's exact result count was not preserved. The catalogue contains 12 supplied papers/leads plus 30 additions, including three provisional content-access leads. This is a targeted critical review, not an exhaustive systematic review.

Reading depth: 16 records have specific-section reading, 23 have abstract-only reading, and 3 have metadata-only or incomplete-abstract access. **No full-text-read label is claimed.** Some full PDFs were available, but only the recorded sections were substantively inspected. H1-E02 outcomes are author-supplied and were not reproduced; the proposed pilot remains unrun.

## Comparison-table conventions

Topic columns use D=direct, P=partial, B=background, -=not established in the inspected material, ?=unverified. A dash is not proof of absence from a full paper. Overall overlap is direct/partial/background and concerns a P2 component, not identity with the complete proposed paper. Group-F content judgements remain provisional.

DOIs use verified publisher/registry values. Journal issue years are used where available; an earlier online date or a year embedded in a DOI is not substituted for the issue year. Qian2015 has no verified DOI in the inspected official record; the field is empty and the BibTeX note says so. Page numbers/article numbers appear only when verified. UTF-8 BibTeX is best handled by a Unicode-capable bibliography workflow.

## PDF policy

Only CC BY 4.0 PDFs whose exact files and licence statements were checked are included. Other papers are links only, including arXiv's non-exclusive version of Miyandoab2024 and the CC BY-NC-ND AIMEA article. Public availability alone was not treated as permission. No shadow libraries were used. The review text consists of original critical summaries and analysis, not reproduced article bodies.

## Practical interpretation

The main new literature risks are Cong2026 (finite-budget access), Koprivec2020 (exact AUF) and Li2026CORAL (size-stratified maintenance), alongside the known Miyandoab2024 overlap and its 2026 extension. Suggested controls are recommendations, not implemented algorithms or completed experiments. Recheck recent citations and obtain the full specifications of any abstract-only method before reimplementation or submission.
