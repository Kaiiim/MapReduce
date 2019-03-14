#! /usr/bin/env python3
from operator import itemgetter
import sys, math


title_ref = None

dico = {}
data = {}

for line in sys.stdin:
    line = line.strip()
    
    word_title, count = line.split('\t',1)
    word_stdout, title = word_title.split(';',1)
    try:
        count = int(count)
    except ValueError:
        continue
    # dictionnaire pour pouvoir recuperer le nom + titre dans la boucle for
    data[word_title] = count    
    # le if else servira a pouvoir compter le nombre de mots par documents
    if title == title_ref:
        dico[title] = dico.get(title, 0) + count
    else:
        if title:
            title_ref = title 

# cas de la derniere ligne
dico[title] = dico.get(title, 0) + count


for key, val in data.items():
    word, filename = key.split(';', 1)
    print('%s\t%s\t%s' % (key, val, dico[filename]))


