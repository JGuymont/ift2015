#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

import sys
import time
import random
from Map import Map
from SkipList import SkipList

_MIN = -sys.maxsize - 1
_MAX = sys.maxsize

#Map implémenté avec une skiplist
class SkipListMap( Map ):

    #on utilise une skiplist avec des Items comme éléments dans les noeuds
    #on utilise les valeurs de +infini et -infini pour les sentinelles
    def __init__( self, _MIN_KEY = _MIN, _MAX_KEY = _MAX ):
        self._T = SkipList( Map._Item( _MIN_KEY, None ), Map._Item( _MAX_KEY, None ) )

    def __str__( self ):
        return str( self._T )

    def __len__( self ):
        return len( self._T )

    #accès à l'élément k, par appel direct à SkipSearch
    def __getitem__( self, k ):
        p = self._T.SkipSearch( self._Item( k ) )
        if p._elem._key != k:
            raise KeyError( k )
        return p._elem._value

    #assignation de l'élément de clé k, appel direct à SkipInsert
    def __setitem__( self, k, v ):
        self._T.SkipInsert( self._Item( k, v ) )

    #suppression de l'élément de clé k, appel direct à SkipRemove
    def __delitem__( self, k ):
        p = self._T.SkipRemove( self._Item( k ) )
        if p is None:
            raise KeyError( k )
        return p._elem._value

    #itérateur sur les clé
    def __iter__( self ):
        for item in self._T:
            yield item._key

    def pop( self, k ):
        p = self._T.SkipRemove( self._Item( k ) )
        if p is None:
            raise KeyError( k )
        return p._elem._value

    #trouve et retourne l'élément avec la plus petit clé
    #si la Map n'est pas vide
    def find_min( self ):
        if len( self._T ) > 0:
            theItem = self._T.Min()
            return ( theItem._key, theItem._value )
        else:
            return None

    #trouve et retourne l'élément avec la plus grande clé
    #si la Map n'est pas vide
    def find_max( self ):
        if len( self._T ) > 0:
            theItem = self._T.Max()
            return ( theItem._key, theItem._value )
        else:
            return None

    #retourne ( key, value ), key >= k
    def find_ge( self, k ):
        #SkipSearch s'arrête sur key <= k
        p = self._T.SkipSearch( Map._Item( k ) )
        #si on arrête sur la sentinelle à droite
        #il n'existe pas d'élément dont la clé est >= k
        if p._next is None:
            return None
        #sinon, si l'élément de clé k n'existe pas,
        #le plus grand est le suivant
        if p._elem._key < k:
            p = p._next
        return ( p._elem._key, p._elem._value )

    #retourne ( key, value ), key <= k
    def find_le( self, k ):
        #SkipSearch s'arrête sur key <= k
        p = self._T.SkipSearch( Map._Item( k ) )
        #si on arrête sur la sentinelle à gauche
        #il n'existe pas d'élément dont la clé est <= k
        if p._prev is None:
            return None
        #sinon, on s'est arrêté dessus
        return ( p._elem._key, p._elem._value )

    #retourne ( key, value ), key > k
    def find_gt( self, k ):
        #SkipSearch s'arrête sur key <= k
        p = self._T.SkipSearch( Map._Item( k ) )
        #si on arrête sur le dernier élément ou la sentinelle à droite
        #il n'existe pas d'élément dont la clé est > k
        if p._next is None or p._next._next is None:
            return None
        #le plus grand est le suivant
        #s'il l'élément de clé k existe, le > est le suivant
        #s'il n'existe pas, le > est aussi le suivant
        #puisqu'on s'est arrêté sur le premier <
        p = p._next
        return ( p._elem._key, p._elem._value )

    #retourne ( key, value ), key < k
    def find_lt( self, k ):
        #SkipSearch s'arrête sur key <= k
        p = self._T.SkipSearch( Map._Item( k ) )
        #si on arrête sur le premier élément ou la sentinelle à gauche
        #il n'existe pas d'élément dont la clé est < k
        if p._prev is None or p._prev._prev is None:
            return None
        #sinon, soit on s'est arrêté sur l'élément de clé k
        #et on doit prendre son précédent (le premier < devant k)
        #ou si l'élément de clé k n'existe pas, on est sur le
        #premier élément de clé < k
        if p._elem._key == k:
            p = p._prev
        return (p._elem._key,p._elem._value)

    #itérateur des éléments de clé entre start jusqu'au précédent stop
    def find_range( self, start, stop ):
        #si start est None, on prend start = Min
        if start is None:
            start,v = self.find_min()
        #on cherche l'élément de clé start
        #on arrête sur ce dernier ou sur le premier élément <
        p = self._T.SkipSearch( Map._Item( start ) )
        #si l'élément start n'existe pas, on est sur l'élément <
        #donc, on prend l'élément suivant
        if p._elem._key < start:
            p = p._next
        #tant qu'il y a des éléments dont la clé est < stop
        #on les rapporte dans l'itérateur
        while not( p._next is None ) and ( p._elem._key < stop ):
                yield ( p._elem._key, p._elem._value )
                p = p._next

#unit testing
if __name__ == '__main__':

    print( "SkipListMap unit testing..." )

    M = SkipListMap()
    nb = 100000
    nbkeys = nb * 1
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    #Access
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        try:
            M[key]
        except KeyError:
            pass
    apres = time.time()
    print( "Access of", nb, "keys in ", apres-avant, "seconds." )

    #Delete
    avant = time.time()
    nbdel = 0
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        try:
            del M[key]
        except KeyError:
            pass
    apres = time.time()
    print( "Delete ", nb, "keys in ", apres-avant, "seconds." )


#     M = SkipListMap( "A", "Z" )
#     print( len( M ) ) #0
#     M['K'] = 2
#     M['B'] = 4
#     M['U'] = 2
#     M['V'] = 8
#     M['K'] = 9
#     print( M )
#     print( M.get('B') )
#     print( M.get('X') )
#     print( M.get( 'F' ) )
#     print( M.get( 'F', 5 ) )
#     print( M.get( 'K', 5 ) )
#     print( M )
#     print( len( M ) )
#     del M['V']
#     print( "pop(K) = ", M.pop( 'K' ) )
#     print( M )
#     for key in M.keys():
#         print( str( key ) )
#     for value in M.values():
#         print( str( value ) )
#     for item in M.items():
#         print( str( item ) )
#     print( M.setdefault( 'B', 1 ) )
#     print( M.setdefault( 'AA', 1 ) )
#     print( M )
#     print( M.popitem() )
#     print( M )
#     print( M.find_min() )
#     print( M.find_max() )

#     M = SkipListMap()
#     nb = 50
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()
#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
#     print( "Skip List Height for ", nb, "keys is ", M._T._height, "." )
#     print( M )

#     print( M.find_min() )
#     print( M.find_max() )

#     print( 'ge(25)' )
#     print( M.find_ge( 25 ) )
#     print( 'gt(25)' )
#     print( M.find_gt( 25 ) )
#     print( 'le(25)' )
#     print( M.find_le( 25 ) )
#     print( 'lt(25)')
#     print( M.find_lt( 25 ) )
#     print( 'lt(0)' )
#     print( M.find_lt( 0 ) )

#     print( 'range(10,50)' )
#     for (x,y) in M.find_range( 10, 50 ):
#         print( "x =", x, ", y =", y )

#     for x in M:
#         print( x )
    
    print( "End of testing." )
