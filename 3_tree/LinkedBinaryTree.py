#!/usr/local/bin/python3

from BinaryTree import BinaryTree

# implémentation de BinaryTree avec des noeuds chaînés
class LinkedBinaryTree(BinaryTree):
    """Binary tree implementation using linked nodes"""
    
    class _Node:
        
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def __str__(self):
            return str(self._node._element)

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type( other ) is type( self ) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate( p )
        return self._make_position( node._right )

    def num_children(self, p):
        node = self._validate( p )
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: 
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: 
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError( 'Right child exists' )
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: 
            raise ValueError( 'p has two children' )
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf( p ): 
            raise ValueError('position must be leaf')
        if not type( self ) is type( t1 ) is type( t2 ):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

# unit testing
if __name__ == '__main__':
    """
             A
       B           D
    E     F     C     J
        G   H
    """

    mytree = LinkedBinaryTree()
    A = mytree._add_root("A")   #level 0
    
    B = mytree._add_left(A, "B")   #level 1
    D = mytree._add_right(A, "D")
    
    E = mytree._add_left(B, "E") #level 2 left
    F = mytree._add_right(B, "F")
    
    mytree._add_left( D, "C" ) #level 2 right
    mytree._add_right( D, "J" )

    mytree._add_left( F, "G" ) #level 3 
    mytree._add_right( F, "H" )

    print( "breadth-first:" )
    mytree.breadth_first_print( mytree.root() )
    print( "---" )

    exit()
    
    print( "inorder:" )
    mytree.inorder_print( mytree.root() )
    print( "---" )

    print( "preorder:" )
    mytree.preorder_print( mytree.root() )
    print( "---" )
    exit()
    print( "postorder:" )
    mytree.postorder_print( mytree.root() )
    print( "---" )

    print( mytree.height( mytree.root() ) )

    # printExpression
    aSecondTree = LinkedBinaryTree()
    plus = aSecondTree._add_root( '+' )
    times1 = aSecondTree._add_left( plus, 'x' )
    times2 = aSecondTree._add_right( plus, 'x' )
    deux = aSecondTree._add_left( times1, '2' )
    minus = aSecondTree._add_right( times1, '-' )
    a = aSecondTree._add_left( minus, 'a' )
    un = aSecondTree._add_right( minus, '1' )
    trois = aSecondTree._add_left( times2, '3' )
    b = aSecondTree._add_right( times2, 'b' )
    aSecondTree.printExpression( aSecondTree.root() )


    
