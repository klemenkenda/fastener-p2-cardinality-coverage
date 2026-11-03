# Figure style guide

Rules for every figure in the P2 manuscript (ComSIS). The figures are made by [`figures/make_figures.py`](figures/make_figures.py) from the tables in [`../evidence/`](../evidence/); the script holds every value below in one place (`STYLE`, `MARK`, `CONFIG`, `LINESTYLE`, `NEUTRAL`, `PILOT_START`, `GRIDS`, `ANNOT`). Change a rule there and here together.

## Purpose

A figure shows one finding that the text states. The finding goes in the caption's first sentence. Statistics, test results and registration labels go in the text or a table, never inside the figure.

## Size and format

- **Width:** the ComSIS text block is 125 mm wide. Full-width figures are 125 mm; a figure is never wider. Half-width figures (61 mm) are allowed for a single small panel.
- **Height:** at most 90 mm, so a figure and its caption leave room for text on the page.
- **Format:** vector PDF with embedded fonts (`pdf.fonttype = 42`). Raster only for dense images, at 600 dpi.
- **Include at natural size:** `\includegraphics{figures/name.pdf}` with no `width=` scaling, so that font sizes stay as set here.

## Type

- **Typeface:** STIX (a Times design, matching the ComSIS body text), with STIX mathematics.
- **Sizes:** 10 pt for axis labels, panel titles and legends, as the ComSIS instructions ask (lettering about 2 mm high, 10-point type); 9 pt for tick labels and annotations. Nothing smaller than 9 pt.
- **Fitting the text:** a larger size is made to fit by layout, not by shrinking: one shared axis label per grid of panels (`grid_labels`), short or two-line category names with the full names in the caption, fewer ticks, and a legend in two rows when one row is wider than the text block.
- **Case:** sentence case for axis labels and panel titles ("Share of runs that reach ten features"). Units in parentheses.
- **Numbers:** plain numbers on log axes, with thousands written as k (10, 100, 1k, 10k, 100k), so that four decades fit a half-width panel. No scientific notation unless the range demands it.

## Names

Use the paper's names, never internal identifiers.

| In the data | In figures and text |
|---|---|
| `nsga2` | OBL start |
| `nsga2_sparse` | Sparse start |
| `nsgaii_miip` | NSGAII-MIIP |
| `H1-E02` | Decision tree (designed) |
| `H5H6-E01` | Decision tree |
| `H5H6-E02` | Random forest |
| `H5H6-E03` | LightGBM |

| `p2_uniform` | Uniform start |
| `p2_loguniform` | Log-uniform start |
| `_min1` suffix | Forced flip (the other arms use balanced mutation) |
| `p2_obl_b3`, `p2_obl_b10` | OBL start at 3× and 10× the budget |

`H1-E02` is the designed experiment on 8 datasets; the other three are the benchmark groups on 39 datasets. The `p2_` arms are the pilot (H14-E02) on four datasets.

## Colour and encoding

One mark and few hues. Colour is reserved for configurations and is the same in every figure; everything that is not a configuration is neutral grey.

| Configuration | Colour |
|---|---|
| OBL start | blue `#285fa8` |
| Sparse start | orange `#e07434` |
| NSGAII-MIIP | teal `#2a9d8f` |
| Uniform start (pilot) | plum `#7e57a6` |
| Log-uniform start (pilot) | ochre `#b5891c` |

