#!/usr/bin/python
# -*- coding: utf-8 -*-

#head -n 3 address.txt

def main(input_file, input_file2):

    wf = open("5.txt", "w")
    threshold = int(input_file2)
    j = 0
    for line in open(input_file, "r"):
        j += 1
        line = line.strip()
        wf.write(line + "\n")
        if j == threshold:
            break

    wf.close()

if __name__ == "__main__":
  import sys
  main(sys.argv[1], sys.argv[2]) #input_file