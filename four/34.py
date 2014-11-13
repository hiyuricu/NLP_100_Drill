#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, marshal

def main():
	dic = marshal.load(open("output32.txt","r"))
	for word in sys.stdin:
		word = word.strip()
		if word not in dic:
			print word

if __name__ == "__main__":
	main()