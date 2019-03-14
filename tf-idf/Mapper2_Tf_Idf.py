#! /usr/bin/env python3

from __future__ import print_function
import sys
import os
import re



# input depuisSTDIN (standard input)
for line in sys.stdin:
    	# hadoop s'occupe de recuperer le path du fichier en local utiliser export
    line = line.strip()
    # split the line into words
    word_title, count, wordPerDoc = line.split('\t', 2)
    word, title = word_title.split(';')
    print('%s\t%s;%s;%s' % (word, title, count,wordPerDoc))  

        

