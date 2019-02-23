#!/usr/local/bin/python3
from ListQueue import ListQueue

class Tree:
    """ADT Tree"""

    class Position:
        """inner class Position"""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children of a Position p"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Return an iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the number of nodes in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max( self.height(c) for c in self.children(p))

    # imprime le sous-arbre dont la racine est la Position p
    # utilise un parcours préfixé
    def preorder_print( self, p, indent = "" ):
        # on traite le noeud courant
        print( indent + str( p ) )
        # et par la suite les enfants, récursivement
        for c in self.children( p ):
            self.preorder_print( c, indent + "    " )

    # imprime le sous-arbre dont la racine est la Position p
    # utilise un parcours postfixé
    def postorder_print( self, p ):
        # on traite les enfants
        for c in self.children( p ):
            self.postorder_print( c )
        # et par la suite le parent
        print( p )

    # imprime le sous-arbre dont la racine est la Position p
    # utilise un parcours en largeur, utilisant une File
    def breadth_first_print(self, p):
        Q = ListQueue()
        # on enqueue la Position p
        Q.enqueue(p)
        # tant qu'il y a des noeuds dans la File
        while not Q.is_empty():
            # prendre le suivant et le traiter
            q = Q.dequeue()
            print(q)
            # enqueuer les enfants du noeud traité
            for c in self.children( q ):
                Q.enqueue(c)