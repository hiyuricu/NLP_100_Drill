#!/usr/bin/python
# -*- coding: utf-8 -*-

#tail -n 3 address.txt

def main(input_file, input_file2):

    wf = open("6.txt", "w")
    threshold = - int(input_file2)

    list = []
    for line in open(input_file, "r"):
        line = line.strip()
        list.append(line)

    for j in range(threshold,0):
        wf.write(list[j] + "\n")

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1], sys.argv[2])