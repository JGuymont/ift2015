#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "7 november 2018"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.2 Hachage

from random import randrange

#class Compression pour tables de hachage
class Compression:

    #constructeur de compresseur selon la taille et un nombre premier p
    #avec 2 options pour la fonction de compression: division et MAD
    def __init__( self, size = 11, p = 109345121 ): # puissance de 2 à tester 134217728
        self._size = size
        self._p = p
        #pour MAD on détermine une échelle et un décalage
        #on trouve un entier multiplicateur entre 1 et p-2
        #qui n'est pas un multipe de p
        trouve = False
        while not trouve:
            self._scale = 1 + randrange( self._p - 1 )
            if not ( self._scale % self._p ) == 0:
                trouve = True
        #on trouve un entier décalage entre 0 et p-1
        self._shift = randrange( self._p )

    #option division, on prend le modulo avec la taille
    def divide( self, hcode ):
        return hcode % self._size

    #option MAD, on prend (hcode * scale + shift) % p % taille
    def mad( self, hcode ):
        return ( hcode * self._scale + self._shift ) % self._p % self._size

#unit testing
if __name__ == '__main__':

    print( "Compression unit testing..." )

    h = 32411 # nombre premier à tester 32411
    #on crée un compresseur pour h entrées
    compressor = Compression( h )
    #on rempli la table à 80%
    n = int( h * 0.8 )
    #on simule k fois
    k = 5000
    #initialisation d'un compteur de collisions
    colldiv = 0
    collmad = 0
    #pour k fois
    for j in range( 0, k ):
        #initialisation d'un ensemble vide
        #pour imiter les entrées d'un table de hachage
        sdiv = set()
        smad = set()
        #pour 80% de la taille de la table
        for i in range( 0, n ):
            #on génère un hashcode au hasard entre 0 et 10*h - 1
            hc = randrange( h * 10 )
            #on favorise les hc pairs
            #if not( hc % 2 == 0 ) and randrange( 2 ) == 1:
                #on rend pair 1 fois sur 2 un hashcode impair
            #    hc += 1
            #on compresse le hashcode dans la table
            hccdiv = compressor.divide( hc )
            hccmad = compressor.mad( hc )
            #on vérifie s'il y a collision ou non
            if hccdiv in sdiv:
                #si oui, on la compte
                colldiv += 1
            else:
                #si non, on ajoute le hashcode compressé dans l'ensemble
                sdiv.add( hccdiv )
            #on vérifie s'il y a collision ou non
            if hccmad in smad:
                #si oui, on la compte
                collmad += 1
            else:
                #si non, on ajoute le hashcode compressé dans l'ensemble
                smad.add( hccmad )

    print( "Number of collisions on average for", n, "entries in a table of size", h, "with division is", colldiv/k )
    print( "Number of collisions on average for", n, "entries in a table of size", h, "with MAD is", collmad/k )

    print( "end unit testing..." )
