#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/Types abstraits/Liste chaînées
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# implémente l'ADT List (List.py)
# utilise SinglyLinkedNode (SinglyLinkedNode.py)

from SinglyLinkedNode import SinglyLinkedNode
from List import List

class SinglyLinkedList( List ):

    def __init__( self ):
        self._head = None
        self._last = None
        self._size = 0

    def __len__( self ):
        return self._size

    def __str__( self ):
        if self.is_empty():
            return "[](size = 0)"
        else:
            pp = "["
            curr = self._head
            while curr != self._last:
                pp += str( curr.element ) + ", "
                curr = curr.next
            pp += str( curr.element ) + "]"
            pp += "(size = " + str( self._size ) + ")"
        return pp

    def is_empty( self ):
        return self._size == 0

    # ajoute un élément à la fin de la liste en O(1)
    def append( self, element ):
        # on crée un nouveau noeud pour l'élément
        newNode = SinglyLinkedNode( element, None )
        # si la liste est vide
        # noeud unique, donc premier et dernier
        if self.is_empty():
            self._head = self._last = newNode
        # sinon le noeud devient le suivant du last 
        # et le last de la liste
        else:
            self._last.next = newNode
            self._last = newNode
        # on incrémente la taille
        self._size += 1

    # ajoute un élément au début de la liste en O(1)
    def insert( self, element ):
        # on crée un nouveau noeud pour l'élément
        newNode = SinglyLinkedNode( element, self._head )
        # si la liste est vide
        # noeud unique, donc dernier
        if self.is_empty():
            self._last = newNode
        # noeud devient le premier de la liste
        self._head = newNode
        # on incrémente la taille
        self._size += 1

    # retire l'élément à l'index k en O(n)
    def remove( self, k ):
        # les indices de listes commencent à 0
        # on vérifie si le kème élément existe
        if not 0 <= k < self._size:
            raise IndexError( 'SinglyLinkedList: index out of bounds' )
        else:
            # on avance un pointeur, curr, vers le kème noeud
            # on commence au premier noeud
            # on garde le noeud précédent, prev,
            # qui sera utile pour compléter l'opération
            curr = self._head
            prev = None
            # on prend le noeud suivant k-1 fois
            # et fait suivre curr
            for i in range( k ):
                prev = curr
                curr = curr.next
            # si prev est None c'est qu'on est sur le 1er élément
            if prev == None:
                # on retire le premier élément
                # simplement en mettant head sur son suivant
                self._head = curr.next
            # sinon on ajuste le suivant du noeud précédent
            # sur le suivant du noeud courant
            else:
                prev.next = curr.next
            # on décrémente la taille
            self._size -= 1
            # si on a vidé la liste
            # last devient None
            if self._size == 0:
                self._last = None
            # si on a retiré le dernier élément
            # mais que la liste n'est pas vide
            # on met last sur le noeud prev
            if curr.next == None:
                self._last = prev
            # on retourne l'élément retiré
            return curr.element

    # retourne l'index d'un élément en O(n)
    # ou None s'il n'est pas trouvé
    def find( self, element ):
        # si la liste est vide l'élément n'y est pas.
        if self.is_empty():
            return None
        # sinon, on commence par la tête de liste
        # et on parcourt les éléments un à un
        # en utilisant les références au noeuds suivants
        else:
            curr = self._head
            for i in range( self._size ):
                if curr.element == element:
                    return i
                else:
                    curr = curr.next
        # si aucun index n'a été retourné
        # c'est que l'élément n'a pas été trouvé
        return None

    # retourne le dernier élément si la liste n'est pas vide
    def last( self ):
        if self.is_empty():
            return None
        else:
            return self._last.element

    # retourne le premier élément si la liste n'est pas vide
    def first( self ):
        if self.is_empty():
            return None
        else:
            return self._head.element

#unit testing
if __name__ == '__main__':

    data = SinglyLinkedList()
    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    print( data )

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
#    print( "remove 0 = ", data.remove( 0 ) )
#    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    data.append( 'holo' )
    data.append( 'asma' )
    print( data )

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

    print( "remove 2 =", data.remove( 2 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )
    
    data2 = SinglyLinkedList()
    data2.append( 'titi' )
    data2.append( 'toto' )
    data2.append( 'tata' )
    print( data )

                
        
