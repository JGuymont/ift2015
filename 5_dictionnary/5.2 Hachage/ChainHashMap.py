#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "7 november 2018"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.2 Hachage

from HashMap import HashMap
from UnsortedListMap import UnsortedListMap
import random
import time

#classe ChaineHashMap pour du hachage avec
#chaînage séparé, càd les buckets sont des
#Map externes à la table
class ChainHashMap( HashMap ):

    #implémentation des fonctions pour les buckets
    
    #accéder à un élément de clé k
    def _bucket_getitem( self, j, k ):
        #j est l'adresse du bucket dans la table
        bucket = self._T[j]
        #si le bucket est vide (n'existe pas)
        #on retourne False
        if bucket is None:
            return False
        #sinon, on retourne l'élément dont la clé est k
        return bucket[k]

    #insertion d'un élément (k, v)
    def _bucket_setitem( self, j, k, v ):
        #si le bucket n'existait pas, on le crée
        #ici une Map non triée
        if self._T[j] is None:
            self._T[j] = UnsortedListMap()
        #on va chercher la taille précédente du bucket
        oldsize = len( self._T[j] )
        #on effectue l'insertion
        self._T[j][k] = v
        #si un élément avec la clé k existait,
        #on a seulement changé sa valeur
        #il ne faut donc pas incrémenter la taille de la table
        if len( self._T[j] ) > oldsize:
            #sinon, on a ajouté l'élément, donc on incérmente la taille
            self._n += 1

    #suppression de l'élément de clé k
    def _bucket_delitem( self, j, k ):
        #j est l'adresse du bucket dans la table
        bucket = self._T[j]
        #si le bucket n'existe pas, l'élément non plus
        if bucket is None:
            return False
        #sinon, on le retire du bucket
        try:
            del bucket[k]
            return True
        except KeyError:
            return False

    #itérateur des clés de la table de hachage
    def __iter__( self ):
        for bucket in self._T:
            if bucket is not None:
                for key in bucket:
                    yield key


#unit testing
if __name__ == '__main__':

    print( "ChainHashMap unit testing..." )

    M = ChainHashMap()

    nb = 1000000
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    #Access
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        try:
            x = M[key]
        except KeyError:
            pass
    apres = time.time()
    print( "Access of", nb, "keys in ", apres-avant, "seconds." )

    #Delete
    avant = time.time()
    nbdel = 0
    for i in range( nb ):
        key = random.randint( 0, nb )
        try:
            del M[key]
        except KeyError:
            pass
    apres = time.time()
    print( "Delete ", nb, "keys in ", apres-avant, "seconds." )

#     print( len( M ) ) #0
#     M['K'] = 2
#     print( M )
#     M['B'] = 4
#     print( M )
#     M['U'] = 2
#     print( M )
#     M['V'] = 8
#     print( M )
#     M['K'] = 9
#     print( M['B'] )
#     print( M['X'] )
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
    
    print( "End of testing." )