- **One marker shape.** Every point is a filled circle, 3.6 pt, with a 0.5 pt white edge. Shape never encodes anything; colour (and, for neutrals, lightness) does.
- **Checked for colour vision.** The three main colours pass all-pairs checks on white (CIEDE2000 under Machado full-severity simulation: worst CVD ΔE 18.8, worst normal-vision ΔE 35.8), and each has at least 3:1 contrast on white. Plum and ochre pass as a pair (worst CVD ΔE 22.2). No five hues pass together, so the uniform and log-uniform starts never share a panel with the OBL, sparse or NSGAII-MIIP configurations; a figure showing all four starts uses one titled panel per start.
- **All figures are in colour.** The paper is read in colour; no greyscale version is made.
- **Lightness as a second cue.** In CIELAB, OBL blue has L* 40, sparse orange 60 and NSGAII-MIIP teal 59. Sparse and NSGAII-MIIP thus differ only in hue. Where they share a panel, another cue separates them: points are offset by configuration, and the NSGAII-MIIP line is dashed (`LINESTYLE`). All other lines are solid. Plum (L* 44) and ochre (L* 60) differ in lightness.
- **Differences take the colour of the first configuration.** A difference "a minus b" drawn as a single series is in the colour of a: sparse minus OBL in orange, NSGAII-MIIP minus OBL in teal.
- **Non-configuration classes are neutral.** When a figure separates classes that are not configurations (the reach and quality parts of a difference, variants of an analysis, classifiers, mutation operators), they are drawn in neutral tones that differ in lightness, so they survive any colour-vision deficiency:

  | Order | Tone |
  |---|---|
  | 1 | dark slate `#2f3b4c` |
  | 2 | light grey `#a7aeb8` |
  | 3 (only with three classes) | mid grey `#6e7783` |

  With three classes they run dark, mid, light. In the sensitivity figure the registered result keeps its configuration colour (orange, sparse minus OBL) and the three variants take the neutral tones.
- **Summaries in ink.** A mean or median drawn over the points is a near-black bar, 1.4 pt.
- **Groups of runs** (classifiers) are shown as panels or along an axis when the figure compares configurations; they take neutral tones only when the classifiers themselves are compared.

## Ink and marks

| Role | Value |
|---|---|
| Text, tick labels, summary bars | `#1a1d23` |
| Secondary text, ticks and marks | `#5a606b` |
| Muted (reference curves) | `#9aa0a8` |
| Grid lines | `#e9ebee`, 0.4 pt, solid, behind the data |
| Axis lines | `#5a606b`, 0.6 pt, left and bottom only |
| Zero or baseline | `#5a606b`, 0.6 pt, solid |

- Data lines 1.2 pt. Markers 3.6 pt filled circles with a 0.5 pt white edge (3.0 pt in dense three-panel strips).
- Categorical axes (groups of runs, starts, datasets) have no tick marks and no grid along the category; when the names are long, the categories run down the y axis, with labels of at most two lines.
- Reference curves (analytic predictions) are muted grey, 0.8 pt, and labelled directly on the curve.
- No dashed grid lines, no frames around legends, no shadows, no 3-D.
- Overlapping points are offset slightly by configuration, not drawn with transparency alone.

## Panels

- **Small multiples** share axes and scales. A panel title names the group in plain words ("Random forest"), with no statistics.
- **Panel order:** designed experiment first, then decision tree, random forest, LightGBM, left to right and top to bottom.
- **Panel letters** (a), (b), … are used only when the caption refers to panels with different content. Facets of one quantity are named by their titles.

## Legends and labels

- One legend per figure, above the panels, without a frame. Point figures show a circle per entry, line figures a short line; never both. Direct labels are preferred when there are at most three series and space allows.
- No numbers printed on data points.
- Axis labels say what is measured ("Features $d$", "Share of the fit budget"), not how it was computed.

## Captions

Written in LaTeX, not in the figure. First sentence: the finding. Then what each mark shows, which split the scores come from, and what is left out. Keep the caption under 80 words.

## Checklist before including a figure

1. Width at most 125 mm and fonts at least 9 pt (10 pt for labels, titles and legends) at natural size.
2. Only the paper's names; no experiment identifiers, file names or p-values.
3. Configuration colours as in the table above, circles only, other classes in neutral tones; differences in the colour of the first configuration.
4. Legend present for two or more configurations.
5. Grid behind the data, solid and light; axis lines left and bottom.
6. Rendered and looked at: no overlapping labels, nothing clipped.
