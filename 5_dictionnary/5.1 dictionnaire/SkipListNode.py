#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

#class noeud pour une skiplist
class SkipListNode:

    #on a besoin de pointeurs sur l'élément, puis sur les noeuds
    #précédent, suivant, au-dessous et au-dessus
    __slots__ = '_elem', '_prev', '_next', '_belo', '_abov'
    def __init__( self, elem, prev = None, next = None, belo = None, abov = None ):
        self._elem = elem
        self._prev = prev
        self._next = next
        self._belo = belo
        self._abov = abov

    #prettyprint
    def __str__( self ):
        return "(" + str( self._elem ) + ")"
