#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/Pile
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

from DynamicArray import DynamicArray
from Stack import Stack

class ArrayStack( Stack ):

    # implémente l'ADT Stack (Stack.py)
    # avec un tableau dynamique (DynamicArray.py)
    def __init__( self ):
        self._A = DynamicArray()

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        pp = str( self._A )
        if self.is_empty():
            pp += "[empty stack]"
        else:
            obj = self.top()
            pp += "[top = " + str( obj ) + ", idx = " + str( len( self._A ) - 1 ) + "]"
        return pp

    # push implémenté avec append
    def push( self, obj ):
        self._A.append( obj )

    # pop récupère l'erreur de DynamicArray
    def pop( self ):
        try:
            return self._A.pop()
        except IndexError:
            return None

    # top implémenté avec get du dernier élément
    def top( self ):
        return self._A.get( len( self._A ) - 1 )

"""unit testing
"""
if __name__ == '__main__':

    data = ArrayStack()
    print( data )

    data.push( 5 )
    print( "push 5" )
    print( data )

    data.push( 3 )
    print( "push 3" )
    print( data )

    print( "len = ", str( len( data ) ) )
    print( "pop = ", data.pop() )
    print( data )

    print( "empty? ", data.is_empty() )
    print( "pop = ", data.pop() )
    print( "empty? ", data.is_empty() )

    print( "pop = ", data.pop() )

    data.push( 7 )
    print( "push 7" )
    print( data )
    data.push( 9 )
    print( "push 9" )
    print( data )
    print( "top = ", data.top() )

    data.push( 4 )
    print( "push 4" )
    print( data )
    print( "len = ", len( data ) )
    print( "pop = ", data.pop() )
    print( data )
    data.push( 6 )
    print( "push 6" )
    data.push( 8 )
    print( "push 8" )
    print( data )
    print( "pop = ", data.pop() )

    print( data )
    print( "pop = ", data.pop() )
    print( data )
    print( "pop = ", data.pop() )
    print( data )
    print( "pop = ", data.pop() )
    print( data )
    print( "pop = ", data.pop() )
    print( data )
