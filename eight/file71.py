#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re, os
from geniatagger import *
#tagger = GeniaTagger('/Users/tachibanaryuichi/Downloads/geniatagger-3.0.1/geniatagger')

#第一引数にコーパスディレクトリ、第二引数に作業用ディレクトリをとる

#コーパスディレクトリ内のファイルのパスを格納したリストを返す
def get_flist(dirpath):
    flist = []
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            dir_path = os.path.join(root, f)
            if os.path.isfile(dir_path):
                flist.append(dir_path)
    return flist

if __name__ == '__main__':
    re_sentence = re.compile(r"\. [A-Z]|\.\[[0-9]+\] [A-Z]")
    tagger = GeniaTagger('/Users/tachibanaryuichi/Downloads/geniatagger-3.0.1/geniatagger')
    corpus_dir = sys.argv[1]
    target_dir = sys.argv[2]

    flist = get_flist(corpus_dir)
    for file_pass in flist:
        wf = open(target_dir + "/" + file_pass.split("/")[1] + ".genia", "w")
        for line in open(file_pass):
            if line == "\n":
                continue
            temp = line
            result_search = re_sentence.search(temp)
            while(result_search is not None):
                for taggered in tagger.parse(temp[0:result_search.start()+1]):
                    wf.write("\t".join(taggered)+"\n")
                wf.write("\n")
                temp = temp[result_search.start()+len(result_search.group()[:-1]):]
                result_search = re_sentence.search(temp)
            for taggered in tagger.parse(temp.strip()):
                wf.write("\t".join(taggered)+"\n")
        wf.close()

"""def extract_noun_phrase():
	noun_phrase = ""
	for line in open(sys.argv[1]):
		print tagger.parse(line)

if __name__ == "__main__":
	extract_noun_phrase()"""
