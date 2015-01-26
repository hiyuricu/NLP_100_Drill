#!/usr/bin/python
# -*- coding: utf-8 -*-

#cut -f 1 address.txt > col1.txt
#cut -f 2 address.txt > col2.txt

def main(input_file):

    wf = open("col1_1.txt", "w")
    wf2 = open("col2_1.txt", "w")

    for line in open(input_file, "r"):
        list = line.split("\t")
        wf.write(list[0] + "\n")
        wf2.write(list[1])

    wf.close()
    wf2.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file