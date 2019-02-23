#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/Listes chaînées
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# DoublyLindedNode

class DoublyLinkedNode:

    def __init__( self, element, prev, next ):
        self.element = element # stockage d'un élément
        self.prev = prev       # référence au noeud précédent
        self.next = next       # référence au noeud suivant



