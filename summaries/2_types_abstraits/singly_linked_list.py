from node import Node
from list import List

class SinglyLinkedList(List):

    def __init__(self):
        self._head = None
        self._last = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty(): return "[](size = 0)"
        pp = "["
        curr = self._head
        while curr != self._last:
            pp += '{}, '.format(curr.element)
            curr = curr.next
        pp += "{}]".format(curr.element)
        pp += "(size = {})".format(self._size)
        return pp 

    def is_empty(self):
        return self._size

    def append(self, element):
        """add an element at the end of the list in O(1)"""
        new_node = Node(element)
        if self.is_empty:
            self._head = new_node 
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._size += 1

    def insert(self, element):
        """add an element at the beginning of the list in O(1)"""
        new_node = Node(element)
        if self.is_empty:
            self._head = new_node 
            self._last = new_node
        else:
            self._

    def remove( self, k ):
        # remove the element at index k in O(n)
        pass

    def find(self, element):
        # return the index where element is located
        # or None if the element is not in the list
        pass

    def last( self ):
        # return the last element if the list is not empty
        pass

    def first( self ):
        # return the first element if the list is not empty
        pass