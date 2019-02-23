from dynamic_array import DynamicArray

class ListStack:

    def __init__( self ):
        self._A = []

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        pp = str(self._A)
        # pp += "(size = " + str( len( self._A ) )
        # pp += ")[top = " + str( len( self._A ) - 1 ) + "]"
        return pp

    # push implémenté avec append
    def push( self, obj ):
        self._A.append( obj )

    # pop implémenté avec pop
    # si l'opération échoue, on retourne None
    def pop( self ):
        try:
            return self._A.pop( )
        except IndexError:
            return None

    # top est le dernier élément
    def top( self ):
        if self.is_empty():
            return None
        else:
            return self._A[len( self._A ) - 1]

class ArrayStack:

    def __init__( self ):
        self._A = DynamicArray()

    def __len__( self ):
        return len( self._A )

    def is_empty( self ):
        return len( self._A ) == 0

    def __str__( self ):
        pp = str(self._A)
        # pp += "(size = " + str( len( self._A ) )
        # pp += ")[top = " + str( len( self._A ) - 1 ) + "]"
        return pp

    # push implémenté avec append
    def push( self, obj ):
        self._A.append( obj )

    # pop implémenté avec pop
    # si l'opération échoue, on retourne None
    def pop( self ):
        try:
            return self._A.pop( )
        except IndexError:
            return None

    # top est le dernier élément
    def top( self ):
        if self.is_empty():
            return None
        else:
            return self._A[len( self._A ) - 1]