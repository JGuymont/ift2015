#!/usr/bin/python3

# author = "Francois Major"
# version = "1.0"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Un premier programme !
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013
# Modifié pour le système de notation de la FAS/UdeM.

print( 'Bienvenue dans le calculateur moyenne générale !' )
print( 'Entrez vos notes littérales, une par ligne' )
print( 'et laissez la ligne blanche pour indiquer la fin.' )

# On utilise un dictionnaire pour convertir les lettres en points
# selon le système de notation de la FAS/UdeM
points = { 'A+':4.3, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7,
           'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'E':0.5, 'F':0.0 }

# utilise compteur pour le nombre de cours
#         accumulateur pour les points
#         booleen pour la terminaison de saisie des notes
nombre_cours = 0
total_points = 0
termine = False

# tant que des notes sont entrées
while not termine:
    # on lit la note sur l'entrée standard
    note = input()
    if note == '':
    # si la note est un caractère vide
    # on met la valeur du booléen termine à vrai
        termine = True
    elif note not in points:
    # si la note n'est pas connue (si absent du dictionnaire)
    # on l'ignore et on envoit un message à l'usager
        print( "Note inconnue", note, "sera ignorée" )
    else:
    # ici on a une note valide
    # on incrémente le nombre de notes
    # on accumule les points qui lui correspondent
        nombre_cours += 1
        total_points += points[ note ]

# ici on a terminé la saisie des notes
# on s'assure que le nombre de cours est > 0
# pour éviter la division par 0
# et on envoit un message à l'usager avec sa note numérique
# ou qu'aucune note n'a été saisie
if nombre_cours > 0:
    print( "Votre moyenne est ", total_points / nombre_cours )
else:
# sinon, on envoit un message pour indiquer qu'aucune note n'a été saisie.
    print( "Aucune note n'a été saisie !" )
