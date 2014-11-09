#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    for word in open(read_file,"r"):
    	word = word.strip()
        word_length = len(word)
        while word_length > 1:
        	print word[word_length - 2:word_length]
        	word_length -= 1

if __name__ == "__main__":
    main(sys.argv[1])