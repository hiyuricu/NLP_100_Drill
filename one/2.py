#!/usr/bin/python
# -*- coding: utf-8 -*-

#sedでは$ sed -e 's/ /\ /g' address.txt > 2_1.txt
#でできた(tabはctrl-v、tabで挿入できる)

import sys
import string
import re

def main(input_file):

    wf = open("2.txt", "w")

    for line in open(input_file, "r"):
            data = re.sub('\t', " ", line)
            wf.write(data)

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file