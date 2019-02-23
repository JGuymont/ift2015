#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

import random

#class Coin pour flipper des coins
class Coin:

    def flip( self ):
        return random.randint( 0, 1 ) == 0

#unit testing
if __name__ == '__main__':

    print( "Coin unit testing..." )

    coin = Coin()
    for i in range( 0, 10 ):
        print( coin.flip() )

    print( "end unit testing..." )
