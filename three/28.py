#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from file27 import main2

def main(read_file):
	with open('bigram.temp', 'w') as bigramFile:
		for word in open(read_file,"r"):
			word_length = len(word)
			while word_length > 1:
				bigramFile.write(word[word_length - 2:word_length] + "\n")
				word_length -= 1
	print main2(bigramFile)

if __name__ == "__main__":
    main(sys.argv[1])