#! /usr/bin/env python3
from operator import itemgetter
import sys, math

i = 0 
max = 30

current_word = None
current_count = 0

dico = {}
data = {}

for line in sys.stdin:
    #if i < max:
     #   print("tour", i)
#    filename = os.environ["map_input_file"]
#    print(filename)
    line = line.strip()
    word_stdout, count, title = line.split('\t',2)
    # cast string -> Int
    try:
        count = int(count)
    except ValueError:
        continue
    data[word_stdout] = count    
    # Hadoop trie STDOUT automatiquement par key
    # Lors du tour 1 current_word == None. Attibution de current_count et current_word
    # Nous pouvons donc au tour 2 comparer automatiquement avec le current word qui réprésente
    # le résultat précédent
    if current_word == word_stdout:
        current_count += 1
        #if i < max:
         #   print("current == au mot predecedentcurrent_count", current_count)
    else:
        dico[current_word] = current_count
        #if current_word:
            # écriture le resultat sur STDOUT
            # Tour Zero attibutions du word et du count qui sera incrémenté
            #print("x")
        current_count = count
        current_word = word_stdout  
        #if i < max:
           # print("ELSE", i,  "current_word |", current_word,"| current_count |", current_count, \
		#"| word_stdout |",word_stdout,"| count |", count,"| titile |", title)
    #i = i + 1

dico[current_word] = current_count
nb_per_doc = len(data)


for i, (k, v) in enumerate(dico.items()):
    if v != 0:
        print("keys", k, "value," ,v / nb_per_doc * math.log10(1/v)) 
#   if i < max:
        #print(k, v)
#        if v != 0:
 #           print("keys", k, "value," ,v / nb_per_doc * math.log10(1/v)) 

