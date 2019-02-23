#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Files avec priorités/File d'attente prioritaire
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

#ADT PriorityQueue (Classe de base)
class PriorityQueue:

    # classe imbriquée privée pour les items
    class _Item:
        # enregistrement efficace pour les items
        # définis par une clé et une valeur
        __slots__ = '_key', '_value'

        def __init__( self, k, v ):
            self._key = k
            self._value = v

        def __lt__( self, other ):
            return self._key < other._key

        def __gt__( self, other ):
            return self._key > other._key

        def __str__( self ):
            return "(" + str( self._key ) + "," + str( self._value ) + ")"

    # méthodes de base de l'ADT

    # constructeur
    def __init__( self ):
        pass

    # taille de la file
    def __len__( self ):
        pass

    # pretty print
    def __str__( self ):
        if self.is_empty():
            return "[]"
        pp = "["
        for item in self:
            pp += str( item )
        pp += "]"
        return pp

    # test si vide
    def is_empty( self ):
        return len( self ) == 0

    # élément minimum (de plus grande priorité)
    def min( self ):
        pass

    # adjouter un élément x avec clé k
    def add( self, k, x ):
        pass

    # retirer l'élément de plus grande priorité
    def remove_min( self ):
        pass
            
# unit testing
if __name__ == '__main__':

    print( "PriorityQueue unit testing..." )
    print( "class PriorityQueue ADT" )
    print( "End of testing." )
