#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

from SkipListMap import SkipListMap
import time
import random

#classe pour un Maxima Set implémenté avec SkipListMap
class SkipListMaximaSet():

    #constructeur
    def __init__( self ):
        self._M = SkipListMap()

    #prettyprint
    def __str__( self ):
        return str( self._M )

    def add( self, x, y ):
        #ne pas considérer (x,y) s'il existe un point
        #équivalent ou meilleur
        other = self._M.find_le( x )
        if ( other is not None ) and ( other[1] >= y ):
            return
        #sinon, l'ajouter
        self._M[x] = y
        #éliminer les points dont le 1er critère est > x
        #et qui ne peuvent pas être justifiés un 2ème critère > y
        #on prend le premier point défavorisé par x
        other = self._M.find_gt( x )
        #on l'élimine s'il est également défavorisé par y
        while ( other is not None ) and ( other[1] <= y ):
            del self._M[other[0]]
            other = self._M.find_gt( x )

# unit testing
if __name__ == '__main__':

    print( "SkipListMaximaSet unit testing..." )

    M = SkipListMaximaSet()

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
