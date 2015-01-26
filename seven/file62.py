#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def extract_noun_phrase():
	noun_phrase = ""
	for line in open(sys.argv[1]):
		line_list = line.strip().split()

		if line_list[0] == "EOS":
			if noun_phrase != "":
				print noun_phrase
			noun_phrase = ""

		elif "名詞" in line_list[1]:
			noun_phrase = noun_phrase + line_list[0]

		elif noun_phrase != "" and "名詞" not in line_list[1]:
			print noun_phrase
			noun_phrase = ""

if __name__ == "__main__":
	extract_noun_phrase()