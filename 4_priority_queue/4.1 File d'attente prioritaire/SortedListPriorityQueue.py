#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Files avec priorités/File d'attente prioritaire
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# utilise la classe de base PriorityQueue
from PriorityQueue import PriorityQueue

# ADT SortedListPriorityQueue
class SortedListPriorityQueue( PriorityQueue ):

    # méthodes de base

    # constructeur, on utilise une liste Python
    def __init__( self ):
        self._Q = []

    # taille de la file avec len de la liste Python
    def __len__( self ):
        return len( self._Q )

    # accès direct à un élément de la liste
    def __getitem__( self, i ):
        return self._Q[i]

    # vide si len == 0
    def is_empty( self ):
        return len( self ) == 0

    # retourne l'élément de plus grande priorité en O(1)
    def min( self ):
        if self.is_empty():
            return None

        # le min est à Q[0]
        return self._Q[0]

    # ajoute l'élément x de clé k
    def add( self, k, x ):
        item = self._Item( k, x )
        if self.is_empty():
            self._Q.append( item )
        else:
            # créer l'espace supplémentaire dans Q, O(1)
            self._Q.append( item )

            # cherche l'index d'insertion en O(n)
            i = 0
            while item > self._Q[i]:
                i += 1

            # décale les éléments en O(n)
            for j in range( len( self ) - 1, i, -1 ):
                self._Q[j] = self._Q[j-1]

            # insère le nouvel élément à l'index i
            self._Q[i] = item
        return item

    # retourne et supprime l'élément de plus grande priorité, O(n)
    def remove_min( self ):
        if self.is_empty():
            return None

        # accède min en O(1); le min est à Q[0]
        the_min = self._Q[0]

        # del doit décaler les éléments, O(n)
        del self._Q[0]
        return the_min

# unit testing
if __name__ == '__main__':

    print( "SortedListPriorityQueue unit testing..." )

    testQ = SortedListPriorityQueue()
    testQ.add( 5, 'A' )
    testQ.add( 9, 'C' )
    testQ.add( 3, 'B' )
    testQ.add( 7, 'D' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.add( 2, 'AA' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    print( testQ.remove_min() )

    print( "End of testing." )
