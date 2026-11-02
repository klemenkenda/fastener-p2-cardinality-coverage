# Figure style guide

Rules for every figure in the P2 manuscript (ComSIS). The figures are made by [`figures/make_figures.py`](figures/make_figures.py) from the tables in [`../evidence/`](../evidence/); the script holds every value below in one place (`STYLE`, `CONFIG`, `GRIDS`). Change a rule there and here together.

## Purpose

A figure shows one finding that the text states. The finding goes in the caption's first sentence. Statistics, test results and registration labels go in the text or a table, never inside the figure.

## Size and format

- **Width:** the ComSIS text block is 125 mm wide. Full-width figures are 125 mm; a figure is never wider. Half-width figures (61 mm) are allowed for a single small panel.
- **Height:** at most 90 mm, so a figure and its caption leave room for text on the page.
- **Format:** vector PDF with embedded fonts (`pdf.fonttype = 42`). Raster only for dense images, at 600 dpi.
- **Include at natural size:** `\includegraphics{figures/name.pdf}` with no `width=` scaling, so that font sizes stay as set here.

## Type

- **Typeface:** STIX (a Times design, matching the ComSIS body text), with STIX mathematics.
- **Sizes:** 8 pt for axis labels, panel titles and legends; 7 pt for tick labels. Nothing smaller than 7 pt.
- **Case:** sentence case for axis labels and panel titles ("Share of runs that reach ten features"). Units in parentheses.
- **Numbers:** plain numbers on log axes (10, 100, 1,000, 10,000), with thousands separators. No scientific notation unless the range demands it.

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

Colour identifies the configuration, and it is the same in every figure. The three colours are the first three slots of the validated reference palette, which pass all-pairs colour-vision checks on white (worst CVD ΔE 9.2, worst normal-vision ΔE 24.0; run on 2 November 2026 with the dataviz validator, `--pairs all --surface #ffffff`).

| Configuration | Colour | Marker |
|---|---|---|
| OBL start | blue `#2a78d6` | circle |
| Sparse start | orange `#eb6834` | square |
| NSGAII-MIIP | aqua `#1baf7a` | triangle |

- **All figures are in colour.** The paper is read in colour; no greyscale version is made. Lines are solid for every configuration.
- **Markers as a second cue.** Aqua has 2.8:1 contrast on white, below 3:1, so each configuration keeps its own marker shape, and every figure with more than one configuration has a legend.
- **Differences take the colour of the first configuration.** A difference "a minus b" drawn as a single series is in the colour of a: sparse minus OBL in orange, NSGAII-MIIP minus OBL in aqua.
- **Every other class has its own colour.** When a figure separates classes that are not configurations (the reach and quality parts of a difference, variants of an analysis, classifiers), each class gets its own colour and marker, taken in this order:

  | Order | Colour | Marker |
  |---|---|---|
  | 1 | violet `#6250d6` | circle |
  | 2 | yellow `#eda100` | square |
  | 3 | magenta `#e87ba4` | diamond |
  | 4 | green `#008300` | triangle down |

  These four pass all-pairs colour-vision checks on white as a set (worst CVD ΔE 16.2, worst normal-vision ΔE 19.6). They are never mixed with the configuration colours in one figure. Yellow (2.2:1) and magenta (2.7:1) are below 3:1 contrast, so the marker and a legend are always present.
- **Pilot starts.** The uniform start is violet with a diamond and the log-uniform start yellow with a down-triangle, the first two class colours. No set of four start colours passes the all-pairs check (violet and blue fail it), so a figure that shows all four starts uses one panel per start, and the uniform and log-uniform starts never share a panel with the OBL start. In the pilot, balanced mutation and the forced flip take the next two class colours, magenta and green.
- **Summaries in ink.** A mean or median drawn over the points is a near-black bar.
- **Groups of runs** (classifiers) are shown as panels or along the axis when the figure compares configurations; they take class colours only when the classifiers themselves are compared.

## Ink and marks

| Role | Value |
|---|---|
| Text, ticks, main neutral marks | `#0b0b0b` |
| Secondary text and marks | `#52514e` |
| Muted (reference curves) | `#898781` |
| Grid lines | `#e1e0d9`, 0.4 pt, solid, behind the data |
| Axis lines | `#52514e`, 0.6 pt, left and bottom only |
| Zero or baseline | `#52514e`, 0.6 pt, solid |

- Data lines 1.0 pt. Markers 3.5 pt, with a 0.4 pt white edge where they overlap.
- Reference curves (analytic predictions) are muted grey, 0.8 pt, and labelled directly on the curve.
- No dashed grid lines, no frames around legends, no shadows, no 3-D.
- Overlapping points are offset slightly by configuration, not drawn with transparency alone.

## Panels

- **Small multiples** share axes and scales. A panel title names the group in plain words ("Random forest"), with no statistics.
- **Panel order:** designed experiment first, then decision tree, random forest, LightGBM, left to right and top to bottom.
- **Panel letters** (a), (b), … are used only when the caption refers to panels with different content. Facets of one quantity are named by their titles.

## Legends and labels

- One legend per figure, above the panels, without a frame. Direct labels are preferred when there are at most three series and space allows.
- No numbers printed on data points.
- Axis labels say what is measured ("Features $d$", "Share of the fit budget"), not how it was computed.

## Captions

Written in LaTeX, not in the figure. First sentence: the finding. Then what each mark shows, which split the scores come from, and what is left out. Keep the caption under 80 words.

## Checklist before including a figure

1. Width at most 125 mm and fonts at least 7 pt at natural size.
2. Only the paper's names; no experiment identifiers, file names or p-values.
3. Configuration colours and markers as in the table above; differences in the colour of the first configuration.
4. Legend present for two or more configurations.
5. Grid behind the data, solid and light; axis lines left and bottom.
6. Rendered and looked at: no overlapping labels, nothing clipped.
