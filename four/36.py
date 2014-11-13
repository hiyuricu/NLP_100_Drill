#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(read_file):
	before_line = ""
	for line in open(read_file):
		if before_line == "":
			before_line = line
		else:
			print "%s\t%s" % (before_line.strip(),line.strip())
			before_line = line

if __name__ == "__main__":
    main(sys.argv[1])
