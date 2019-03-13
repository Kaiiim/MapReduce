#! /usr/bin/env python3

from __future__ import print_function
import sys
import os
import re


def read_stopword(file_path):
    return (set(word.strip() for word in open(file_path)))

stopwords = read_stopword("/usr/local/hadoop/MapReduce/tf-idf/stopwords_en.txt")

# input depuisSTDIN (standard input)
for line in sys.stdin:
    	# hadoop s'occupe de recuperer le path du fichier en local utiliser export
    filename = os.environ["map_input_file"]
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
       word = word.lower().strip("\t()!.;,:\"'")
       if word not in stopwords and word != '' and len(word) > 3:
            key = word + '\t' + filename;
            print('%s\t%s' % (key, 1))

# écriture des resultats STDOUT (standard output);
# Cet output sera l'input de reducer_Tf_Idf.py
        

