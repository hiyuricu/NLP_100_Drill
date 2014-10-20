#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('18.txt',"w")
    r = re.compile(u"(宮城県|)仙台市(.+(町|区)|)(.+|)([0-9]+-[0-9]+-[0-9]+|)")
    for line in open(read_file,"r"):
    	line = line.decode("utf-8")
        m = r.search(line)
        if m:
            wf.write("%s\n" % (m.group(0).encode("utf-8")))
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])