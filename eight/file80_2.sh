#-*-coding:utf-8-*-
cat feature_for_classias.txt | classias-tag -s t -m model.txt -r > 80_output_classias.txt
python file80_compare.py 80_output_classias.txt feature_for_classias.txt
