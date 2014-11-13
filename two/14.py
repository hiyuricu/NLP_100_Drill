#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('14.txt',"w")
    r = re.compile(r"^@")
    for line in open(read_file,"r"):
    	m = r.match(line)
        if m:
        	wf.write(line)
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])
