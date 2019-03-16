# MapReduce

# Projet-tfidf-python

# Job 1 : calcul du nombre d'occurences des mots dans des documents
Input : dossier contenant des fichiers textes (stopwords_en.txt, callwild, defoe-robinson-103.txt)

Filtrer avec les critères suivants :

    Mise en minuscule de tous les mots
    Filtrer les mots inutiles contenu dans un fichier stopwords_en.txt
    Suppression des ponctuations et caractères numériques
    Suppression des mots de moins de 3 caractères
    
Sortie : fichier contenant des lignes avec clé <docID mot> et valeur <wordcount>

# Job 2  : calcul du nombre total de mots par document et insertion en fin de lignes
Input : fichier de sortie du job 1
Output : Fichier contenant des lignes avec clé <docID mot> et valeur <wordcount wordperdoc>

# Job 3  : calcul du tf_idf pour chaque mot
Input : fichier de sortie du job 2
Output : fichier contenant des lignes avec clé <docID mot> et valeur <tf_idf>

Pour en savoir plus https://medium.freecodecamp.org/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3
