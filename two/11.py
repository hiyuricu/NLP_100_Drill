#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import re

#perfect_sentence_candidate_dicとabbreviation_scoreの辞書の構成として、keyにはstring,valueにはlistが入るように設計してある
perfect_sentence_candidate_dic = {}
abbreviation_score = {}

#一文ある毎に改行されているテキストが引数にあると想定している
def main(read_file):
    wf = open('11.txt',"w")
    for line in open(read_file,"r"):
        line = line.strip()
        if re.search('拡散希望', line):
            wf.write("%s\n" % line)
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])
