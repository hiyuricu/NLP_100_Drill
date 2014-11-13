#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from stemming.porter2 import stem

def main():
 	for line in sys.stdin:
		print "%s\t%s\t%s" % (line.strip().split()[0], line.strip().split()[1], stem(line.strip().split()[1]))
		
if __name__ == "__main__":
    main()