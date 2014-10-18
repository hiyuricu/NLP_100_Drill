#!/usr/bin/python
# -*- coding: utf-8 -*-

#sort -t '     ' -k 2 address.txt > 8_1.txt
#bash上でタブを入力するには[Ctrl-V][tab] (Ctrl-Vで入力モードにしてからtabを入力する)

def main(input_file):

    wf = open("8.txt", "w")

    dic = {}
    for line in open(input_file, "r"):
        temp_list = line.split("\t")
        dic[temp_list[1]] = line

    for k, v in sorted(dic.items()):
        wf.write("%s" % (v))

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file