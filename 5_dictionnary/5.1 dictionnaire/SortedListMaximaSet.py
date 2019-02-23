#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

from SortedListMap import SortedListMap
import time
import random

#classe pour un Maxima Set implantée avec SortedListMap
class SortedListMaximaSet():

    #constructeur
    def __init__( self ):
        self._M = SortedListMap()

    #prettyprint
    def __str__( self ):
        return str( self._M )

    #ajouter un point au Maxima Set
    def add( self, x, y ):
        #ne pas considérer (x,y) s'il existe un point
        #équivalent ou meilleur
        other = self._M.find_le( x )
        if other is not None and other[1] >= y:
            return
        #sinon, on l'ajoute à l'ensemble
        self._M[x] = y
        #éliminer les points dont le 1er critère est > x
        #et qui ne peuvent pas être justifiés un 2ème critère > y
        #on prend le premier point défavorisé par x
        other = self._M.find_gt( x )
        #on l'élimine s'il est également défavorisé par y
        while other is not None and ( other[1] <= y ):
            del self._M[other[0]]
            other = self._M.find_gt( x )

# unit testing
if __name__ == '__main__':

    print( "SortedListMaximaSet unit testing..." )

    M = SortedListMaximaSet()

#     M.add( 15000,  50 ) # a
#     M.add( 18000,  80 ) # b
#     M.add( 22000,  85 ) # c
#     M.add( 24000,  90 ) # d
#     M.add( 25000,  95 ) # e
#     M.add( 30000, 120 ) # f
#     M.add( 32000, 125 ) # g
#     M.add( 35000, 140 ) # h
#     print( M )
#     #esseyons p = ( 20000, 40 )
#     #plus chère que toute autre voiture plus performante
#     #on ne garde pas cette option
#     M.add( 20000,  40 ) # eliminate
#     print( M )
#     #esseyons p = ( 20000, 100 )
#     #plus chère mais plus performante que certains points
#     #on garde l'option, qui en élimine d'autres
#     M.add( 20000, 100 ) # p
#     print( M )


    nb = 4000000
    random.seed( 131341 )

    avant = time.time()
    for i in range( nb ):
        x = random.randint( 9000, 300000 )
        y = random.randint(   50,    300 )
        M.add( x, y )
    apres = time.time()
    print( "Add", nb, "(x,y) pairs, x in [9000..300000], y in [50...300] in ", apres-avant, "seconds." )

    print( M )

    print( "End of testing." )
