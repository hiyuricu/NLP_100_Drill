#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    for word in open(read_file,"r"):
        if re.compile("(ness|ly)$").search(word):
            print word.strip()

if __name__ == "__main__":
    main(sys.argv[1])