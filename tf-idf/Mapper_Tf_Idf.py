#!/usr/bin/env python3

from __future__ import print_function
import sys
import os
import re


def read_stopword(file_path):
    return (set(word.strip() for word in open(file_path)))


stopwords = read_stopword("stopwords.txt")

# input depuisSTDIN (standard input)
for line in sys.stdin:
        # Pour tester en local -> export de la variable s3
        ## sinon c'est hadoop qui s'occupe du fichier
    filename = os.environ["defoe_robinson_103.txt"]
        # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        word = word.lower().strip("\t()!.;,:\"'")
        if word not in stopwords and word != '':
            #key = word + '\t' + filename;
            print('%s\t%s\t%s' % (word, 1, filename))

# écriture des resultats STDOUT (standard output);
# Cet output sera l'input de reducer_Tf_Idf.py
        
# cat file | scriptMapper.py > mapper




#hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar -input ./tfidf/files/defoe-robinson-103.txt -output ./res4     -mapper  'python3 Mapper_Tf_Idf.py' -reducer 'python3 Reducer_Tf_Idf.py' -file /usr/local/hadoop/MapReduce/Mapper_Tf_Idf.py -file /usr/local/hadoop/MapReduce/Reducer_Tf_Idf.py

#Importer du fichier des mots a ne pas compter
#path_file_stopword = "/Users/kaiim/project/MapReduce/tf-idf/files/stopwords_en.txt"
#path_file_stopword = "./tfidf/files/stopwords_en.txt"
#fd = open(path_file_stopword, 'r') 
#stopwords = fd.read().strip().split()


