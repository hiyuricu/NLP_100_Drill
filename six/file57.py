#!/usr/bin/python
#-*-coding:utf-8-*-

from file054 import *

def file057(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num == another_chunk.dst:
					s  = one_chunk.morphs_pos("動詞")
					s2 = one_chunk.morphs_pos1("非自立")
					s3 = another_chunk.morphs_pos("名詞")
					s4 = another_chunk.morphs_pos1("非自立")
					if s and s2 == False and s3 and s4 == False:
						print '%s\t%s' % (another_chunk.morphs_add, one_chunk.morphs_add)


if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanese.txt")
	file057(all_sent_list)