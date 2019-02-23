#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "16 février 2014"
#
# Programme Python pour IFT2015/Types abstraits/File
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Implémentation de Queue avec une liste Python

from Queue import Queue
class ListQueue( Queue ):

    DEFAULT_CAPACITY = 1

    def __init__( self, capacity = DEFAULT_CAPACITY ):
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0

    # retourne une chaîne de caractères représentant la Queue
    # avec capacité
    def __str__( self ):
        pp = str( self._data )
        pp += "(size = " + str( len( self ) )
        pp += ")[first = " + str( self._front )
        pp += "; capacity = " + str( self._capacity ) + "]"
        return pp

    # retourne le nombre d'éléments
    def __len__( self ):
        return self._size

    # indique s'il y a des éléments
    # dans la Queue
    def is_empty( self ):
        return self._size == 0

    # retourn le premier élément
    # en Queue sans le retirer
    def first( self ):
        if self.is_empty():
            return None
        else:
            return self._data[self._front]

    # retire le prochain élément de la Queue
    def dequeue( self ):
        # si aucun élément, on retourne None
        if self.is_empty():
            return None
        else:
            # on prend le premier élément
            elem = self._data[self._front]
            # on vide l'espace
            self._data[self._front] = None
            # on ajuste l'index du front
            self._front = ( self._front + 1 ) % len( self._data )
            # on décrémente la taille
            self._size -= 1
            # on retourne l'élément
            return elem

    # ajoute un élément à la fin de la Queue
    def enqueue( self, elem ):
        # on vérifie s'il y a de l'espace dans la liste
        # et sinon, on double sa capacité
        if self._size == len( self._data ):
            self._resize( 2 * len( self._data ) )
        # on calcule l'index du premier élément disponible
        avail = ( self._front + self._size ) % len( self._data )
        # on ajoute le nouvel élément à cet index
        self._data[avail] = elem
        # on incérmente la taille
        self._size += 1

    # redimensionne le tableau à capacité c
    def _resize( self, newcapacity ):
        old = self._data
        # on crée un nouveau tableau de capacité c
        self._data = [None] * newcapacity
        # on copie les éléments de l'ancien tableau dans le nouveau
        walk = self._front
        for k in range( self._size ):
            self._data[k] = old[walk]
            walk = ( 1 + walk ) % len( old )
        # on remet la tête de file au début de la liste et
        # on ajuste la capacité
        self._front = 0
        self._capacity = newcapacity

# unit testing
if __name__ == '__main__':

    data = ListQueue()
    print( data )

    data.enqueue( 5 )
    print( "enqueue 5" )
    print( data )

    data.enqueue( 3 )
    print( "push 3" )
    print( data )

    print( "len = ", str( len( data ) ) )
    print( "is_empty = ", data.is_empty() )
    print( data )

    print( "dequeue = ", data.dequeue() )
    print( data )
    print( "is_empty = ", data.is_empty() )

    print( "dequeue = ", data.dequeue() )
    print( data )
    print( "is_empty = ", data.is_empty() )

    print( "dequeue = ", data.dequeue() )

    data.enqueue( 7 )
    print( "enqueue 7" )
    print( data )
    data.enqueue( 9 )
    print( "enqueue 9" )
    print( data )

    print( "first = ", data.first() )
    data.enqueue( 4 )
    print( "enqueue 4" )
    print( data )

    print( "len = ", str( len( data ) ) )
    print( "dequeue = ", data.dequeue() )
    print( data )

    data.enqueue( 13 )
    print( "enqueue 13" )
    print( data )

    data.enqueue( 15 )
    print( "enqueue 15" )
    print( data )

    data.enqueue( 21 )
    print( "enqueue 21" )
    print( data )
