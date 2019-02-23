from node import Node
from list import List

class SinglyLinkedList(List):

    def __init__( self ):
        self._head = None
        self._last = None
        self._size = 0

    def __len__(self):
        # return the lenght of the list
        pass

    def __str__(self):
        # return a string representation of the list
        pass 

    def is_empty(self):
        # return True if the list is empty else False
        pass

    def append(self, element):
        # add an element at the end of the list in O(1)
        pass

    def insert(self, element):
        # add an element at the beginning of the list in O(1)
        pass

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