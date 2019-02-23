#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "28 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

import random
import time
from LinkedBinaryTree import LinkedBinaryTree
from Map import Map

class TreeMap( LinkedBinaryTree, Map ):

    #on ajoute des méthodes d'accès à une Position
    #pour la clé et la valeur
    class Position( LinkedBinaryTree.Position ):

        def key( self ):
            return self.element()._key
    
        def value( self ):
            return self.element()._value

    #--- méthodes privées ---

    #pour rebalancer après une suppression
    def _rebalance_delete( self, p ):
        pass

    #pour rebalancer après une accession
    def _rebalance_access( self, p ):
        pass

    #pour rebalancer après une insertion
    def _rebalance_insert( self, p ):
        pass

    #recherche à partir d'une position l'élément de clé k
    def _subtree_search( self, p, k ):
        #si la position possède l'élément de clé k
        #on retourne la position correspondante
        if k == p.key():
            return p
        #sinon, si la clé est < à celle de l'élément à positon p
        elif k < p.key():
            #on poursuit la recherche dans le sous-arbre de gauche
            if self.left( p ) is not None:
                return self._subtree_search( self.left( p ), k )
        else:
            #sinon, k est plus grande et on poursuit dans le sous-arbre de droite
            if self.right( p ) is not None:
                return self._subtree_search( self.right( p ), k )
        #on arrive à un sous-arbre de p qui est vide
        #on retourne p, le dernier noeud visité
        #sa clé peut être >, = ou < à k selon le cas
        return p

    #trouve et retourne la position du noeud qui possède
    #l'élément de clé k
    def _find_position( self, k ):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search( self.root(), k )
            self._rebalance_access( p )
            return p

    #accède et retourne la première position (clé la plus petite) du sous-arbre
    #de racine p
    def _subtree_first_position( self, p ):
        walk = p
        #on descend le plus loin possible à gauche
        while self.left( walk ) is not None:
            walk = self.left( walk )
        return walk

    #accède et retourne la dernière position (clé la plus grande) du sous-arbre
    #de racine p
    def _subtree_last_position( self, p ):
        walk = p
        #on descend le plus loin possible à droite
        while self.right( walk ) is not None:
            walk = self.right( walk )
        return walk

    #version racine de première position
    def first( self ):
        return self._subtree_first_position( self.root() ) if len( self ) > 0 else None

    #version racine de dernière position
    def last( self ):
        return self._subtree_last_position( self.root() ) if len( self ) > 0 else None

    #retourne la position juste avant p
    def before( self, p ):
        #on valide p
        self._validate( p )
        #la position précédente est soit la dernière position du sous-arbre gauche
        if self.left( p ):
            return self._subtree_last_position( self.left( p ) )
        #ou le premier ancêtre avec une clé plus petite que p
        #on remonte jusqu'à un virage à gauche
        else:
            walk = p
            above = self.parent( walk )
            while above is not None and walk == self.left( above ):
                walk = above
                above = self.parent( walk )
            return above

    #retourne la position juste après p
    def after( self, p ):
        #on valide p
        self._validate( p )
        #la position après est soit la première position du sous-arbre droit
        if self.right( p ):
            return self._subtree_first_position( self.right( p ) )
        #ou le premier ancêtre avec une clé plus grande que p
        #on remonte jusqu'à un virage à droite
        else:
            walk = p
            above = self.parent( walk )
            while above is not None and walk == self.right( above ):
                walk = above
                above = self.parent( walk )
            return above

    #retourne l'élément avec la clé minimum, soit first
    def find_min( self ):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value() )

    #retourne l'élément avec la clé maximum, soit last
    def find_max( self ):
        if self.is_empty():
            return None
        else:
            p = self.last()
            return (p.key(), p.value() )

    #retourne l'élément avec la clé plus grande ou égale à k
    def find_ge( self, k ):
        if self.is_empty():
            return None
        else:
            #on trouve la position du noeud de clé k
            p = self._find_position( k )
            #si le noeud trouvé possède une clé < k
            #on retourne la suivante qui est > k (car clé k non trouvée)
            #sinon, soit on a trouvé la clé k ou on s'est arrêté
            #sur un noeud dont la clé est > k, donc on la retourne
            if p.key() < k:
                p = self.after( p )
            return (p.key(), p.value()) if p is not None else None

    #retourne l'élément avec la clé plus grande que k
    def find_gt( self, k ):
        if self.is_empty():
            return None
        else:
            #on trouve la position du noeud de clé k
            p = self._find_position( k )
            #si le noeud trouvé possède une clé <= k, on retourne la suivante
            #sinon, on s'est arrêté sur une clé > k, donc on la retourne
            if p.key() <= k:
                p = self.after( p )
            return (p.key(), p.value()) if p is not None else None

    #retourne l'élément avec la clé plus petite ou égale à k
    def find_le( self, k ):
        if self.is_empty():
            return None
        else:
            #on trouve la position du noeud de clé k
            p = self._find_position( k )
            #si le noeud trouvé possède une clé > k
            #on retourne la précédente qui est < k (car clé k non trouvée)
            #sinon, soit on a trouvé la clé k ou on s'est arrêté
            #sur un noeud dont la clé est < k, donc on la retourne
            if p.key() > k:
                p = self.before( p )
            return (p.key(), p.value()) if p is not None else None

    #retourne l'élément avec la clé plus petite que k
    def find_lt( self, k ):
        if self.is_empty():
            return None
        else:
            #on trouve la position du noeud de clé k
            p = self._find_position( k )
            #si le noeud trouvé possède une clé >= k, on retourne la précédente
            #sinon, on s'est arrêté sur une clé < k, donc on la retourne
            if p.key() >= k:
                p = self.before( p )
            return (p.key(), p.value()) if p is not None else None

    #itérateur sur les clés entre [start, stop[
    def find_range( self, start = None, stop = None ):
        if not self.is_empty():
            if start is None:
                #si start est None, on commence avec la plus petite clé
                p = self.first()
                print( "start is None, p = ", p.key() )
            else:
                #sinon, on trouve la position de start
                p = self._find_position( start )
                #si elle n'existe pas et qu'on s'est arrêté sur
                #le noeud de clé < start, on commence à la clé suivante
                if p.key() < start:
                    p = self.after( p )
            #on parcourt les clés à partir de start jusqu'à stop exclusivement
            #ou toutes les clés après start si stop est None
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after( p )

    def __str__( self ):
        pp = "["
        for (k,v) in self.items():
            pp += "(" + str( k ) + "," + str( v ) + ")"
        pp += "]"
        return pp

    def __iter__( self ):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after( p )

    #accession à la position avec clé k
    def __getitem__( self, k ):
        #si arbre vide, on lance un exception
        if self.is_empty():
            raise KeyError
        else:
            #sinon, on cherche la position de clé k
            p = self._subtree_search( self.root(), k )
            #on rebalance post-accession
            self._rebalance_access( p )
            #si la clé k est absente, on lance une exception
            if k != p.key():
                raise KeyError
            #sinon, on retourne la valeur de la position de clé k
            return p.value()

    #assignation ou insertion de l'élément (k, v)
    def __setitem__( self, k, v ):
        #si l'arbre est vide, on crée la racine
        if self.is_empty():
            leaf = self._add_root( self._Item( k, v ) ) #de LinkedBinaryTree
        else:
            #sinon, on cherche si la position de clé k existe
            p = self._subtree_search( self.root(), k )
            #si elle existe
            if p.key() == k:
                #on change sa valeur
                p.element()._value = v
                #on rebalance post-accession
                self._rebalance_access( p )
                #on sort
                return
            else:
                #sinon, on crée le nouvel item et la nouvelle position
                item = self._Item( k, v )
                #à droite si la clé k est > que la clé de la position feuille
                if p.key() < k:
                    leaf = self._add_right( p, item ) #de LinkedBinaryTree
                else:
                    #sinon, à gauche
                    leaf = self._add_left( p, item ) #de LinkedBinaryTree
        #on rebalance post-insertion
        self._rebalance_insert( leaf )

    #suppression du noeud à positon p
    def delete( self, p ):
        #on valide p
        self._validate( p )
        #si p possède des sous-arbres gauche et droit
        #on substitut son élément par celui de la clé suivante
        #et on supprime le noeud qui la contient (le substitut)
        #sinon, on le supprime avec delete de LinkedBinaryTree.py
        if self.left( p ) and self.right( p ):
            #on trouve la clé de remplacement
            #par convention la première clé du sous-arbre droit
            replacement = self._subtree_first_position( self.right( p ) )
            #on modifie l'élément à position p par celui du substitut
            #replace est dans LinkedBinaryTree.py
            self._replace( p, replacement.element() )
            #le noeud à supprimer est le substitut
            p = replacement
        #on note le parent du noeud à supprimer
        parent = self.parent( p )
        #on supprime le noeud à position p
        self._delete( p )
        #on rebalance autour du parent
        self._rebalance_delete( parent )

    #suppression d'une clé dans la Map
    def __delitem__( self, k ):
        #si la Map n'est pas vide
        if not self.is_empty():
            #on cherche la position du noeud de clé k
            p = self._subtree_search( self.root(), k )
            #si trouvé, on la supprime
            if k == p.key():
                self.delete( p )
                return
            #sinon, la clé n'existe pas et on
            #rebalance autour du dernier noeud accédé
            self._rebalance_access( p )
        #si la clé n'est pas trouvée ou la Map est vide,
        #on lance une exception
        raise KeyError( "Key Error: ", k )

    #liaison d'un parent et son enfant (qui peut être None)
    def _relink( self, parent, child, make_left_child ):
        #à gauche
        if make_left_child:
            parent._left = child
        #ou à droite (selon make_left_child)
        else:
            parent._right = child
        #on relie l'enfant au (nouveau) parent
        if child is not None:
            child._parent = parent

    #rotation autour de p
    def _rotate( self, p ):
        #x est le noeud p
        x = p._node
        #y est son parent
        y = x._parent
        #z est son grand-parent
        z = y._parent
        #si z est None, on a 2 noeuds, pas de grand-parent
        if z is None: #x remplacera y à la racine
            self._root = x
            x._parent = None
        else:
            #x est adopté par son grand-père
            self._relink( z, x, y == z._left )
        #rotation de x et y et transfert du sous-arbre du milieu
        if x == y._left:
            self._relink( y, x._right, True )
            self._relink( x, y, False )
        else:
            self._relink( y, x._left, False )
            self._relink( x, y, True )

    #restructuration pour le noeud x
    def _restructure( self, x ):
        #y est le parent de x
        y = self.parent( x )
        #z est le grand-parent de x
        z = self.parent( y )
        #on identifie le cas
        #pour les cas de rotation simple (pas de zig zag)
        #si x est enfant droit de y et y enfant droit de z, ou
        #si x est enfant gauche de y et y enfant gauche de z
        if( x == self.right( y ) ) == (y == self.right( z ) ):
            #rotation simple autour de y
            self._rotate( y )
            return y
        #sinon, on est dans un cas de rotation double (zig zag)
        else:
            #on applique 2 fois la rotation sur x
            self._rotate( x )
            #après la 1ère rotation, on est dans un des 2 premiers cas
            self._rotate( x )
            return x

