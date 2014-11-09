#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(read_file):
	for word in open(read_file):
		print "%s\t%s" % (word.strip(), word.lower().strip())

if __name__ == "__main__":
    main(sys.argv[1])
