#!/usr/bin/python3
"""
Representation of a simple graph using an adjacency map.

Internally, we manage the directed case by having two different top-level dictionary
instances, outgoing and incoming, such that _outgoing[v] maps to another
dictionary representing I_out(v), and _incoming[v] maps to a representation of I_in(v).

In order to unify our treatment of directed and undirected graphs, we continue to
use the outgoing and incoming identifiers in the undirected case, yet as aliases
to the same dictionary. For convenience, we define a utility named is_directed to
allow us to distinguish between the two cases.
"""
from graph.vertex import Vertex
from graph.edge import Edge

class Graph:
    """
    Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    def __init__(self, directed=False):
        self._outgoing = {}                                 # outgoing incidence collection e.g. if u --> v
                                                            # then v is in _outgoing[u]
        self._ingoing = {} if directed else self._outgoing  # ingoing incidence collection
        self.Vertex = Vertex
        self.Edge = Edge

    def __str__(self):
        vertices = set([str(v) for v in self.vertices()])
        edges = set([str(e) for e in self.edges()])
        return "G(V={vertices}, E={edges})".format(vertices=vertices, edges=edges)

    def is_directed(self):
        return self._outgoing is not self._ingoing
    
    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._ingoing
        return len(adj[v])

    def edge_count(self):
        count = [self.degree(v) for v in self._outgoing]
        return count if self.is_directed else count // 2
    
    def edges(self):
        edges = set()
        for incidence_collection in self._outgoing.values():
            edges.update(incidence_collection.values())
        return edges

    def get_edges(self, u, v):
        """
        return the edge from u to v or None if u
        and v are not adjacent.
        """
        incident_edges = self._outgoing.get(u)
        return incident_edges.get(v) if incident_edges is not None else None 

    def incident_edges(self, v, outgoing=True):
        incident_edges = self._outgoing.get(v) if outgoing else self._ingoing.get(v) 
        return incident_edges.values() if incident_edges is not None else None

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed:
            self._ingoing[v] = {}
        return v
    
    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._ingoing[v][u] = e
