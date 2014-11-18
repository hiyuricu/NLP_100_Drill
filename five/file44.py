#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MeCab
import marshal

def extract_sahen_noun():
	me = MeCab.Tagger("mecabrc")
	verb_base_list = []

	for line in open(sys.argv[1]):
		result = me.parse(line.strip())
		#morphには一文のそれぞれの単語のmecabの解析結果が代入されています
		for morph in result.split("\n"):
			if morph == "EOS":
				break
			if morph.split("\t")[1].split(",")[0] == "名詞" and morph.split("\t")[1].split(",")[1] == "サ変接続":
				verb_base_list.append(morph.split("\t")[0])

	return verb_base_list

if __name__ == "__main__":
	for verb in extract_sahen_noun():
		print verb