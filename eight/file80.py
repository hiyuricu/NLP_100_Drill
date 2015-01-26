#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict

#第一引数にdir71をとる
#get_dic_listは辞書を格納したリストを格納したリストを返すモジュール
def get_NP_feature(sentense_list):
    after_word_flag = False
    for token_dic_list in sentense_list:
        BNP_flag = False
        INP_flag = False
        before_word = ""
        before_pos = ""
        after_word = ""
        after_pos = ""

        if after_word_flag:
            after_word_flag = False
            print feature_str + '\tw[1]=NONE\tpos[1]=NONE'

        for token_dic in token_dic_list:
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

def get_sentense_list(genia_processed_list):
    sentense_list = []
    token_dic_list = []
    token_dic = {}

    for i in range(len(genia_processed_list)/5):
        token_dic = {"w":genia_processed_list[5 * i], "lem":genia_processed_list[5 * i + 1],"pos":genia_processed_list[5 * i + 2], "chunk":genia_processed_list[5 * i + 3]}
        token_dic_list.append(token_dic)

    sentense_list.append(token_dic_list)

    return sentense_list

if __name__ == '__main__':
    import sys
    sentense_list = get_sentense_list(sys.argv[1:])
    get_NP_feature(sentense_list)

