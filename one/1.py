#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import re

def main(input_file):
    line_number = 0
    for line in open(input_file, "r"):
        line_number = line_number + 1

    print line_number

if __name__ == "__main__":
  import sys
  main(sys.argv[1]) #input_file