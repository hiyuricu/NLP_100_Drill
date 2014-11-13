#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def return_bigram_frequency(read_file):
	count_of = defaultdict(int)
	count_of["."] += 1
	for line in open(read_file):
		line = line.strip()
		count_of[line.split()[1]] += 1
		count_of[line.split()[1] + "\t" + line.split()[2]] += 1
	for line in open(read_file):
		line = line.strip()
		print "%s\t%s\t%s" % (float(count_of[line.split()[1] + "\t" + line.split()[2]]) / count_of[line.split()[1]], line.split()[1], line.split()[2])

if __name__ == "__main__":
	return_bigram_frequency(sys.argv[1])