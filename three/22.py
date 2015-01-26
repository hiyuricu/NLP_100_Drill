#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re

def main():
	for article in sys.stdin:
		article = article.strip()
		print re.sub(r'\. ([A-Z])', r'.\n\1', article)
if __name__ == "__main__":
    main()