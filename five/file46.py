#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MeCab

def extract_compound_noun():
	me = MeCab.Tagger("mecabrc")
	noun_list = []

	for line in open(sys.argv[1]):
		noun_flag = 0
		temp_noun_list = []
		result = me.parse(line.strip())
		#morphには一文のそれぞれの単語のmecabの解析結果が代入されています
		for morph in result.split("\n"):
			if morph == "EOS":
				break
			elif morph.split("\t")[1].split(",")[0] == "名詞":
				noun_flag = 1
				temp_noun_list.append(morph.split("\t")[0])
			elif noun_flag == 1 and morph.split("\t")[1].split(",")[0] != "名詞":
				noun_flag = 0
				compound_noun = ""
				for temp_noun in temp_noun_list:
					compound_noun = "%s%s" % (compound_noun,temp_noun)
				temp_noun_list = []
				noun_list.append(compound_noun)

	return noun_list

if __name__ == "__main__":
	for noun in extract_compound_noun():
		print noun