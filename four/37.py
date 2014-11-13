#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def return_bigram_frequency(read_file):
	count_of = defaultdict(int)
	for line in open(read_file):
		count_of[line] += 1
	for line in open(read_file):
		print "%s\t%s" % (count_of[line],line.strip())

if __name__ == "__main__":
	return_bigram_frequency(sys.argv[1])