#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from file10 import main

def main2(read_file):
	print type(main(read_file))
"""	i = 0
	for line in main(read_file):
		line = line.strip()
		i += 1
		if i < 101:
			print i
			print line
		else:
			break
"""
if __name__ == "__main__":
    main2(sys.argv[1])