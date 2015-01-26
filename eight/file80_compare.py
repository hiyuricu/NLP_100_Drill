#!/usr/bin/python
#-*-coding:utf-8-*-

def main(pair_text, feature_text):
    pair_list = []
    count = -1
    for line in open(pair_text):
        pair_list.append(line)

    for line in open(feature_text):
        feature_list = line.strip().split()
        if feature_list[0] == "#":
            del feature_list[0]
            count += 1
            if pair_list[count].strip().split()[0] != pair_list[count].strip().split()[1]:
                for word in feature_list:
                    if word == pair_list[count].strip().split()[0].lower():
                        print pair_list[count].strip().split()[1].lower(),
                    else:
                        print word,
                print ""
            else:
                for word in feature_list:
                    print word,
                print ""


if __name__ == '__main__':
    import sys
    main(sys.argv[1], sys.argv[2])
