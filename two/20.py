#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('20.txt',"w")
    r = re.compile(ur'([\(（])([^一-龠ぁ-んァ-ヶ0-9A-Za-z]+?)([\)|）])')
    for line in open(read_file,"r"):
    	line = line.decode("utf-8")
        m = r.search(line)
        if m:
            wf.write("%s\n" % (m.group(0).encode("utf-8")))
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])