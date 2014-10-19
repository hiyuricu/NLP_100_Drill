#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main(read_file):
    wf = open('15.txt',"w")
    r = re.compile(r"(@([a-zA-Z0-9_]+))")
    for line in open(read_file,"r"):
    	m = r.search(line)
        if m:
        	#\1や\2は後方参照である。compileの括弧とそれぞれ対応している
        	wf.write(r.sub(r'<a href="https://twitter.com/#!/\2">\1</a>', line))
        else:
        	wf.write(line)
    wf.close()

if __name__ == "__main__":
    main(sys.argv[1])