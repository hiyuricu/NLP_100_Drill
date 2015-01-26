#!/usr/bin/python
#-*-coding:utf-8-*-

from optparse import OptionParser
from file42 import *
from file43 import *
from file44 import *
from file45 import *
from file46 import *

def print_list(text):
    if text != None:
        for line in text:
            print line

parser = OptionParser()
parser.add_option("-v","--verb", help=u"全ての動詞を抜き出す(42)")
parser.add_option("-b","--base",action='store_true', help=u"全ての動詞の原型を抜き出す(43)")
parser.add_option("-n","--noun",action='store_true', help=u"全てのサ変名詞を抜き出す(44)")
parser.add_option("-o","--AofB",action='store_true', help=u"全ての「AのB」という表現を抜き出す(45)")
parser.add_option("-c","--chain",action='store_true', help=u"全ての名詞の連接を抜き出す(46)")
options,args = parser.parse_args()
if options.verb:
    verb_list = extract_verb(open("japanese.txt").read())
    print_list(verb_list)
if options.base != None:
    base_list = extract_verb_base(options.base)
    print_list(base_list)
if options.noun != None:
    form_list = extract_sahen_noun(options.noun)
    print_list(form_list)
if options.AofB != None:
    pair_list = extract_noun_and_noun(options.AofB)
    print_list(pair_list)
if options.chain != None:
    chain_list = extract_compound_noun(options.chain)
    print_list(chain_list)
