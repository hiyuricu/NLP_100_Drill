#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MeCab
import marshal

def extract_noun_and_noun():
	me = MeCab.Tagger("mecabrc")

	for line in open(sys.argv[1]):
		roop_number = 0
		temp_surface_list = []
		temp_pos_list = []
		result = me.parse(line.strip())
		#morphには一文のそれぞれの単語のmecabの解析結果が代入されています
		for morph in result.split("\n"):
			if morph == "EOS":
				break
			roop_number += 1
			temp_surface_list.append(morph.split("\t")[0])
			temp_pos_list.append(morph.split("\t")[1].split(",")[0])
			if roop_number >= 3 and temp_pos_list[roop_number - 3] == "名詞" and temp_surface_list[roop_number - 2] == "の" and temp_pos_list[roop_number - 1] == "名詞":
				print "%s%s%s" % (temp_surface_list[roop_number - 3], temp_surface_list[roop_number - 2], temp_surface_list[roop_number - 1])

if __name__ == "__main__":
	extract_noun_and_noun()