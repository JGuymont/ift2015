from ListQueue import ListQueue

#ADT Tree (Classe de base)    
class Tree:

    #inner class Position
    class Position:

        def element( self ):
            pass

        def __eq__( self, other ):
            pass

        def __ne__( self, other):
            return not( self == other )

    # retourne la racine
    def root( self ):
        pass

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

    # retourne le parent d'une Position
    def parent( self, p ):
        pass

    # retourne le nombre d'enfants d'une Position
    def num_children( self, p ):
        pass

    # retourne les enfants d'une Position
    def children( self, p ):
        pass

    # retourne le nombre de noeuds
    def __len__( self ):
        pass

    # demande si une Position est la racine
    def is_root( self, p ):
        return self.root() == p

    # demande si une Position est une feuille
    def is_leaf( self, p ):
        return self.num_children( p ) == 0

    # demande si un arbre est vide
    def is_empty( self ):
        return len( self ) == 0

    # retourne la profondeur d'une Position
    def depth( self, p ):
        # retourne le nombre d'ancêtres d'une Position
        if self.is_root( p ):
            return 0
        else:
            return 1 + self.depth(self.parent())

    # retourne la hauteur d'une Position avec depth (non efficace)
    def height1( self, p ):
        # retourne la profondeur maximum des feuilles sous une Position
        # positions n'est pas implanté et se fait en O(n)
        return max( self.depth( p ) for p in self.positions() if self.is_leaf( p ))

    # retourne la hauteur d'une Position en descendant l'arbre (efficace)
    def height( self, p ):
        # retourne la hauteur d'un sous-arbre à une Position
        if self.is_leaf( p ):
            return 0
        else:
            return 1 + max( self.height( c ) for c in self.children( p ) )

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
    def breadth_first_print( self, p ):
        Q = ListQueue()
        # on enqueue la Position p
        Q.enqueue( p )
        # tant qu'il y a des noeuds dans la File
        while not Q.is_empty():
            # prendre le suivant et le traiter
            q = Q.dequeue()
            print( q )
            # enqueuer les enfants du noeud traité
            for c in self.children( q ):
                Q.enqueue( c )
