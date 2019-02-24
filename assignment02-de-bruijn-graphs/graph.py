"""IFT2015 - Assignment 2 - De Brujin graph

@author J. Guymont
@date 11 nov. 2018
"""
import random
import string
from itertools import islice

class DeBrujinGraph:
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
        """
        self.genomic_alphabet = genomic_alphabet
        self._nodes = set(nodes)
    
    def __contains__(self, N):
        """
        Détermine si le graphe de Brujin contient le noeud N
        """
        return N in self.nodes()
    
    def __iter__(self):
        """
        Retourne un itérable sur les noeuds du graphe
        """
        return self.nodes()
    
    def load_factor(self):
        """
        Calcule le facteur de charge de la table de hachage sous-jacente
        """
        pass
    
    def add(self, N):
        """
        Ajoute le noeud N au graphe
        """
        assert type(N) is str
        pass 
    
    def remove(self, N):
        """
        Enlève le noeud N du graphe
        """
        assert type(N) is str
        pass

    def nodes(self):
        """
        Retourne un itérable `str` sur les noeuds du graphe
        """
        return list(self._nodes)

    def edges(self):
        for k in self.nodes():
            for s in self.genomic_alphabet:
                successor = k[1:] + s
                if successor in self.nodes():
                    yield k, successor

    def predecessors(self, N):
        """
        Retourne tous les prédécesseur du noeud N
        """
        assert type(N) is str
        for x in self.genomic_alphabet:
            yield x + N[:-1]

    def successors(self, N):
        """Retourne tous les successeurs du noeud N
        
        return all forward neighbors of the k-mer `N`
        """
        assert type(N) is str
        for x in self.genomic_alphabet:
            yield N[1:] + x

    def kmer_walk(self, start):
        """
        reconstruct the original sequence        
        """
        k = start
        yield k # yield the starting node

        while True:
            for symbol in self.genomic_alphabet:
                candidate = k[1:] + symbol
                if candidate in self.nodes():
                    k = candidate
                    yield k
                    break
            else:
                break # break the while-loop if no more candidate is found

    def get_contig(self, start, contig=None):
        visited = set()
        for k in self.kmer_walk(start):
            if contig is None:
                contig = k
            else:
                contig += k[-1]
            if k in visited:
                break # stop traversal on repeat
            else:
                visited.add(k)
        return contig

    @staticmethod
    def get_kmers(sequence, k=21):
        l = len(sequence)
        return [sequence[i:i+k] for i in range(l - k + 1)]


if __name__ == '__main__':
    random.seed(123) # recommendé pour des résultats reproduisibles!
    segment = ''.join(random.choices('ACGT', k=10))
    #segment = 'ATGCGAGTCTCCACGTCAGTCAACGGTGGTG'
    print(segment)
    kmers = DeBrujinGraph.get_kmers(segment, k=7)
    graph = DeBrujinGraph(kmers)
    contig = graph.get_contig(start=segment[:7])
    print(contig)
    print(contig==segment)

    
    




