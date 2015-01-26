#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(read_file):
	for line in open(read_file):
		for sentence in line.strip().rstrip('.').split(". "):
			print sentence + '.'

if __name__ == "__main__":
    main(sys.argv[1])
