#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/Listes chaînées
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# SinglyLindedNode

class SinglyLinkedNode:

    def __init__( self, element, next ):
        self.element = element # stockage d'un élément
        self.next = next       # référence au noeud suivant



