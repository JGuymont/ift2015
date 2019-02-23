#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/ADT List
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# List implémentée avec un tableau dynamique
# On a besoin de DynamicArray
from DynamicArray import DynamicArray
# et de l'interface de l'ADT List
from List import List

# la classe ArrayList hérite de l'interface List
class ArrayList( List ):

    # implémente l'ADT List (List.py)
    # utilise la classe DynamicArray (DynamicArray.py)
    def __init__( self ):
        self._A = DynamicArray()

    # retourne le nombre d'éléments
    def __len__( self ):
        return len( self._A )

    # retourne une chaîne de caractères représentant la liste
    def __str__( self ):
        return str( self._A )

    # accès avec notation des crochets
    def __getitem__( self, k ):
        return self._A[k]

    # ajoute l'élément obj à la fin de la liste
    def append( self, obj ):
        self._A.append( obj )

    # retire le ième élément de la liste
    def remove( self, i ):
        return self._A.remove( i )

    # retourne l'index de l'élément obj s'il existe
    def find( self, obj ):
        return self._A.find( obj )

"""unit testing
"""
if __name__ == '__main__':

    data = ArrayList()
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
