#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#

import sys
import random
from SkipListNode import SkipListNode
from Coin import Coin

_FACE      = True
_TAILS     = False
_MAX       = sys.maxsize
_MIN       = -sys.maxsize - 1

#ADT SkipList
class SkipList():

    def __init__( self, _MIN_VALUE = _MIN, _MAX_VALUE = _MAX ):
        #valeurs pour les sentinelles, -infini à +infini
        self._MIN_VALUE = _MIN_VALUE
        self._MAX_VALUE = _MAX_VALUE
        #une instance de Coin pour les tours de hauteurs variables
        self._coin = Coin()
        #hauteur de départ
        self._height = 1
        #taille initiale de 0
        self._size = 0
        #les 4 sentinelles et leurs interrelations
        #lr = low-right; ll = low-left; ul = upper-left; ur = upper-right
        sentinel_lr = SkipListNode( self._MAX_VALUE )
        sentinel_ll = SkipListNode( self._MIN_VALUE, None, sentinel_lr, None, None )
        sentinel_lr._prev = sentinel_ll
        sentinel_ul = SkipListNode( self._MIN_VALUE, None, None, sentinel_ll, None )
        sentinel_ur = SkipListNode( self._MAX_VALUE, sentinel_ul, None, sentinel_lr, None )
        sentinel_ul._next = sentinel_ur
        sentinel_ll._abov = sentinel_ul
        sentinel_lr._abov = sentinel_ur
        #par convention, le début de la skiplist est la sentinelle _ul
        self._start = sentinel_ul

    #taille de la skiplist
    def __len__( self ):
        return self._size

    # prettyprint
    def __str__( self ):
        #on prend le début de la skiplist
        current = self._start
        pp = "SkipList of height " + str( self._height ) + ":\n"
        #pour chaque niveau
        for level in range( self._height, -1, -1 ):
            p = current
            pp += "level " + str( level ) + " ["
            #le premier élément du niveau est le suivant de la sentinelle
            p = p._next
            while not( p is None ):
                if( not p._next is None ):
                    pp +=  str( p._elem )
                    if( not p._next._next is None ):
                        pp += ","
                p = p._next
            #on descend par la sentinelle
            current = current._belo
            pp += "]\n"
        return pp

    #iterateur : parcours les éléments du niveau 0
    def __iter__( self ):
        #on prend le niveau du début de la skiplist (plus haut)
        level = self._start
        #on descend jusqu'au niveau 0 par les sentinelles
        while not( level._belo is None ):
            level = level._belo
        #on parcourt les éléments du niveau 0,
        #le premier étant le suivant de la sentinelle
        current = level._next
        while not( current._next is None ):
                yield current._elem
                current = current._next

    #retourne l'élément le plus petit de la skiplist
    def Min( self ):
        #si la skiplist est vide, il n'existe pas
        if self._size == 0:
            return None
        #on prend le début de la skiplist
        tower = self._start
        #on descend jusqu'au niveau 0 par les sentinelles
        while not( tower._belo is None ):
            tower = tower._belo
        #l'élément le plus petit est le suivant de la sentinelle
        return tower._next._elem

    #retourne l'élément le plus grand de la skiplist
    def Max( self ):
        #si la skiplist est vide, il n'existe pas
        if self._size == 0:
            return None
        #on prend la sentinelle à droite du début de la skiplist
        tower = self._start._next
        #on descend jusqu'au niveau 0 par les sentinelles de droite
        while not( tower._belo is None ):
            tower = tower._belo
        #l'élément le plus grand est le précédent de la sentinelle
        return tower._prev._elem

    #recherche et retourne un élément, ou son précédent s'il n'existe pas
    def SkipSearch( self, element ):
        #on prend le début de la skiplist
        p = self._start
        #tant que sur un niveau supérieur à 0
        while not( p._belo is None ):
            #on descend de niveau
            p = p._belo
            #tant que l'élément suivant est < que l'élément recherché
            while element >= p._next._elem:
                #on prend l'élément suivant
                p = p._next
        #s'arrête et retourne l'élément recherché ou son précédent
        return p

    #augmente la hauteur de la skiplist
    def increaseHeight( self ):
        #on retient les anciennes sentinelles du plus haut niveau
        old_sentinel_l = self._start
        old_sentinel_r = self._start._next
        #on crée deux nouvelles sentinelles pour la nouveau niveau
        new_sentinel_l = SkipListNode( self._MIN_VALUE, None, None, old_sentinel_l, None )
        new_sentinel_r = SkipListNode( self._MAX_VALUE, new_sentinel_l, None, old_sentinel_r, None )
        new_sentinel_l._next = new_sentinel_r
        #on relie les pointeurs du dessus des vielles sentinelles aux nouvelles
        old_sentinel_l._abov = new_sentinel_l
        old_sentinel_r._abov = new_sentinel_r
        #on augmente la variable qui indique la hauteur de la skiplist
        self._height += 1
        #on ajuste le début de la skiplist
        self._start = new_sentinel_l

    #insère un noeud après le noeud p et au-dessus du noeud q
    def insertAfterAbove( self, p, q, element ):
        #p est pour le précédent
        #q est pour celui au-dessous
        #arguments de SkipListNode : element, prev, next, belo, abov
        #abov toujours None car on insère toujours au niveau le plus haut
        #le nouveau noeud a p comme précédent, p._next comme suivant,
        #     q au-dessous et rien au-dessus
        newnode = SkipListNode( element, p, p._next, q, None )
        #on relie le précédent de l'ancien suivant, next._prev, au nouveau noeud
        p._next._prev = newnode
        #on relie le suivant du précédent, p._next, au nouveau noeud
        p._next = newnode
        #s'il y a un noeud en-dessous, q n'est pas à None, on le relie au nouveau noeud
        #which is abov it
        if not( q is None ):
            q._abov = newnode
        #on retourne le nouveau noeud
        return newnode

    #insertion d'un nouvel élément
    #retourne le noeud du plus haut niveau du nouvel élément s'il n'existait pas
    #sinon, le noeud du niveau 0 de celui qui existait
    def SkipInsert( self, element ):
        #on commence par le chercher
        p = self.SkipSearch( element )
        #on sauve le résultat de la recherche
        q = p
        #si l'élément existait
        if p._elem == element:
            #on doit modifier sa valeur à chaque niveau
            #imaginez des éléments du type ( clé, valeur )
            #on doit ajuster la valeur de tous les éléments de sa tour
            while( not p is None ):
                p._elem = element
                p = p._abov
            #dans ce cas, on a terminé, on retourne
            return q

        #comme l'élément n'existe pas, p pointe sur le noeud précédent
        #nous sommes au niveau 0, donc belo est None
        q = self.insertAfterAbove( p, None, element )

        #on a inséré un noeud au niveau 0 pour le nouvel élément
        #on doit maintenant monter sa tour en fonction de pile ou face
        i = 0
        coin_flip = self._coin.flip()
        while coin_flip == _FACE:
            i += 1 #i indique le niveau courant d'insertion
            #si on a atteint le niveau du haut
            #on doit ajouter un nouveau niveau, on appelle increaseHeight()
            if i >= self._height:
                self.increaseHeight()
            #on doit ajouter un noeud sur le niveau au-dessus
            #on cherche un noeud dans les précédents, débutant à p, qui permet de monter de niveau
            while p._abov is None:
                #on va voir le précédent
                p = p._prev
            #p pointe vers un noeud qui en possède un au-dessus, on le suit pour monter
            p = p._abov
            #q pointe vers le noeud inséré précédemment,
            #il correspond au noeud en dessous du noeud à insérer
            q = self.insertAfterAbove( p, q, element )
            #on relance le jeton
            coin_flip = self._coin.flip()

        #ici on a terminé la tour de l'élément à insérer
        #avant de sortir, on incrémente de 1 la taille de la skiplist
        self._size += 1
        #on retourne le dernier noeud inséré, celui du plus haut niveau ajouté
        return q

    #_SkipHeadCut
    def decreaseHeight( self ):
        p = self._start._belo
        while( not p._belo is None and p._next._elem == self._MAX_VALUE ):
            self._start = p
            self._height -= 1
            p = p._belo
        return p

    #supprime et retourne un élément, s'il existe
    #sinon, retourne None
    def SkipRemove( self, element ):
        #on commence par le chercher
        p = self.SkipSearch( element )
        #s'il existe
        if p._elem == element:
            #on retire le noeud de cet élément à chaque niveau
            tower = p
            while not( tower is None ):
                #comme la suppression dans une liste chaînée
                tower._prev._next = tower._next
                tower._next._prev = tower._prev
                #on monte de niveau
                tower = tower._abov
            #on retourne 
            return p
        return None

