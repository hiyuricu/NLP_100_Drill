#!/usr/bin/python
# -*- coding: utf-8 -*-

#cut -f 1 address.txt | sort | uniq | wc

def main(input_file):

    list = []
    for line in open(input_file, "r"):
        temp_list = line.split("\t")
        list.append(temp_list[0])

    print len(set(list))

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file