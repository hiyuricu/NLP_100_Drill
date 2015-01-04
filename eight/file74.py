#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from file72 import get_dic_list

#第一引数にdir71をとる
#get_dic_listは辞書を格納したリストを格納したリストを返すモジュール
def get_NP():
	BNP_flag = False
	for sentense_list in get_dic_list(sys.argv[1]):
	    for token_dic in sentense_list:
	        if token_dic["chunk"] == "B-NP" and not BNP_flag:
	        	NP = token_dic["w"]
	        	BNP_flag = True
	        elif token_dic["chunk"] == "B-NP" and BNP_flag:
	        	if NP.split()[0] in ["a","an","the","A","An","The"]:
	        		print "# %s\n%s" % (NP, NP.split()[0].upper())
	        	else:
	        		print "# %s\nNONE" % NP
	        	NP = token_dic["w"]
	        elif token_dic["chunk"] == "I-NP" and BNP_flag:
	        	NP += " %s" % token_dic["w"]
	        elif BNP_flag:
	        	if NP.split()[0] in ["a","an","the","A","An","The"]:
	        		print "# %s\n%s" % (NP, NP.split()[0].upper())
	        	else:
	        		print "# %s\nNONE" % NP
	        	NP = ""
	        	BNP_flag = False

if __name__ == '__main__':
    get_NP()
