#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
	for line in sys.stdin:
		for list_word in line.strip().split(" "):
			print list_word
		print

if __name__ == "__main__":
    main()
