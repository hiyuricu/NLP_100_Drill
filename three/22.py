#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
	for line in open(read_file):
		line = line.strip()
		print re.sub(r'\. ([A-Z])', r'.\n\1', line)
if __name__ == "__main__":
    main(sys.argv[1])