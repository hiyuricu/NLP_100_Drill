#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys ,marshal
from file31 import main31

def main():
	wf = open("output32.txt","w")
	marshal.dump(main31(), wf)

if __name__ == "__main__":
	main()