#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

#第一引数にdir71をとる
#コーパスディレクトリ内のファイルのパスを格納したリストを返す
def get_flist(dirpath):
    flist = []
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            file_path = os.path.join(root, f)
            if os.path.isfile(file_path):
                # print file_path
                flist.append(file_path)
    return flist

#辞書を格納したリストを格納したリストを返すモジュールを作成している
def get_dic_list(dirpath):
    sentense_list = []
    token_dic_list = []
    for file_pass in get_flist(dirpath):
        for line in open(file_pass):
            temp_token_list = line.strip().split()
            if line == "\n":
                continue

            token_dic = {"w":temp_token_list[0], "lem":temp_token_list[1],"pos":temp_token_list[2], "chunk":temp_token_list[3]}
            token_dic_list.append(token_dic)

            if temp_token_list[0] == ".":
                sentense_list.append(token_dic_list)
                token_dic_list = []

    return sentense_list

if __name__ == '__main__':
    for sentense_list in get_dic_list(sys.argv[1]):
        for token_dic in sentense_list:
            for k,v in token_dic.items():
                print k,v
