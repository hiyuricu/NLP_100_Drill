#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
	for word in sys.stdin:
		print "%s\t%s" % (word.strip(), word.lower().strip())

if __name__ == "__main__":
    main()