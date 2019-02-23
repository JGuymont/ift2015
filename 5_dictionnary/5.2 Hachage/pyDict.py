#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "7 november 2018"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.2 Hachage

PERTURB_SHIFT = 5

#class Sondage pour mimer le sondage du pyDict
class Sondage:

    def __init__( self, size = 31 ):
        self._size = size

    def sondage( self, hashcode ):
        sondes = []
        j = hashcode % self._size
        perturb = j
        sondes.append( j )
        for k in range( 0, self._size - 1 ):
            j = (5 * j) + 1 + perturb
            #décalage à droite
            perturb >>= PERTURB_SHIFT
            j = j % ( self._size + 1 )
            sondes.append( j )
        print( sondes )

#unit testing
if __name__ == '__main__':

    s = Sondage()
    s.sondage( hash( 3 ) )
