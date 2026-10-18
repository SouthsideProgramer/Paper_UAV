#!/usr/bin/env bash
# Regenerate the tables from the result files, then build main.pdf.
cd "$(dirname "$0")"
/home/aclab_pc/miniconda3/envs/adas-observer/bin/python gen_tables.py && cp ../Task_F_Fusion/paper_figs/fig_*.pdf figs/ \
  && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1 && echo "built main.pdf ($(pdfinfo main.pdf | grep Pages))"
