#!/usr/bin/env python3

import sys
import os

#Importer du fichier des mots a ne pas compter
#path_file_stopword = "/Users/kaiim/project/MapReduce/files/tf-idf/stopwords_en.txt"

path_file_stopword = "./tfidf/files/stopwords_en.txt"

fd = open(path_file_stopword, 'r') 
stopwords = fd.read().strip().split()



# input depuisSTDIN (standard input)
for line in sys.stdin:
        # Pour tester en local -> export de la variable s3
        ## sinon c'est hadoop qui s'occupe du fichier
    filename = os.environ["defoe-robinson-103.txt"]
        # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        word = word.lower().strip("()!.;,:\"'")
        if word not in stopwords:
            key = word + ' ' + filename;
            print('%s\t%s' % (key, 1))

# écriture des resultats STDOUT (standard output);
# Cet output sera l'input de reducer_Tf_Idf.py
        
# cat file | scriptMapper.py > mapper
