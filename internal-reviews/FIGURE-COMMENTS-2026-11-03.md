# Comments on the P2 figures (2026-11-03)

Comments on the figures of the P2 manuscript, received in Slovenian and translated into English. Figure numbers are those of the manuscript at commit 99e209b (Fig. 1 reach and quality parts, 2 reach against $d$, 3 time to reach, 4 large end, 5 three arms, 8 pilot starts, 10 forced flip). The response is in the last section.

## Comments

A few ideas for decluttering these visualizations:

- Where points lie in the same place (Fig. 2 above all is a problem), I would try a little transparency, so that one can see how many lie on top of each other. And without the white edge around them.
- Text hierarchy: it is the same throughout (only the annotations differ). Perhaps the titles above the individual plots could be a bit stronger than the legend labels. Maybe also make the labels smaller, so that the difference is clearer.
- I do not quite like the legend labels. Now they are at the top, in the centre, in every figure. Could you try putting them on the left, inside the first plot (if possible), and at a lower level of the text hierarchy?

Smaller things:

- Fig. 1: the caption says "pair of points", so the black and grey points are connected to each other. If so, it might make sense to emphasize that.
- Fig. 2: great that you have the annotation inside! My first idea would be to make a matrix of plots, so that they separate more clearly. But perhaps it will be enough to make the points somewhat transparent.
- Fig. 3: is NSGAII-MIIP dashed because you wanted to emphasize it most? It sticks out a bit.
- Figs. 4a and 5: great that you show all the points, just make them a little transparent. Statistics of the comparisons?
- Figs. 8 and 10: the (a), (b), … are centre-aligned. I would put them on the left. Because the legends are also aligned at the top centre, a bit too much is going on at the top.

## Response

All changes are in `manuscript/figures/make_figures.py` and recorded as rules in `manuscript/FIGURE-STYLE.md`.

- **Transparency, no white edge.** Points are drawn at alpha 0.55 without an edge, so stacked points build up to a darker spot; neutral tones at 0.8, because lightness is what tells them apart. The offsets by configuration stay. Fig. 2 stays a 2 × 2 grid; with transparency the stacks at 0 and 1 are readable.
- **Text hierarchy.** Panel titles are 10 pt bold; axis labels 10 pt regular; legends 9 pt in the secondary grey. Tick labels stay at 9 pt, the floor the style guide sets from the ComSIS lettering rule.
- **Legends.** Moved from above the panels into a panel, one entry per row: on the left of the first panel where the data leave room (Figs. 3, 6, 8, 10), otherwise in a free corner (Fig. 1: the LightGBM panel; Fig. 2: right of the first panel; Fig. 4: panel b, the only one with configurations; appendix figure: panel b).
- **Fig. 1.** A thin grey line joins the reach and quality parts of each dataset; the caption says "each pair of points joined by a line".
- **Fig. 3.** NSGAII-MIIP is solid like the other lines; the dash was meant only to separate it from the sparse start, which has the same lightness, and the curves are apart anyway. The caption no longer mentions it.
- **Figs. 4a and 5.** Each mean bar now carries its 95% percentile-bootstrap interval as a thin vertical line; the captions say so. Tests and p-values stay in the text, as the style guide asks.
- **Figs. 8 and 10, and all others.** Panel titles, with their letters, are left-aligned.
