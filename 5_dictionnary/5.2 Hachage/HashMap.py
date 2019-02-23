#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "7 november 2018"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.2 Hachage

from Map import Map
from random import randrange

#classe HashMap utilisant MAD
class HashMap( Map ):

    def __init__( self, cap = 11, p = 109345121 ):
        self._T = cap * [None]               #table de hachage de cap entrées
        self._n = 0                          #nombre d'éléments dans la table
        self._prime = p                      #nombre premier pour la compression MAD
        #pour MAD on détermine une échelle et un décalage
        self._scale = 1 + randrange( p - 1 ) #scale entre 1 et p-2
        #on trouve un entier multiplicateur entre 1 et p-2
        #qui n'est pas un multipe de p
        trouve = False
        while not trouve:
            self._scale = 1 + randrange( p - 1 )
            if not ( self._scale % p ) == 0:
                trouve = True
        self._shift = randrange( p )         #shift entre 0 et p-1
        self._mask = cap

    #fonction de hachage avec compression MAD
    def _hash_function( self, k ):
        return( hash( k ) * self._scale + self._shift ) % self._prime % self._mask

    #taille (nombre d'éléments) dans la table
    def __len__( self ):
        return self._n

    #on utilise des bucket qui seront implémentés
    #dans les sous-classes de HashMap
 
    #accession à l'élément de clé k en O(1) espéré
    def __getitem__( self, k ):
        #on calcule l'index du bucket
        j = self._hash_function( k )
        #on accède à l'élément de clé k dans le bucket
        tmp = self._bucket_getitem( j, k )
        if not tmp:
            raise KeyError
        else:
            return tmp

    #insetion d'un élément (k, v) en O(1) espéré
    def __setitem__( self, k, v ):
        #on calcule l'index du bucket
        j = self._hash_function( k )
        #on insère l'élément de clé k dans le bucket
        self._bucket_setitem( j, k, v )
        #si le nombre d'éléments dépasse 50% de la taille de la table
        #on la double
        if self._n > len( self._T ) // 2:
            self._resize( 2 * len( self._T ) - 1 )

    #suppression de l'élément de clé k en O(1) espéré
    def __delitem__( self, k ):
        #on calcule l'index du bucket
        j = self._hash_function( k )
        #on retire l'élément du bucker
        succes = self._bucket_delitem( j, k )
        #on décrément la taille si l'élément
        #a bel et bien été supprimé (s'il existait)
        if succes:
            self._n -= 1
        else:
            raise KeyError

    #redimensionnement de la table à capacité c
    def _resize( self, c ):
        #on insère tous les éléments de la table dans une liste
        old = list( self.items() )
        #on crée une nouvelle table avec la nouvelle capacité
        self._T = c * [None]
        #on réinitialise la taille de la table à 0
        self._n = 0
        #on redéfinit le mask à la nouvelle capacité
        self._mask = c
        #on insère les éléments de l'ancienne table un à un
        #cette opération est dans O(n) en temps
        for (k,v) in old:
            self[k] = v
