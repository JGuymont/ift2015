"""IFT2015 - Assignment 2 - De Brujin graph

@author J. Guymont
@date 11 nov. 2018
"""
import random
import base64
import hashlib
import string
import collections
from itertools import islice


class Map(collections.MutableMapping):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v=None):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not(self == other)

        def __lt__(self, other):
            return self._key < other._key

        def __ge__(self, other):
            return self._key >= other._key

        def key(self):
            return self._key

        def value(self):
            return self._value

    def is_empty(self):
        return len(self) == 0

    def get(self, k, d=None):
        try:
            tmp = self[k]
            return tmp
        except KeyError:
            return d

    def setdefault(self, k, d=None):
        try:
            tmp = self[k]
            return tmp
        except:
            self[k] = d
            return d


class UnsortedListMap(Map):

    def __init__(self):
        self._T = []

    def __getitem__(self, k):
        for item in self._T:
            if k == item._key:
                return item._value
        raise KeyError(k)

    def __setitem__(self, k, v):
        for item in self._T:
            if k == item._key:
                item._value = v
                return
        self._T.append(self._Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._T)):
            if k == self._T[j]._key:
                self._T.pop(j)
                return
        raise KeyError(k)

    def __len__(self):
        return len(self._T)

    def __iter__(self):
        for item in self._T:
            yield item._key

    def __items__(self):
        for item in self._T:
            yield (item._key, item._value)


class DeBrujinGraph(Map):
    """De Brujin graph

    Implémentation de la structure de données du graphe de Brujin
    à avec une table de hachage. Le constructeur prend
    en entrée un itérable sur des `string` de
    longueur `k`.

    Puisque l'itérable est de longueur arbitraire, la table de hachage
    est redimensionner dynamiquement pour maintenir un facteur de charge
    sous 0.75 par default.

    Args
        nodes: (str)
        k: (int)
        max_charge: (float)
    """

    GENOMIC_ALPHABET = 'ACGT'

    def __init__(self, nodes, k=21, max_charge=0.75, genomic_alphabet=GENOMIC_ALPHABET):
        """
        Initialise la structure de données

        Args

        """
        self._genomic_alphabet = genomic_alphabet
        self._char2int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        self._start = nodes[0]
        self._nodes = set(nodes)
        self._size = int(len(self._nodes) / max_charge)
        self._T = [None] * self._size
        self._n = 0
        self._max_charge = max_charge
        for node in self._nodes:
            self.add(node)

    def _hash_function(self, string):
        total = 0
        for i, c in enumerate(list(string)):
            total += self._char2int[c] * 4**i
        return total % self._size

    def __len__(self):
        return self._n

    def __contains__(self, N):
        """
        Détermine si le graphe de Brujin contient le noeud N
        """
        return N in self.nodes()

    def __getitem__(self, node):
        """
        retourne les arcs sortant d'un noeud
        """
        j = self._hash_function(node)
        bucket = self._T[j]
        if bucket is None:
            raise KeyError(node)
        return bucket[node]

    def __setitem__(self, node, edges):
        j = self._hash_function(node)
        if self._T[j] is None:
            self._T[j] = UnsortedListMap()
        oldsize = len(self._T[j])
        self._T[j][node] = edges
        if len(self._T[j]) > oldsize:
            self._n += 1
        if self._n > int(self._max_charge * len(self._T)):
            c = int(len(self._T) / self._max_charge - 1)
            if c > self._size:
                self._resize(c)

    def __delitem__(self, k):
        j = self._hash_function(k)
        bucket = self._T[j]
        if bucket is None:
            raise KeyError(k)
        try:
            del bucket[k]
            self._n -= 1
            return
        except KeyError:
            raise KeyError(k)

    def add(self, node):
        self[node] = self._outgoing_edge(node)

    def _resize(self, c):
        old = list(self.items())
        self._T = c * [None]
        self._n = 0
        self._size = c
        for k, v in old:
            self[k] = v

    def __iter__(self):
        """
        Retourne un itérable sur les noeuds du graphe
        """
        for bucket in self._T:
            if bucket is not None:
                for node in bucket:
                    yield node

    def start(self):
        return self._start

    def load_factor(self):
        """
        Calcule le facteur de charge de la table de hachage sous-jacente
        """
        return round(self._n / self._size, 2)

    def _outgoing_edge(self, node):
        return [(node, next_node) for next_node in self.successors(node) if next_node in self._nodes]

    def remove(self, N):
        """
        Enlève le noeud N du graphe et les arcs
        incidentes a ce noeuds
        """
        del self[N]
        for node, edge in self.items():
            if N in edge:
                self[node].remove(edge)

    def nodes(self):
        """
        Retourne un itérable `str` sur les noeuds du graphe
        """
        for node in self._nodes:
            yield node

    def predecessors(self, N):
        """
        Retourne tous les prédécesseur du noeud N
        """
        assert type(N) is str
        for x in self._genomic_alphabet:
            yield x + N[:-1]

    def successors(self, N):
        """Retourne tous les successeurs du noeud N

        return all forward neighbors of the k-mer `N`
        """
        assert type(N) is str
        for x in self._genomic_alphabet:
            yield N[1:] + x

    def is_empty(self):
        return all([not edges for edges in self.values()])

    @staticmethod
    def assemble_segment(nodes):
        path = None
        for node in nodes:
            if path:
                path += node[-1]
            else:
                path = node
        return path

    @staticmethod
    def kmer_walk(graph):
        search = [[[], graph.start(), graph]]
        while search:
            path, node, undiscovered = search.pop()
            path.append(node)
            if undiscovered.is_empty():
                return graph.assemble_segment(path)
            for edge in undiscovered[node]:
                undiscovered[node].remove(edge)
                search.append([path, edge[1], undiscovered])

    @staticmethod
    def get_kmers(sequence, k=21):
        l = len(sequence)
        return [sequence[i:i + k] for i in range(l - k + 1)]


if __name__ == '__main__':
    random.seed(123)
    segment = ''.join(random.choices('ACGT', k=10))
    kmers = DeBrujinGraph.get_kmers(segment, k=2)
    graph = DeBrujinGraph(kmers)
    print(graph.load_factor())
    contig = DeBrujinGraph.kmer_walk(graph)
    print(segment)
    print(contig)
    print(segment in contig)
