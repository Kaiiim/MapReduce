#! /usr/bin/env python3
from operator import itemgetter
import sys, math



i = 0 
max = 10

title_ref = None
count_doc = 0

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


#for i, (k, v) in enumerate(dico.items()):
#    if v != 0:
#        print("keys", k, "value," ,v / nb_per_doc * math.log10(1/v)) 
#   if i < max:
        #print(k, v)
#        if v != 0:
 #           print("keys", k, "value," ,v / nb_per_doc * math.log10(1/v)) 

