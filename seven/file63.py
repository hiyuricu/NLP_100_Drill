
#!/usr/bin/python
#-*-coding:utf-8-*-
def tfidfscore():
    import glob, sys, math
    from collections import defaultdict
    freq = defaultdict(int)
    freq_doc = {}
    df = defaultdict(int)
    file_no = 0
    tfidf = {}

    for file_pass in glob.glob("dir62/*"):
        file_no += 1
        for line in open(file_pass):
            line = line.strip()
            freq[line] += 1
            freq_doc[line] = 1
        for j in freq_doc:
            df[j] += 1
        freq_doc = {}

    for k in freq:
        idf = float(math.log(file_no/df[k],2))
        tfidf[k] = freq[k]*idf

    return(tfidf,freq,df)

if __name__ == "__main__":
    (tfidf,freq,df) = tfidfscore()
    for i in tfidf:
        print i,tfidf[i],freq[i],df[i]