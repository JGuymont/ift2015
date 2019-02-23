#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

from Map import Map
import random
import time

class SortedListMap( Map ):

    #recherche dichotomique pour trouver en O(log n) en pire cas la clé k
    #vue en section 1 Mise à niveau/1.4 Récursivité
    #retourne j, l'index de l'élément le plus à gauche avec clé >= k :
    #tel que T[low:j] ont des clés < k
    #        T[j:high+1] ont des clés >= k
    #j retourné est entre 0 et len( self )
    def _find_index( self, k, low, high ):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._T[mid]._key:
                return mid
            elif k < self._T[mid]._key:
                return self._find_index( k, low, mid - 1 )
            else:
                return self._find_index( k, mid + 1, high )

    #utilise la list de Python
    def __init__( self ):
        self._T = []

    #taille de la Map
    def __len__( self ):
        return len( self._T )

    #accède l'élément de clé k
    #bénificie de la liste triée pour le faire en O(log n)
    def __getitem__( self, k ):
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #j == len(T) ou T[j] != k => non trouvée
        if j == len( self._T ) or self._T[j]._key != k:
            raise KeyError( k )
        return self._T[j]._value

    #insertion d'un élément de clé k et valeur v
    #bénificie de la liste triée pour trouver l'index d'insertion en O(log n)
    def __setitem__( self, k, v ):
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #si j < len(T) et clé de T[j] == k => clé existe
        #donc on remplace sa valeur par v
        if j < len( self._T ) and self._T[j]._key == k:
            self._T[j]._value = v
        else:
            #clé n'existe pas, on insère un nouvel élément
            self._T.insert( j, self._Item( k, v ) )

    #suppression de l'élément de clé k
    #bénificie de la liste triée pour trouver son index en O(log n)
    #soulève une erreur si la clé n'existe pas
    def __delitem__( self, k ):
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #si j == len(T) ou clé de T[j] diffère de k => non trouvée
        if j == len( self._T ) or self._T[j]._key != k:
            raise KeyError( k )
        self._T.pop( j )

    #itérateur sur les clés de la Map
    def __iter__( self ):
        for item in self._T:
            yield item._key

    #itérateur sur les clés dans l'ordre inverse
    def __reversed__( self ):
        for item in reversed( self._T ):
            yield item._key

    #trouve et retourne l'élément avec la plus petit clé
    #si la Map n'est pas vide
    def find_min( self ):
        if len( self._T ) > 0:
            return ( self._T[0]._key, self._T[0]._value )
        else:
            return None

    #trouve et retourne l'élément avec la plus grande clé
    #si la Map n'est pas vide
    def find_max( self ):
        if len( self._T ) > 0:
            return ( self._T[-1]._key, self._T[-1]._value )
        else:
            return None

    #trouve et retourne l'élément avec la première clé >= k
    #si il existe
    def find_ge( self, k ):
        j = self._find_index( k, 0, len( self._T ) - 1 )
        if j < len( self._T ):
            return ( self._T[j]._key, self._T[j]._value )            
        else:
            #j >= len(T) => non trouvé
            return None

    #trouve et retourne l'élément avec la première clé <= k
    #si il existe
    def find_le( self, k ):
        #si la Map est vide, il n'existe pas
        if( len( self._T ) ) == 0:
            return None
        #sinon, on trouve j tel que clé de T[j] >= k
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #si k est > que la plus grande clé
        #on retourne le dernier élément (celui de la plus grande clé)
        if j >= len( self._T ):
            return ( self._T[j-1]._key, self._T[j-1]._value )
        #si on a trouvé un clé à l'intérieur de la liste mais
        #que cette clé ne correspond par à k => elle est > k
        #alors on retourne l'élément précédent
        if self._T[j]._key != k:
            j -= 1
        #si cet élément n'était pas l'élément de la plus petite clé
        #on le retourne
        if j >= 0:
            return ( self._T[j]._key, self._T[j]._value )
        else:
            #sinon, il n'existe pas d'élément avec une clé <= k
            return None

    #trouve et retourne l'élément avec la première clé > k
    #si il existe
    def find_gt( self, k ):
        #si la Map est vide, il n'existe pas
        if( len( self._T ) ) == 0:
                return None
        #sinon, on trouve j tel que clé de T[j] >= k
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #si j < len(T) et que la clé de T[j] == k
        #alors on retourne l'élément suivant
        if j < len( self._T ) and self._T[j]._key == k:
            j += 1
        #si cet élément suivant est toujours dans la liste
        #on le retourne
        if j < len( self._T ):
            return ( self._T[j]._key, self._T[j]._value )
        else:
            #sinon, l'élément k est le plus grand de la Map
            #et, donc, il n'en existe pas de plus grand
            return None

    #trouve et retourne l'élément avec la première clé < k
    #si il existe
    def find_lt( self, k ):
        #si la Map est vide, il n'existe pas
        if( len( self._T ) ) == 0:
                return None
        #sinon, on trouve j tel que clé de T[j] >= k
        j = self._find_index( k, 0, len( self._T ) - 1 )
        #si j < len(T) et que la clé de T[j] > k
        #alors on prend l'élément précédent
        #si la clé de T[j] == k, on a un élément dont la clé est égale
        #et on veut l'élément de clé plus petite
        #si la clé de T[j] n'est pas égale à k, elle est la première > k
        #et on veut l'élément de clé plus petite
        if j < len( self._T ) and self._T[j]._key > k :
            j -= 1
        #si ce n'était pas la plus petite clé de la Map
        #alors on le retourne
        if j >= 0:
            return ( self._T[j]._key, self._T[j]._value )
        else:
            #sinon, l'élément de clé k est le plus petit de la Map
            #et, donc, il n'en existe pas de plus petit
            return None

    #itérateur d'éléments de la Map avec start <= clé < stop
    def find_range( self, start, stop ):
        #si start est None, on commence au début de la Map
        if start is None:
            j = 0
        #sinon, on trouve l'index de l'élément de clé >= start
        else:
            j = self._find_index( start, 0, len( self._T ) - 1 )
        #on itère sur les élément j <= clé < stop
        #on teste j < len(T), puisque j pourrait correspondre
        #à une clé > la plus grande clé dans la Map
        while j < len( self._T ) and (stop is None or self._T[j]._key < stop):
            yield ( self._T[j]._key, self._T[j]._value )
            j += 1

