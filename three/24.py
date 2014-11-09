#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(read_file):
	for line in open(read_file):
		for list_word in line.strip().split(" "):
			if list_word[-1] in [".", ",","(",")"]:
				print "%s\n%s" % (list_word[:-1], list_word[-1])
			else:
				print list_word

if __name__ == "__main__":
    main(sys.argv[1])
