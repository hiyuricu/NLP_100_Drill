#!/usr/bin/python
#-*-coding:utf-8-*-

import re

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1
		print surface, base, pos, pos1

def file52_morph():
	morph_list = []
	for line in open("output51.txt"):
		if "EOS" in line:
			pass
		elif "*" != line[0]:
			item = re.split(r"\t|,", line.strip())
			morph_list.append(Morph(item[0], item[7], item[1], item[2]))

if __name__ == '__main__':
	file52_morph()