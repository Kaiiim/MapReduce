#!/usr/bin/env python

import os
import sys

path="/Users/kaiim/project/MapReduce/files/tf-idf/defoe-robinson-103.txt"
path2="/Users/kaiim/project/MapReduce/files/tf-idf/stopwords_en.txt"
path3="/Users/kaiim/project/MapReduce/files/tf-idf/callwild"

with open(path) as f:
    text = f.read().strip().split()
with open(path2) as g:
    stopwords = g.read().strip().split()
with open(path3) as h:
    callwild = h.read().strip().split()

for word in text:
    w = word.lower()
    if w not in stopwords:
        print('%s\t%s' % (word, 1)) 
