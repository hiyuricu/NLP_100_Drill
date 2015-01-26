#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from file72 import get_dic_list

#第一引数にdir71をとる
#get_dic_listは辞書を格納したリストを格納したリストを返すモジュール
def get_NP_feature():
	after_word_flag = False
	for sentense_list in get_dic_list(sys.argv[1]):
	    BNP_flag = False
	    INP_flag = False
	    before_word = ""
	    before_pos = ""
	    after_word = ""
	    after_pos = ""

	    if after_word_flag:
	    	after_word_flag = False
	    	print feature_str + '\tw[1]=NONE\tpos[1]=NONE'

	    for token_dic in sentense_list:
	        if token_dic["chunk"] == "B-NP" and not BNP_flag and not INP_flag:
	        	NP = token_dic["w"]
	        	fw = ""
	        	hw = ""
	        	fpos = ""
	        	hpos = ""
	        	BNP_flag = True
	        	if before_word != "":
	        		pre_word = before_word
	        		pre_pos = before_pos
	        	else:
	        		pre_word = "None"
	        		pre_pos = "None"

	        elif token_dic["chunk"] == "B-NP" and BNP_flag:
	        	if NP.split()[0] in ["a","an","the","A","An","The"] and NP.strip() not in ["a","an","the","A","An","The"]:
	        		after_word_flag = True
	        		feature_str = '# %s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s\tw[-1]=%s\tpos[-1]=%s' % (NP, NP.split()[0].upper(),NP,hw,hpos,hw,hpos,fw,fpos,fw,fpos,pre_word,pre_pos)
	        	NP = token_dic["w"]
	        	fw = ""
	        	hw = ""
	        	fpos = ""
	        	hpos = ""
	        	if before_word != "":
	        		pre_word = before_word
	        		pre_pos = before_pos
	        	else:
	        		pre_word = "None"
	        		pre_pos = "None"
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
	        		after_word_flag = True
	        		feature_str = '# %s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s\tw[-1]=%s\tpos[-1]=%s' % (NP, NP.split()[0].upper(),NP,hw,hpos,hw,hpos,fw,fpos,fw,fpos,pre_word,pre_pos)
	        	BNP_flag = False
	        	INP_flag = False

	        if after_word_flag:
	        	after_word_flag = False
	        	print feature_str + '\tw[1]=%s\tpos[1]=%s' % (token_dic["w"],token_dic["pos"])

	        before_word = token_dic["w"]
	        before_pos = token_dic["pos"]

if __name__ == '__main__':
    get_NP_feature()
