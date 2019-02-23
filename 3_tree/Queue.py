"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""

#ADT Queue "interface"
class Queue:

    def __init__( self ):
        pass

    #return the number of elements in Queue
    def __len__( self ):
        pass

    #convert a Queue into a string:
    # elements listed between brackets
    # separated by commas
    # element front and rear highlighted
    # size and capacity of the data structure
    # indicated
    def __str__( self ):
        pass

    #indicate whether no element are
    #stored in the Queue
    def is_empty( self ):
        pass

    #add element on the Queue
    def enqueue( self, element ):
        pass

    #remove an element from the Queue
    def dequeue( self ):
        pass

    #return the first element
    #without removing it
    def first( self ):
        pass
