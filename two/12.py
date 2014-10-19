#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import re

def main(read_file):
    wf = open('12.txt',"w")
    for line in open(read_file,"r"):
        line = line.strip()
        if re.search('なう$', line):
            wf.write("%s\n" % line)
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])
