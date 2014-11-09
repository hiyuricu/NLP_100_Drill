#!/usr/bin/python
# -*- coding: utf-8 -*-

#cut -f 2 address.txt | sort | uniq -c | sort -nr > 10_1.txt
#cut -f 2 address.txt | sort | uniq -c | sort -t ' ' -k1r > 10_1.txt

def main(input_file):

    count_of = {}
    for word in open(input_file, "r"):
        if word in count_of:
            count_of[word] += 1
        else:
            count_of[word] = 1

    for k, v in sorted(count_of.items(), key=lambda x:x[1], reverse=True):
        print "%s\t%s" % (k.strip(), v)

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file