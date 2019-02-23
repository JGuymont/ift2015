#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Files avec priorités/Tas

# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# utilise la classe de base PriorityQueue
from PriorityQueue import PriorityQueue

# ADT HeapPriorityQueue
class HeapPriorityQueue( PriorityQueue ):

    # implémentation avec un tas implanté avec une list Python
    # construction avec possiblement une séquence de tuples (k,v)
    def __init__( self, contents = () ):
        self._Q = [self._Item( k, v ) for k,v in contents]
        if len( self._Q ) > 1:
            self._heapify()

    # taille avec len
    def __len__( self ):
        return len( self._Q )

    # accès direct à un élément
    def __getitem__( self, i ):
        return self._Q[i]

    # vide si len == 0
    def is_empty( self ):
        return len( self ) == 0

    # parent du noeud d'index j
    def _parent(self, j):
        return (j-1) // 2

    # enfant de gauche du noeud d'index j
    def _left(self, j):
        return 2*j + 1

    # enfant de droite du noeud d'index j
    def _right(self, j):
        return 2*j + 2

    # noeud d'index j possède un enfant gauche si l'index de cet enfant
    # est à l'intérieur du tas
    def _has_left( self, j ):
        return self._left( j ) < len(self)

    # noeud d'index j possède un enfant droit si l'index de cet enfant
    # est à l'intérieur du tas
    def _has_right(self, j):
        return self._right(j) < len(self)

    # retourne l'élément de plus grande priorité
    # stocké à la racine du tas
    def min(self):
        if self.is_empty():
            return None
        return self._Q[0]

    # échange les contenus des noeuds i et j
    def _swap( self, i, j ):
        tmp = self._Q[i]
        self._Q[i] = self._Q[j]
        self._Q[j] = tmp

    # version récursive de swim
    def _recswim( self, j ):
        # on prend l'index du parent
        parent = self._parent( j )
        # si parent dans le tas (j n'est pas l'index de la racine)
        # si la clé au noeud d'index j est plus prioritaire
        # alors on échange les contenus de l'enfant avec son parent
        # et on appelle récursivement sur le parent
        # récursivité de queue, donc version itérative triviale
        if j > 0 and self._Q[j] < self._Q[parent]:
            self._swap( j, parent )
            self._swim( parent )

    # swim itératif
    def _swim( self, j ):
        # tantque j n'est pas la racine ou
        # qu'un parent est moins prioritaire
        while j > 0:
            # on accède à l'index du parent
            parent = self._parent( j )
            # on échange enfant et parent si nécessaire
            if self._Q[j] < self._Q[parent]:
                self._swap( j, parent )
                # on continue avec le parent
                j = parent
            # sinon, on met j à 0 pour sortir du while
            else:
                j = 0

    # ajoute et retourne l'élément x de clé k, O(log n)
    def add( self, k, x ):
        item = self._Item( k, x )
        # on ajoute à la fin de la liste
        self._Q.append( item )
        # on fait nager le nouvel élément, O(log n)
        self._swim(len(self)-1)
        # retourne le nouvel élément
        return item

    # version récursive de sink
    def _sink( self, j ):
        # on prend les indices des enfants gauche et droit
        # pour déterminer le plus petit des 2
        if self._has_left( j ):
            left = self._left( j )
            small_child = left
            if self._has_right( j ):
                right = self._right( j )
                if self._Q[right] < self._Q[left]:
                    small_child = right
            # si le plus petit des enfants est plus prioritaire
            # on échange et on appelle récursivement sur l'enfant
            if self._Q[small_child] < self._Q[j]:
                self._swap( j, small_child )
                self._sink( small_child )

    # suppression de l'élément de plus grande priorité, O(log n)
    def remove_min( self ):
        if self.is_empty():
            return None
        # il se trouve à la racine
        the_min = self._Q[0]

        # on déplace le dernier élément du tas à la racine
        self._Q[0] = self._Q[len(self)-1]
        # on détruit le dernier élément
        del self._Q[len(self)-1]

        # si c'était le seul élément, on le retourne et c'est fini
        if self.is_empty():
            return the_min

        # sinon, on coule la nouvelle racine, O(log n)
        self._sink( 0 )

        # retourne le min
        return the_min

    # construit un heap en O(n)
    def _heapify( self ):
        # on débute au parent de la dernière feuille
        # le dernier noeud est nécessairement la dernière feuille !
        start = self._parent( len( self ) - 1 )

        # on coule du parent de la dernière feuille jusqu'à la racine
        for j in range( start, -1, -1 ):
            self._sink( j )

            
# unit testing
if __name__ == '__main__':

    print( "ArrayHeapPriorityQueue unit testing..." )

    testQ = HeapPriorityQueue()
    testQ.add(5, 'A')
    testQ.add(9, 'C')
    testQ.add( 3, 'B' )
    testQ.add( 7, 'D' )
    testQ.add( 1, 'E' )
    print( testQ )
    exit()
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.add( 2, 'AA' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    print( testQ.remove_min() )

    print( "empty? ", testQ.is_empty() )

    #test de heapify

    testQ = HeapPriorityQueue( [(5,'A'), (9, 'C'), (3, 'B'), (7, 'D')] )
    
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.add( 2, 'AA' )
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    testQ.remove_min()
    testQ.remove_min()
    print( testQ )
    print( "min = ", testQ.min() )
    print( "len = ", len( testQ ) )
    print( "empty?", testQ.is_empty() )

    print( testQ.remove_min() )

    print( "empty? ", testQ.is_empty() )

    print( "End of testing." )
