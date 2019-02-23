#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "9 février 2014"
#
# Programme Python pour IFT2015/Types abstraits/Liste
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Implémentation de List avec une liste Python
from List import List

class ListList( List ):

    # Implémente l'ADT List avec une liste Python
    def __init__( self ):
        self._A = []

    # retourne le nombre d'éléments
    def __len__( self ):
        return len( self._A )

    # retourne une chaîne de caractères représentant la liste
    # sans capacité
    def __str__( self ):
        pp = str( self._A )
        pp += "(size = " + str( len( self._A ) ) + ")"
        return pp

    # accès avec notation des crochets
    def __getitem__( self, k ):
        return self._A[k]

    # ajoute l'élément obj à la fin de la liste
    def append( self, obj ):
        self._A.append( obj )

    # retire le ième élément de la liste
    def remove( self, i ):
        # vérifie si l'index est valide
        if not 0 <= i < len( self._A ):
            raise IndexError( 'ListList: index out of bounds' )
        else:
            # si oui, on garde une référence sur l'élément à retourner
            obj = self._A[i]
            # on retire l'élément de la liste
            self._A.pop( i )
            return obj

    # retourne l'index de l'élément obj s'il existe
    # sinon None
    def find( self, obj ):
        # utilise le système d'exceptions
        try:
            idx = self._A.index( obj )
        except ValueError:
            return None
        # index a réussi
        return idx

"""unit testing
"""
if __name__ == '__main__':

    data = ListList()
    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    print( data )

    idx = data.find( 'titi' )
    if idx is not None:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx is not None:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove 0 =", data.remove( 0 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )
    print( "remove 1 = ", data.remove( 1 ) )
    print( data )
    print( "remove 0 = ", data.remove( 0 ) )
    print( data )

