#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from file10 import main

def main2(read_file):
	word_list = []
	i = 0
	#main(read_file)には辞書が返されている
	for k, v in sorted(main(read_file).items(), key=lambda x:x[1], reverse=True):
		i += 1
		if i < 101:
			word_list.append("%s\t%s" % (k.strip(), v))
		else:
			break
	return word_list

if __name__ == "__main__":
    for word in main2(sys.argv[1]):
    	print word