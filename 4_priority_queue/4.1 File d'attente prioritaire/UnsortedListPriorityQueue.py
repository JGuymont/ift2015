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

# ADT UnsortedListPriorityQueue
class UnsortedListPriorityQueue( PriorityQueue ):

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

    # cherche et retourne l'élément de plus grande priorité
    def min( self ):
        if self.is_empty():
            return None

        # cherche le min en O(n)
        the_min = self._Q[0]
        for item in self:
            if item < the_min:
                the_min = item

        #retourne le min
        return the_min

    # ajoute un élément x de clé k à la fin de la liste, O(1)
    def add( self, k, x ):
        #in O(1)
        self._Q.append( self._Item( k, x ) )

    # recherche, supprime et retourne l'élément de plus grande priorité
    def remove_min( self ):
        if self.is_empty():
            return None

        # cherche l'index du min en O(n)
        index_min = 0
        for i in range( 1, len( self ) ):
            if self._Q[i] < self._Q[index_min]:
                index_min = i

        the_min = self._Q[index_min]
        # supprime le min en O(n)
        del self._Q[index_min]
        # retourne l'élément supprimé
        return the_min
            
# unit testing
if __name__ == '__main__':

    print( "UnsortedListPriorityQueue unit testing..." )

    testQ = UnsortedListPriorityQueue()
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
