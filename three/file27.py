#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from file10 import main

def main2(read_file):
	i = 0
	for k, v in sorted(main(read_file).items(), key=lambda x:x[1], reverse=True):
		i += 1
		if i < 101:
			print "%s\t%s" % (k.strip(), v)
		else:
			break

if __name__ == "__main__":
    main2(sys.argv[1])