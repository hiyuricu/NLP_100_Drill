#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from file27 import main2

def main(read_file):
	bigramFile = open("bigram.txt", "w")
	for word in open(read_file,"r"):
		word = word.strip()
		word_length = len(word)
		while word_length > 1:
			bigramFile.write("%s\n" % word[word_length - 2:word_length])
			word_length -= 1
	bigramFile.close()
	for i in main2("bigram.txt"):
		print i

if __name__ == "__main__":
    main(sys.argv[1])