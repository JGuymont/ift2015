#!/usr/local/bin/python3

from Map import Map
import random
import time


class UnsortedListMap(Map):
    """Implémentation de Map avec une liste non triée"""

    def __init__( self ):
        self._T = []

    def __getitem__( self, k ):
        """
        accède à l'élément de clé k en O(n) en pire cas
        retourne l'élément si présent, None sinon
        """
        for item in self._T:
            if k == item._key:
                return item._value
        raise KeyError(k)

    def __setitem__( self, k, v ):
        """
        insertion d'un élément de clé k en O(n) en pire cas.
        If the key exist, overwrite the value.
        """
        for item in self._T:
            if k == item._key:
                item._value = v
                return
        self._T.append(self._Item(k, v))

    def __delitem__( self, k ):
        """
        suppression de l'élément de clé k en O(n) en pire cas
        soulève une erreur si la clé n'existe pas
        """
        for j in range(len(self._T)):
            if k == self._T[j]._key:
                self._T.pop(j)
                return
        raise KeyError(k)

    def __len__(self):
        return len(self._T)

    def __iter__(self):
        for item in self._T:
            yield item._key

    def __contains__( self, k ):
        """
        appartenance de la clé k en O(n) en pire cas
        """
        try:
            self[k]
            return True
        except:
            return False

    def __items__(self):
        """
        itérateur de (clé, valeur)
        """
        for item in self._T:
            yield (item._key, item._value)


if __name__ == '__main__':
    # simple unit testing

    map = UnsortedListMap()

    map['a'] = 1

    print(map['a'])




















    exit()

    print( "UnsortedListMap unit testing..." )

    M = UnsortedListMap()

    nb = 5
    nbkeys = nb * 1
    random.seed( 131341 )

    #insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        M[key] = key
    apres = time.time()
    nbreal = len( M )
    print( "Insertion of", nbreal, "(over", nb, "attempts) keys in ", apres-avant, "seconds." )

    #accès
    avant = time.time()
    for i in range( nb ):
        M.get( key )
#         try:
#             x = M[key]
#         except KeyError:
#             pass
    apres = time.time()
    print( "Access to", nb, "keys in ", apres-avant, "seconds." )

    #insertion dans list Python
    l = []
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        l.append( key )
    apres = time.time()
    print( "Insertion of", nb, "keys in a list takes ", apres-avant, "seconds." )

    #accès dans list Python
    count = 0
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nbkeys )
        try:
            l.index( key )
        except ValueError:
            count += 1
    apres = time.time()
    print( "Access of", nb, "keys in a list takes ", apres-avant, "seconds." )

    M.clear()
    print( len( M ) ) #0
    M['K'] = 2
    M['B'] = 4
    M['U'] = 2
    M['V'] = 8
    M['K'] = 9
    print( M['B'] )
    print( M.get( 'F' ) )
    print( M.get( 'F', 5 ) )
    print( M.get( 'K', 5 ) )
    print( len( M ) )
    del M['V']
    print( M.pop( 'K' ) )
    for key in M.keys():
        print( str( key ) )
    for value in M.values():
        print( str( value ) )
    print( "items:")
    for item in M.items():
        print( str( item ) )
    print( M.setdefault( 'B', 1 ) )
    print( M.setdefault( 'A', 1 ) )
    print( M )
    print( M.popitem() )
    
    print( "End of testing." )