#unit testing
if __name__ == '__main__':

    print( "SkipList unit testing..." )

    random.seed( 131341 )

    L = SkipList()
#    L.SkipRemove( 100 )
#     L.SkipInsert( 12 )
#     L.SkipInsert( 17 )
#     L.SkipInsert( 20 )
#     L.SkipInsert( 25 )
#     L.SkipInsert( 31 )
#     L.SkipInsert( 38 )
#     L.SkipInsert( 39 )
#     L.SkipInsert( 44 )
#     L.SkipInsert( 50 )
#     L.SkipInsert( 55 )
#     L.SkipInsert( 20 )
#     print( L )
#     L.SkipRemove( 55 )
#     L.SkipRemove( 50 )
#     L.SkipRemove( 12 )
#     L.SkipRemove( 17 )
#     L.SkipRemove( 20 )
#     L.SkipRemove( 25 )
#     L.SkipRemove( 31 )
#     L.SkipRemove( 38 )
#     L.SkipRemove( 39 )
#     L.SkipRemove( 44 )
#     print( L )

    for i in range( 100000 ):
        x = random.randint( 0, 5000 )
        L.SkipInsert( x )
    for i in range(  25000 ):
        x = random.randint( 0, 5000 )
        L.SkipRemove( x )
    print( L )

    for i in range( 10 ):
        x = random.randint( 0, 100 )
        

    for i in range( 10 ):
        x = random.randint( 0, 100 )
        L.SkipInsert( x )
        print( L )
        print( str( L.SkipSearch( x ) ) )    
        
    print( "end unit testing..." )
