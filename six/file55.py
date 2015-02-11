#!/usr/bin/python
#-*-coding:utf-8-*-

from file054 import *

def file055(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					print '%s\t%s' % (another_chunk.morphs_add, one_chunk.morphs_add)


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	file055(all_sent_list)