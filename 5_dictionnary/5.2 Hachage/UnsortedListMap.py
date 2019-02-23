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

#Implémentation de Map avec une liste non triée
class UnsortedListMap( Map ):

    #on utilise la list Python
    def __init__( self ):
        self._T = []

    #accède à l'élément de clé k en O(n) en pire cas
    #retourne l'élément si présent, None sinon
    def __getitem__( self, k ):
        #on doit parcourir la liste
        for item in self._T:
            if k == item._key:
                return item._value
        raise KeyError( k )

    #insertion d'un élément de clé k en O(n) en pire cas
    def __setitem__( self, k, v ):
        #on doit parcourir la liste
        #car si la clé existe, on change la valeur
        for item in self._T:
            if k == item._key:
                item._value = v
                return
        #si la clé n'existe pas, on ajoute un nouvel élément
        self._T.append( self._Item( k, v ) )

    #suppression de l'élément de clé k en O(n) en pire cas
    #soulève une erreur si la clé n'existe pas
    def __delitem__( self, k ):
        #on doit parcourir la liste
        for j in range( len( self._T ) ):
            if k == self._T[j]._key:
                self._T.pop( j )
                return
        #élément non trouvé : erreur
        raise KeyError( k )

    #taille de la Map
    def __len__( self ):
        return len( self._T )

    #itérateur de clés
    def __iter__( self ):
        for item in self._T:
            yield item._key

    #appartenance de la clé k en O(n) en pire cas
    def __contains__( self, k ):
        try:
            self[k]
            return True
        except:
            return False

    #itérateur de (clé, valeur)
    def __items__( self ):
        for item in self._T:
            yield ( item._key, item._value )

#unit testing
if __name__ == '__main__':

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

