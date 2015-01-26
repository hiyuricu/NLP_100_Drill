#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MeCab

def Morphological_Analysis():
	me = MeCab.Tagger("mecabrc")
	text = []

	for line in open(sys.argv[1]):
		result = me.parse(line.strip())
		sent = []
		#morphには一文のそれぞれの単語のmecabの解析結果が代入されています
		for morph in result.split("\n"):
			if morph == "EOS":
				break
			d={}
			d["surface"]=morph.split("\t")[0]
			d["base"]=morph.split("\t")[1].split(",")[6]
			d["pos"]=morph.split("\t")[1].split(",")[0]
			d["pos1"]=morph.split("\t")[1].split(",")[1]
			#sentには辞書型の一文分の解析結果がappendされていく
			sent.append(d)
		#textは辞書を要素としたリスト(sent)を要素としたリストとなる
		text.append(sent)
	#print text

if __name__ == "__main__":
	Morphological_Analysis()