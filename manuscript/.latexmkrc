# Build settings shared by latexmk on the command line and in VS Code (LaTeX Workshop).
$pdf_mode = 1;
$out_dir = 'build';
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
$bibtex_use = 2;
