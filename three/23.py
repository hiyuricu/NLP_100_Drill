#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(read_file):
	for line in open(read_file):
		for list_word in line.strip().split(" "):
			print list_word
		print

if __name__ == "__main__":
    main(sys.argv[1])
