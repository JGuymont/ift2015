#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/Pile
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# ADT Stack "interface"
class Stack:

    # constructeur
    def __init__( self ):
        pass

    # nombre d'éléments
    def __len__( self ):
        pass

    # produit une chaîne de caractères:
    # les éléments entre crochets
    # séparés par des virgules
    # élément top indiqué
    # taille et capacité de la structure de données
    # indiquées lorsque pertinent
    def __str__( self ):
        pass

    # indique si la pile est vide : aucun élément
    def is_empty( self ):
        pass

    # ajoute un élément sur la pile
    def push( self, element ):
        pass

    # retire un élément de la pile
    def pop( self ):
        pass

    # retourne le dernier élément empilé
    # sans le retirer
    def top( self ):
        pass
