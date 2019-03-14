#! /usr/bin/env python3
from operator import itemgetter
import sys, math


word_ref = None
counter = 0

dico = {}
data = {}


# le but de cette boucle est de compter le nombre de fois ou un mot apparait dans les documents
for i, line in enumerate(sys.stdin):
    line = line.strip()
    
    # recuperation de mot 
    word, rest = line.split('\t',1)
    # stockage dans un dictionnaire pour pouvoir recuperer le nom + titre dans la boucle for
    data[word] = rest 
    # le if else servira a pouvoir compter le nombre de mots par documents
        
    if word == word_ref:
        counter = counter + 1
    else:
        dico[word_ref] = counter
        if word != "":
            word_ref = word 
            counter = 1
 
	####################################
	# ou solution 2           
	#    if word not in dico:
	#        dico[word] = 1
	#    else:
	#        dico[word] = dico[word] + 1 
	####################################

# cas de la derniere ligne
dico[word] = counter
#print(dico.items())

for key, val in data.items():
    title, count, nbPerDoc = val.split(';', 2)
    try:
        nbPerDoc = int(nbPerDoc)
        count = int(count)
    except ValueError:
        continue
    try:
        tfidf = (count/nbPerDoc)*math.log10(2.0/float(dico[key]))
    except ValueError:
        continue
    print('%s\t%s\t%s' % (key, val, tfidf))

