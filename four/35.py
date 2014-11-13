#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, marshal
from collections import defaultdict

def main():
	word_flag_dic = defaultdict(int)
	dic = marshal.load(open("output32.txt","r"))
	for word in sys.stdin:
		word = word.strip()
		if word in dic:
			word_flag_dic[word] += 1
		if word_flag_dic[word] >= 3:
			print dic[word]

if __name__ == "__main__":
	main()