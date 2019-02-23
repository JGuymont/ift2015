from DoublyLinkedList import DoublyLinkedList

class PositionalList(DoublyLinkedList):

    class Position:
        """Abstraction for the position of an element"""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__( self, other ):
            # retourne True si other est du même type et réfère au même noeud
            return type(other) is type(self) and other._node is self._node

        def __ne__( self, other ):
            return not self == other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError( "p must be proper Position type" )
        if p._container is not self:
            raise ValueError( "p does not belong to this container" )
        if p._node.next is None: #convention pour noeud désassigné
            raise ValueError( "p is no longer valid" )
        return p._node

    def _make_position( self, node ):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position( self, node )

    def first(self):
        return self._make_position(self._head.next)

    def last( self ):
        return self._make_position(self._tail.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        #itérateur des éléments de la liste
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after( cursor )

    def insert(self, e):
        node = super().insert(e)
        return self._make_position(node)

    def append( self, e ):
        node = super().append(e)
        return self._make_position(node)

    def replace(self, p, e):
        #remplace l'élément p par e
        #retourne l'élément qui était à la position p
        original = self._validate( p )
        old_value = original.element
        original.element = e
        return old_value

    def move_to_front(self, p):
        node = self._validate(p)
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self._head.next.prev = node # |head|(node)|head.next|
        node.next = self._head.next
        node.prev = self._head
        self._head.next = node
        return p


# unit testing
if __name__ == '__main__':

    data = PositionalList()
    data.append('titi')
    data.append( 'toto' )
    data.append( 'tata' )
    print(data)
    f = data.last()
    data.move_to_front(f)
    print(data)
    exit()
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
#    print( "remove 1 = ", data.remove( 1 ) )
#    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    data.append( 'holo' )
    data.append( 'asma' )
    print( data )

    idx = data.find( 'titi' )
    if idx:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove 2 =", data.remove( 2 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )

    f = data.first()
    print( f )
    print( f.element() )
    g = data.after( f )
    print( g.element() )
    data.replace( g, "bonjour" )
    print( "iterer les valeurs :" )
    for _ in data:
        print( _ )
    
