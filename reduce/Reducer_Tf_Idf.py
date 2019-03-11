from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word_stdout, count, title = line.split('\t',2)
    # cast string -> Int
    try:
        count = int(count)
    except ValueError:
        continue
    
    # Hadoop trie STDOUT automatiquement par key
    # Lors du tour 1 current_word == None. Attibution de current_count et current_word
    # Nous pouvons donc au tour 2 comparer automatiquement avec le current word qui réprésente
    # le résultat précédent
    if current_word == word_stdout:
        current_count += count
    else:
        if current_word:
            # écriture le resultat sur STDOUT
            print('%s\t%s' % (current_word, current_count))
        # Tour Zero attibutions du word et du count qui sera incrémenté
        current_count = count
        current_word = word    

# Cas de la dérniere ligne a ne pas oublier 
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
