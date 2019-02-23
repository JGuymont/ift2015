#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "11 avril 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.3 Arbres binaires de recherche
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

import random
import time
from TreeMap import TreeMap

#classe SplayTreeMap
class SplayTreeMap( TreeMap ):

    #opération splay d'un noeud p
    def _splay( self, p ):
        #on splay jusqu'à ce que p soit la racine
        while p != self.root():
            #identification du cas
            parent = self.parent( p )
            grand = self.parent( parent )
            #pas de grand-parent => zig
            if grand is None:
                #cas zig, rotation simple autour de p
                self._rotate( p )
            #enfant, parent et grand-parent alignés
            elif ( parent == self.left( grand ) ) == ( p == self.left( parent ) ):
                #cas zig-zig, rotation du parent suivie d'une rotation de p
                self._rotate( parent )
                self._rotate( p )
            else:
                #cas zig-zag, double rotation de p
                self._rotate( p )
                self._rotate( p )

    #rebalancement après insertion
    def _rebalance_insert( self, p ):
        self._splay( p )

    #rebalancement après suppression
    def _rebalance_delete( self, p ):
        if p is not None:
            self._splay( p )

    #rebalancement après accession
    def _rebalance_access( self, p ):
        self._splay( p )

    #print the subtree rooted by position p
    #using a preorder traversal
    def preorder_print( self, p, indent = "" ):
        print( indent + str( p ) )
        for c in self.children( p ):
            self.preorder_print( c, indent + "    " )

#unit testing
if __name__ == '__main__':

    print( "SplayTreeMap unit testing..." )

    M = SplayTreeMap( )
#     for x in [8,16,4,2,1,64,0,32]:
#         M[x] = x
#         M.preorder_print( M.root() )

    nb = 1000000
    random.seed( 131341 )

    #Insertion
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        M[key] = key
    apres = time.time()
    print( "Insertion of", nb, "keys in ", apres-avant, "seconds." )

    #Access
    random.seed( 131341 )
    avant = time.time()
    for i in range( nb ):
        key = random.randint( 0, nb )
        x = M[key]
    apres = time.time()
    print( "Access of", nb, "keys in ", apres-avant, "seconds." )

    #Delete
    avant = time.time()
    nbdel = 0
    for i in range( nb ):
        key = random.randint( 0, nb )
        try:
            del M[key]
        except:
            pass
    apres = time.time()
    print( "Delete ", nb, "keys in ", apres-avant, "seconds." )

#     M = SplayTreeMap( )
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

#     M = SplayTreeMap()
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

