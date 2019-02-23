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
# utilise DoublyLinkedNode (DoublyLinkedNode.py)

from DoublyLinkedNode import DoublyLinkedNode
from List import List

class DoublyLinkedList(List):

    def __init__( self ):
        self._head = DoublyLinkedNode( None, None, None )
        self._tail = DoublyLinkedNode( None, None, None )
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__( self ):
        return self._size

    def __str__( self ):
        if self.is_empty():
            return "[](size = 0)"
        else:
            pp = "["
            curr = self._head.next
            while curr.next != self._tail:
                pp += str( curr.element ) + ", "
                curr = curr.next
            pp += str( curr.element ) + "]"
            pp += "(size = " + str( self._size ) + ")"
        return pp

    def is_empty( self ):
        return self._size == 0

    # ajoute un élément à la fin de la liste en O(1)
    def append( self, element ):
        # on crée un nouveau noeud pour l'élément à ajouter
        newNode = DoublyLinkedNode( element, self._tail.prev, self._tail )
        # le nouveau noeud sera le dernier
        # on met le suivant de l'ancien dernier sur le nouveau
        #   il se trouve avec le précédent de tail
        # on met le précédent de tail sur le nouveau noeud
        self._tail.prev.next = newNode
        self._tail.prev = newNode
        # on incrémente la taille
        self._size += 1

    # insère un nouvel élément au début de la liste en O(1)
    def insert( self, element ):
        # on crée le nouveau noeud pour l'élément à ajouter
        newNode = DoublyLinkedNode( element, self._head, self._head.next )
        # le nouveau noeud devient le premier
        # on met le précédent de l'ancien premier sur le nouveau
        # on met le suivant de head sur le nouveau
        self._head.next.prev = newNode
        self._head.next = newNode
        # on incrémente la taille
        self._size += 1

    # retire l'élément à l'index k en O(n)
    def remove( self, k ):
        # index de liste commence à 0
        # on valide k
        if not 0 <= k < self._size:
            raise IndexError( 'DoublyLinkedList: index out of bounds' )
        else:
            # on se positionne sur le premier élément
            curr = self._head.next
            # on avance de k-1 noeuds
            for i in range( k ):
                curr = curr.next
            # curr pointe le noeud à retirer
            # on fait sauter les pointeurs :
            #   le suivant du précédent sur le suivant de curr
            #   le précédent du suivant de curr sur son précédent
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            # on libère l'espace occupé par l'élément
            curr.next = None #convention pour un noeud désassigné
            # on décrémente la taille
            self._size -= 1
            # on retourne l'élément
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
            curr = self._head.next
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
            return self._tail.prev.element

    # retourne le premier élément si la liste n'est pas vide
    def first( self ):
        if self.is_empty():
            return None
        else:
            return self._head.next.element

# unit testing
if __name__ == '__main__':

    data = DoublyLinkedList()
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
#    print( "remove 1 = ", data.remove( 1 ) )
#    print( data )

    data.append( 'titi' )
    data.append( 'toto' )
    data.append( 'tata' )
    data.append( 'hala' )
    data.append( 'asma' )
    print( data )

    idx = data.find( 'titi' )
    if idx:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove 2 =", data.remove( 2 ) )
    print( "new size = ", str( len( data ) ) )
    print( data )
    

                
        
