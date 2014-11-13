#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('15.html',"w")
    r = re.compile(r"(@([a-zA-Z0-9_]+))")
    for line in open(read_file,"r"):
        line = line.strip()
        #\1や\2は後方参照である。compileの括弧とそれぞれ対応している
        line2 = r.sub(r'<a href="https://twitter.com/#!/\2">\1</a>', line)
        wf.write("%s\n" % line2)
        line2 = ""
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])