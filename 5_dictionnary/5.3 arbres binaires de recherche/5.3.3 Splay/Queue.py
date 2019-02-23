#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/ADT Queue
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

#ADT Queue (Classe de base)
class Queue:

    # constructeur
    def __init__( self ):
        pass

    # retourne le nombre d'éléments
    def __len__( self ):
        pass

    # produit une chaîne de caractères:
    # les éléments entre crochets
    # séparés par des virgules
    # taille et capacité de la structure de données
    # indiquées lorsque pertinent
    def __str__( self ):
        pass

    # indique s'il y a des éléments
    # dans la Queue
    def is_empty( self ):
        pass

    # ajoute un élément à la fin de la Queue
    def enqueue( self, element ):
        pass

    # retire le prochain élément de la Queue
    def dequeue( self ):
        pass

    # retourn le premier élément
    # en Queue sans le retirer
    def first( self ):
        pass