#unit testing
if __name__ == '__main__':

    print( "TreeMap unit testing..." )

    M = TreeMap()
    M[6] = 'six'
    M[3] = 'three'
    M[1] = 'one'
    M[4] = 'four'
    M[9] = 'nine'
    M[8] = 'eight'

    print( M )

    print( M.find_lt( 5 ) )
    print( M.find_le( 5 ) )
    for k, v in M.find_range( ):
        print( k, v )

    

#    for _ in M.find_range( 1, 9 ):
#        print( _ )
#
#    for _ in M.find_range( 4, None ):
#        print( _ )
#
#    for _ in M.find_range( 0, 10 ):
#        print( _ )
#
#    for _ in M.find_range( None, 5 ):
#        print( _ )
#        
#    for _ in M.find_range( None, None ):
#        print( _ )


#     M = TreeMap( )
#     nb = 500000
#     random.seed( 131341 )
#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M[key] = key
#     apres = time.time()
#     print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

#     avant = time.time()
#     for i in range( nb ):
#         key = random.randint( 0, nb )
#         M.get( key )
#     apres = time.time()
#     print( "Access to", nb, "keys in ", apres-avant, "seconds." )

#     M = TreeMap( )
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

#    M = TreeMap()
#    nb = 100000
#    random.seed( 131341 )
#    avant = time.time()
#    for i in range( nb ):
#        key = random.randint( 0, nb )
#        M[key] = key
#    apres = time.time()
#    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )
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
