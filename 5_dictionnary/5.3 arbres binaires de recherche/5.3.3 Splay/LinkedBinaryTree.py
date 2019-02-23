#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Arbres
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# utilise BinaryTree (BinaryTree.py)
from BinaryTree import BinaryTree

# implémentation de BinaryTree avec des noeuds chaînés
class LinkedBinaryTree( BinaryTree ):
    
    # classe imbriquée _Node
    class _Node:
        # crée une structure statique pour _Node utilisant __slots__
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__( self, element,
                      parent = None,
                      left = None,
                      right = None ):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    # classe imbriquée Position, une sous-classe de BinaryTree.Position
    class Position( BinaryTree.Position ):

        # constructeur
        # le container (l'arbre) et une référence au noeud sont requis
        # le noeud est de type _Node
        def __init__( self, container, node ):
            self._container = container
            self._node = node

        def __str__( self ):
            return str( self._node._element )

        def element( self ):
            return self._node._element

        # deux Positions sont équivalente si elles sont du même type
        # et réfèrent au même noeud
        def __eq__( self, other ):
            return type( other ) is type( self ) and other._node is self._node

    # retourne le noeud d'une Position si valide
    # soit, une instance de Position du même container existante
    def _validate( self, p ):
        if not isinstance( p, self.Position ):
            raise TypeError( 'p must be proper Position type' )
        if p._container is not self:
            raise ValueError( 'p does not belong to this container' )
        # si p a été deleté (_parent pointe à lui-même: see _delete plus bas)
        if p._node._parent is p._node:
            raise ValueError( 'p is no longer valid' )
        return p._node

    #retourne une instance de Position pour un noeud donné (None sinon)
    def _make_position( self, node ):
        return self.Position( self, node ) if node is not None else None

    # constructeur d'un BinaryTree
    # crée un arbre binaire vide
    def __init__( self ):
        self._root = None
        self._size = 0

    # retourne la taille
    def __len__( self ):
        return self._size

    # retourne la racine
    def root( self ):
        return self._make_position( self._root )

    # retourne le parent d'une Position si valide
    def parent( self, p ):
        node = self._validate( p )
        return self._make_position( node._parent )

    # retourne l'enfant gauche d'une Position si valide
    def left( self, p ):
        node = self._validate( p )
        return self._make_position( node._left )

    # retourne l'enfant droit d'une Position si valide
    def right( self, p ):
        node = self._validate( p )
        return self._make_position( node._right )

    # retourne le nombre d'enfants d'une Position si valide
    def num_children( self, p ):
        node = self._validate( p )
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # méthodes du niveau développeur

    # ajoute la racine avec valeur e, si elle n'existe pas déjà
    # retourne sa Position
    def _add_root( self, e ):
        if self._root is not None: raise ValueError( 'Root exists' )
        # taille devient 1
        self._size = 1
        # on crée un noeud pour la racine et retourne sa Position
        self._root = self._Node( e )
        return self._make_position( self._root )

    # ajoute un enfant à gauche de valeur e à une Position
    # si elle est valide et si cet enfant n'existe pas déjà
    def _add_left( self, p, e ):
        node = self._validate( p )
        if node._left is not None: raise ValueError( 'Left child exists' )
        # on incrémente la taille
        self._size += 1
        # on crée un noeud pour l'enfant et on retourne sa Position
        node._left = self._Node( e, node )
        return self._make_position( node._left )

    # ajoute un enfant à droite de valeur e à une Position
    # si elle est valide et si cet enfant n'existe pas déjà
    def _add_right( self, p, e ):
        node = self._validate( p )
        if node._right is not None: raise ValueError( 'Right child exists' )
        # on incrémente la taille
        self._size += 1
        # on crée un noeud pour l'enfant et on retourne sa Position
        node._right = self._Node( e, node )
        return self._make_position( node._right )

    # remplace l'élément d'une Position si valide
    # retourne l'ancien élément
    def _replace( self, p, e ):
        #on valide p
        node = self._validate( p )
        #on retient l'ancien élément, à retourner
        old = node._element
        #on remplace l'élément du node par e
        node._element = e
        return old

    # delete une Position si valide
    # la remplace par son enfant s'il y en a un (mais pas 2!)
    # retourne l'élément deleté
    def _delete( self, p ):
        # validation de la Position
        node = self._validate( p )
        # doit avoir au plus 1 enfant
        if self.num_children( p ) == 2: raise ValueError( 'p has two children' )
        # on prend l'enfant existant ou None s'il n'y en a aucun
        child = node._left if node._left else node._right
        # s'il y a un enfant, il est adopté par son grand-parent
        # ou par personne s'il n'en a pas
        if child is not None:
            child._parent = node._parent
        # si la Position était la racine, la nouvelle racine
        # devient l'enfant
        if node is self._root:
            self._root = child
        # sinon, on remplace le noeud par son enfant
        # de gauche s'il était enfant gauche
        # de droite s'il était enfant droit
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        # on décrémente la taille
        self._size -= 1
        # on rend la Position invalide (en mettant parent sur lui même)
        node._parent = node
        # on retourne l'élément deleté 
        return node._element

    # attache des sous-arbres gauche et droit à une Position feuille si valide
    def _attach( self, p, t1, t2 ):
        # validation de p
        node = self._validate( p )
        # s'assurer que c'est une feuille
        if not self.is_leaf( p ): raise ValueError( 'position must be leaf' )
        # s'assurer que les types des sous-arbres sont compatibles
        if not type( self ) is type( t1 ) is type( t2 ):
            raise TypeError( 'Tree types must match' )
        # augmenter la taille de celles des deux sous-arbres attachés
        self._size += len( t1 ) + len( t2 )
        # on attache un sous-arbre non vide
        # en mettant son parent à la feuille d'attache
        # en mettant à None sa racine et à 0 sa taille
        # cet arbre n'existera plus de manière individuelle
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

    mytree = LinkedBinaryTree()

    #level 0
    A = mytree._add_root( "A" )

    #levels
    B = mytree._add_left( A, "B" )

    D = mytree._add_left( B, "D" )
    H = mytree._add_left( D, "H" )
    M = mytree._add_left( H, "M" )
    N = mytree._add_right( H, "N" )
    E = mytree._add_right( B, "E" )
    I = mytree._add_left( E, "I" )
    J = mytree._add_right( E, "J" )
    C = mytree._add_right( A, "C" )
    G = mytree._add_right( C, "G" )
    L = mytree._add_right( G, "L" )
    R = mytree._add_right( L, "R" )
    Q = mytree._add_left( L, "Q" )
    K = mytree._add_left( G, "K" )
    O = mytree._add_left( K, "O" )
    P = mytree._add_right( K, "P" )
    F = mytree._add_left( C, "F" )
    
    print( "inorder:" )
    mytree.inorder_print( mytree.root() )
    print( "---" )

    print( "preorder:" )
    mytree.preorder_print( mytree.root() )
    print( "---" )

    print( "postorder:" )
    mytree.postorder_print( mytree.root() )
    print( "---" )

    print( "breadth-first:" )
    mytree.breadth_first_print( mytree.root() )
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


    
