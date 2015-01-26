#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('16.txt',"w")
    #[一-龠]がカタカナに対応してしまう
    r = re.compile("([一-龠]+)\(([A-Z]+)\)")
    for line in open(read_file,"r"):
        m = r.search(line)
        if m:
            wf.write("%s\t%s" % (m.group(1), m.group(2)))
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])