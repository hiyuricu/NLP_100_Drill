#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def main31():
	word_dict = defaultdict(int)
	for line in sys.stdin:
		word_list = line.strip().split("|")
		if word_list[0] in word_dict:
			word_dict[word_list[0]] = word_dict[word_list[0]],(word_list[1],word_list[3],word_list[6])
		else:
			word_dict[word_list[0]] = (word_list[1],word_list[3],word_list[6])
	#defaultdictは辞書のような使い方ができるクラスなので辞書型として返り値としたい場合はdict()を使うことができる。
	return dict(word_dict)

if __name__ == "__main__":
	for k,v in main31().items():
		print k,v