#!/usr/bin/python
# -*- coding: utf-8 -*-

#sort -t '     ' -k2r -k1r address.txt > 9_1.txt

def main(input_file):

    wf = open("9.txt", "w")

    dic = {}
    for line in open(input_file, "r"):
        temp_list = line.split("\t")
        temp_str = ("%s_%s" % (temp_list[1], temp_list[0]))
        print temp_str
        dic[temp_str] = line

    for k, v in sorted(dic.items(), reverse=True):
        wf.write("%s" % (v))

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file