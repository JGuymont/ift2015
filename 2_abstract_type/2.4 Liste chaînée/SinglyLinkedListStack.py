"""Programme pour le cours IFT2015
   Écrit par François Major le 16 février 2014.
"""

from SinglyLinkedList import SinglyLinkedList
from Stack import Stack

class SinglyLinkedListStack( Stack ):

    #implements the ADT Stack (Stack.py)
    #uses SinglyLinkedList (SinglyLinkedList.py)
    def __init__( self ):
        self._A = SinglyLinkedList()

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        if self._A.is_empty():
            return "[](size = 0)[top = None]"
        else:
            pp = str( self._A )
            pp += "[top = 1]"
            return pp

    #push obj
    def push( self, obj ):
        self._A.insert( obj )

    #pop
    def pop( self ):
        try:
            return self._A.remove( 0 )
        except IndexError:
            return None

    #top
    def top( self ):
        return self._A.first()

"""unit testing
"""
if __name__ == '__main__':

    data = SinglyLinkedListStack()
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
    print( "pop = ", data.pop() )
    print( "pop = ", data.pop() )
    print( "pop = ", data.pop() )
