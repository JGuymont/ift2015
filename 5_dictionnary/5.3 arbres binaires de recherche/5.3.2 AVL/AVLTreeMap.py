#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "30 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.3 Arbres binaires de recherche
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

import random
import time
from TreeMap import TreeMap

#classe AVLTreeMap
class AVLTreeMap( TreeMap ):

    #ajout de la hauteur d'un noeud
    class _Node( TreeMap._Node ):
        __slots__ = '_height' #membre additionel

        #constructeur : on appelle celui de TreeMap et on met la hauteur par défaut à 0
        def __init__( self, element, parent = None, left = None, right = None ):
            super().__init__( element, parent, left, right )
            self._height = 0

        #accès à la hauteur du sous-arbre gauche
        def left_height( self ):
            return self._left._height if self._left is not None else 0

        #accès à la hauteur du sous-arbre droit
        def right_height( self ):
            return self._right._height if self._right is not None else 0

    def __str__( self ):
        pp = super().__str__()
        pp += "(h = " + str( self.root()._node._height ) + ")"
        return pp

    #recalcul de la hauteur d'un noeud
    def _recompute_height( self, p ):
        p._node._height = 1 + max( p._node.left_height(), p._node.right_height() )

    #noeud balancé si différence des hauteurs de ses enfants est au plus 1
    def _isbalanced( self, p ):
        return abs( p._node.left_height() - p._node.right_height() ) <= 1

    #retourne le plus grand (haut) des enfants de p
    #si favorleft, on lui ajoute 1 pour le choisir en cas d'égalité
    def _tall_child( self, p, favorleft = False ):
        if p._node.left_height() + ( 1 if favorleft else 0 ) > p._node.right_height():
            return self.left( p )
        else:
            return self.right( p )

    #retourne le plus grand (haut) des petits enfants de p
    def _tall_grandchild( self, p ):
        child = self._tall_child( p )
        #si enfant gauche, on favorise le petit enfant gauche
        #si enfant droit, on favorise le petit enfant droit
        #pour choisir une rotation simple plutôt que (zig-zag) double
        alignment = ( child == self.left( p ) )
        return self._tall_child( child, alignment )

    #rebalancement autour de p, propagé vers le haut
    def _rebalance( self, p ):
        while p is not None:
            #on note l'ancienne hauteur
            old_height = p._node._height
            #si on note un débalancement autour de p
            if not self._isbalanced( p ):
                #on restructure autour du plus grand petit enfant
                #on met p sur la racine du résultat
                #on recalcule les hauteurs à gauche et à droite de p
                p = self._restructure( self._tall_grandchild( p ) )
                self._recompute_height( self.left( p ) )
                self._recompute_height( self.right( p ) )
            #on recalcule la hauteur de p
            self._recompute_height( p )
            #si la hauteur est inchangée, on sort
            if p._node._height == old_height:
                p = None
            else:
                #sinon, on propage au parent
                p = self.parent( p )

    #on rebalance après un insertion
    def _rebalance_insert( self, p ):
        self._rebalance( p )

    #on rebalance après une suppression
    def _rebalance_delete( self, p ):
        self._rebalance( p )

#unit testing
if __name__ == '__main__':

    print( "AVLTreeMap unit testing..." )

#     M = AVLTreeMap( )
#     for x in [0,1,2]:
#         M[x] = x
#     print( M )

    M = AVLTreeMap( )
    nb = 1000000
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    print( M.height( M.root() ) )

    #Access
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         try:
#             M[key]
#         except KeyError:
#             pass
#     apres = time.time()
#     print( "Access of", nb, "keys in ", apres-avant, "seconds." )

#     #Delete
#     avant = time.time()
#     nbdel = 0
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         try:
#             del M[key]
#         except KeyError:
#             pass
#     apres = time.time()
#     print( "Delete ", nb, "keys in ", apres-avant, "seconds." )

#     M = AVLTreeMap( )
#     print( len( M ) ) #0
#     M['K'] = 2
#     print( M )
#     print( len( M ) )
#     M['B'] = 4
#     print( M )
#     print( len( M ) )
#     M['U'] = 2
#     print( M )
#     print( len( M ) )
#     M['V'] = 8
#     print( M )
#     print( len( M ) )

#     M['K'] = 9
#     print( M )
#     print( len( M ) )
#     print( M['B'] )
#     print( M['X'] )
#     print( M.get( 'F' ) )
#     print( M.get( 'F', 5 ) )
#     print( M.get( 'K', 5 ) )
#     print( M )
#     print( len( M ) )
#     del M['V']
#     print( "pop(K) = ", M.pop( 'K' ) )
#     print( M )
#     for key in M.keys():
#         print( str( key ) )
#     for value in M.values():
#         print( str( value ) )
#     for item in M.items():
#         print( str( item ) )
#     print( M.setdefault( 'B', 1 ) )
#     print( M.setdefault( 'AA', 1 ) )
#     print( M )
#     print( M.popitem() )
#     print( M )
#     print( M.find_min() )
#     print( M.find_max() )

#     M = AVLTreeMap()
#     nb = 50
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()
#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
#     print( M )

#     print( M.find_min() )
#     print( M.find_max() )

#     print( M.find_ge( 25 ) )
#     print( M.find_gt( 25 ) )
#     print( M.find_le( 25 ) )
#     print( M.find_lt( 25 ) )
#     print( M.find_lt( 0 ) )

#     for (x,y) in M.find_range( 12, 100 ):
#         print( "x =", x, ", y =", y )
    
    print( "End of testing." )

