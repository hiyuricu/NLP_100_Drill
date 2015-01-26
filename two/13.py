#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('13.txt',"w")
    r = re.compile(": RT @.+?: (.+)")
    for line in open(read_file,"r"):
    	#line = line.decode('utf-8')
    	m = r.search(line)
        if m:
        	wf.write("%s\n" % (m.group(1)))
            #wf.write("%s\n" % (m.group(1)).encode('utf-8'))
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])
