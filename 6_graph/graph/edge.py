#!/usr/bin/python3
"""
Lightweight edge structure for a graph.
"""

class Edge:

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x
    
    def __str__(self):
        return str(self.element())

    def endpoint(self):
        return (self._origin, self._destination)
    
    def opposite(self, v):
        return self._destination if v is self._origin else self._destination

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))

if __name__ == '__main__':
    edge = Edge('a', 'b', 1)
    print(edge.element())
    h = hash(edge)
    print(h)