#!/usr/bin/python
# -*- coding: utf-8 -*-

#paste col1.txt col2.txt

def main(input_file, input_file2):

    wf = open("4.txt", "w")

    dic_of = {}
    i = 0
    for line in open(input_file, "r"):
        i += 1
        value = line.strip()
        dic_of[i] = value

    j = 0
    for line in open(input_file2, "r"):
        j += 1
        line = line.strip()
        wf.write("%s\t%s\n" % (dic_of[j], line))

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1], sys.argv[2]) #input_file