#unit testing
if __name__ == '__main__':

    print( "SortedListMap unit testing..." )

    M = SortedListMap()

    nb = 1000000
    nbkeys = nb * 1
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        M[key] = key
    apres = time.time()
    nbreal = len( M )
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    #Access
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        M.get( key )
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

#     M = SortedListMap()

#     print( len( M ) ) #0
#     M['K'] = 2
#     M['B'] = 4
#     M['U'] = 2
#     M['V'] = 8
#     M['K'] = 9
#     print( M['B'] )
#     print( M.get( 'F' ) )
#     print( M.get( 'F', 5 ) )
#     print( M.get( 'K', 5 ) )
#     print( len( M ) )
#     del M['V']
#     print( M.pop( 'K' ) )
#     for key in M.keys():
#         print( str( key ) )
#     for value in M.values():
#         print( str( value ) )
#     for item in M.items():
#         print( str( item ) )
#     print( M.setdefault( 'B', 1 ) )
#     print( M.setdefault( 'A', 1 ) )
#     print( M )
#     print( M.popitem() )    

#     M = SortedListMap()

#     nb = 50
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()

#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
#     print( M )
#     print( M.find_ge( 6 ) )
#     print( M.find_gt( 6 ) )
#     print( M.find_le( 6 ) )
#     print( M.find_lt( 6 ) )
#     for (x,y) in M.find_range( 12, 38 ):
#         print( "x =", x, ", y =", y )

    print( "End of testing." )
