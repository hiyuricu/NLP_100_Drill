#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from file72 import get_dic_list

#第一引数にdir71をとる
#get_dic_listは辞書を格納したリストを格納したリストを返すモジュール
def get_NP():
	BNP_flag = False
	INP_flag = False
	for sentense_list in get_dic_list(sys.argv[1]):
	    for token_dic in sentense_list:
	        if token_dic["chunk"] == "B-NP" and not BNP_flag and not INP_flag:
	        	NP = token_dic["w"]
	        	fw = ""
	        	hw = ""
	        	fpos = ""
	        	hpos = ""
	        	BNP_flag = True
	        elif token_dic["chunk"] == "B-NP" and BNP_flag:
	        	if NP.split()[0] in ["a","an","the","A","An","The"] and NP.strip() not in ["a","an","the","A","An","The"]:
	        		print '%s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s' % (NP, NP.split()[0].upper(),NP,hw,hpos,hw,hpos,fw,fpos,fw,fpos)
	        	NP = token_dic["w"]
	        	fw = ""
	        	hw = ""
	        	fpos = ""
	        	hpos = ""
	        	INP_flag = False
	        elif token_dic["chunk"] == "I-NP" and BNP_flag and not INP_flag:
	        	NP += " %s" % token_dic["w"]
	        	fw = token_dic["w"]
	        	hw = token_dic["w"]
	        	fpos = token_dic["pos"]
	        	hpos = token_dic["pos"]
	        	INP_flag = True
	        elif token_dic["chunk"] == "I-NP" and BNP_flag and INP_flag:
	        	NP += " %s" % token_dic["w"]
	        	hw = token_dic["w"]
	        	hpos = token_dic["pos"]
	        elif BNP_flag:
	        	if NP.split()[0] in ["a","an","the","A","An","The"] and NP.strip() not in ["a","an","the","A","An","The"]:
	        		print '%s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s' % (NP, NP.split()[0].upper(),NP,hw,hpos,hw,hpos,fw,fpos,fw,fpos)
	        	BNP_flag = False
	        	INP_flag = False

if __name__ == '__main__':
    get_NP()

# print '%s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s\tw[-1]=%s\tpos[-1]=%s\tw[1]=%s\tpos[1]=%s' % (w,fatures.head_w,w_0,hw,hpos,hw,hpos,fw,fpos,fw,fpos,fatures.pre_w,fatures.pre_pos,next_w,next_pos)
