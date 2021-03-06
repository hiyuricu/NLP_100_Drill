#!/usr/bin/python
#-*-coding:utf-8-*-

from collections import defaultdict
import re

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1


class Chunk:
	def __init__(self, num, morphs, dst, srcs):
		self.num    = num
		self.morphs = morphs
		self.dst    = dst
		self.srcs   = srcs


def file53_morph():
	one_sent = []
	all_sent_list = []
	kakari_dict = defaultdict(list)
	for line in open("cabocha_japanese.txt"):
		if "* " in line:
			w = re.split(r" ", line.strip())
			w[2] = w[2][:-1]
			one_chunk = Chunk(w[1], [], w[2], [])
			kakari_dict[w[2]].append(w[1])
			one_sent.append(one_chunk)
		elif "\t" in line:
			item = re.split(r"\t|,", line.strip())
			one_chunk.morphs.append(Morph(item[0], item[7], item[1], item[2]))
		elif "EOS" in line:
			for one_chunk in one_sent:
				one_chunk.srcs = kakari_dict[one_chunk.num]
				for morphs in one_chunk.morphs:
					print 'surface=%s\tbase=%s\tpos=%s' % (morphs.surface, morphs.base, morphs.pos)
				print 'num=%s\tdst=%s\tsrcs=%s' % (one_chunk.num, one_chunk.dst, one_chunk.srcs)
				#one_sent_list.append(c_line)
			all_sent_list.append(one_sent)
			print "EOS"
			one_sent = []
			kakari_dict = defaultdict(list)


if __name__ == '__main__':
	file53_morph()