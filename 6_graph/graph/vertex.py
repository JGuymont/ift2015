#!/usr/bin/python3
"""
Lightweight vertex structure for a graph. This class 
will be inhetited by the class Graph.
"""

class Vertex:
    
    def __init__(self, x):
        self._element = x

    def __str__(self):
        return str(self.element())

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))
