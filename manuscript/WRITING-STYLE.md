# Writing style guide

Working guide for writing in Klemen Kenda's voice, based on his stated preferences. Refine it as he edits the manuscript.

## Main principle

Write so that the reader can understand the idea on the first reading. Use familiar words whenever they express the meaning accurately. When a technical term is necessary, explain it before relying on it. Scientific precision comes from clear definitions, sound reasoning, and evidence.

## Voice

Use the voice of an experienced researcher explaining his work to a colleague: calm, direct, practical, and respectful of the reader's time. Let the reasoning carry the argument. Avoid promotional language and claims of importance that the results do not support.

Write natural English for an international audience. The author's Slovenian background should not be imitated through awkward phrasing or deliberate grammatical errors. Preserve his preference for straightforward explanations. Use the manuscript's existing American spelling consistently, for example, “initialization” and “analyze.” Preserve original spelling in publication titles.

Use “we” for the authors' choices and actions: “We compare four initialization strategies.” Name the method when describing its behavior: “The algorithm selects a subset size.” Use passive voice when the actor does not matter.

## Words and definitions

- Prefer concrete verbs: “use,” “show,” “compare,” “measure,” and “explain.” Avoid inflated substitutes such as “utilize” and “elucidate.”
- Introduce an idea in ordinary language, then give its technical name if that name will be useful later.
- Define abbreviations at first use. Avoid an abbreviation used only once or twice unless readers need it to identify an established method.
- Keep technical terms that make a distinction precise. Define them rather than replacing them with a simpler but inaccurate expression.
- Use the same term for the same quantity throughout the paper. Do not alternate between “accuracy,” “score,” and “predictive quality” as if they were interchangeable.
- Avoid long chains of nouns and invented labels. “How mutation changes subset size” is easier to follow than “mutation-induced cardinality dynamics.”

For this paper, explain “cardinality” as the number of selected features. Define what “coverage” measures each time a different kind of coverage is introduced. Distinguish a subset with exactly ten features from one with at most ten features. Explain a cache as stored evaluation results that can be reused when the same subset occurs again.

## Sentences and paragraphs

Give each sentence a clear main point. Split it when definitions, qualifications, or multiple conclusions make it difficult to follow. Vary sentence length naturally; a sequence of very short sentences can also make an argument harder to read.

Develop one main idea per paragraph. State the point early, explain why it holds, and give the evidence or example needed to understand it. Connect the next paragraph to that reasoning. Use transitions such as “however” or “therefore” only when they express an actual relationship.

Use lists for contributions, procedures, or parallel comparisons. Use connected prose for explanations. Avoid turning every distinction into a numbered list or a separate heading.

Organize related work by ideas, with one main idea per paragraph. Bring relevant studies together to explain that idea and its connection to the paper. Avoid a sequence of separate summaries of individual publications.

## Claims and evidence

State what was measured, under which conditions, and what follows from it. Describe limitations where they affect the conclusion. Prefer a precise boundary to repeated vague qualifications such as “may potentially suggest.”

Keep these distinctions explicit:

- A result from the completed experiment versus a question for a planned experiment.
- An observed association versus an established cause.
- A mathematical consequence of stated assumptions versus an empirical finding.
- A result for the tested configuration versus a claim about the whole class of algorithms.
- An existing method or property versus the contribution of this paper.

Use “shows” for a directly supported observation and “suggests” for an interpretation that still needs testing. Reserve “proves” for a mathematical proof. Avoid “first,” “novel,” “superior,” and “state of the art” unless the paper supplies the evidence needed for that exact claim.

Cite a source where its method, result, or idea is introduced. Explain what the source contributes to the argument. A group of citations does not replace that explanation.

## Equations and results

Explain the question an equation answers before presenting it. Define every symbol and state the assumptions. After the equation, explain its practical meaning. Include a numerical example when it helps the reader see the scale of an effect.

When reporting a comparison, name the metric and the conditions. “Better” by itself is incomplete. Report the size of the difference and its uncertainty when available. Explain what a zero, a missing value, and a failed run mean; they can represent different situations.

## Examples of the intended style

| Dense wording | Preferred wording |
|---|---|
| We provide a diagnostic treatment of their interaction. | We examine how initialization and mutation together affect the subset sizes reached during search. |
| Cardinality preservation coexists with low variation activity. | The mutation keeps the expected number of selected features unchanged, but it may change very few bits. |
| The method exhibits superior performance. | The method has a higher AUF under the ten-feature limit in the tested configuration. |
| The proposed framework facilitates the interpretation of empirical outcomes. | These measures help explain why the methods obtain different scores. |

An example paragraph:

> A method can receive a low score because it finds poor subsets, because it finds no subset within the size limit, or because both occur. These cases require different explanations. We therefore report whether a method finds a subset within the limit and how well the available subsets predict. We also distinguish subsets evaluated during the search from those kept in the final output.

## Before accepting a draft

Read it as a researcher who knows feature selection but has not followed this project. Check whether each necessary term is explained, each claim has support, and each paragraph advances the argument. Replace phrases that sound impressive but add little meaning. Keep the technical detail that the reader needs to assess or reproduce the work.

When choosing between two equally accurate versions, prefer the one that is easier to understand.
