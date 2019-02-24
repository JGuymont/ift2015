"""Devoir 1 IFT2015

@author Jonathan Guymont

Script ecrit dans le cadre du cours IFT2015

"""


import numpy as np

class SparseMatrix:
    """CSR sparse matrix implementation.

    La classe SparseMatrix encode une matrice dense de dimension <n x m> 
    dans 3 vecteurs: `rowptr`, `colind` et `data`. Le vecteur `colind` 
    contient les indices des colonnes des valeurs non nulles. Le vecteur 
    `data` contient les valeurs non nulles. Le vecteur `rowptr` est contruit 
    iterativement de la facon suivante:

        rowptr[0] = 0 
        rowptr[i] = rowptr[i-1] + nombre d'elments non nul dans la ligne i-1
    
    Soit A la matrice dense original. Une matrice encoder avec SparseMatrix 
    retourne l'element de la position (i, j) de la facon suivante:
    Le nombre d'element non nulles qui sont dans les ligne precedentes est donne 
    par `rowptr[i]`. Ce qui veut dire que si A[i, j] est non nulle, alors j est 
    dans la liste 
    
        [colind[rowptr[i]], colind[rowptr[i]+1],..., colind[rowptr[i+1]-1]]
    
    Si j est egale a colind[k] pour rowptr[i] <= k < rowptr[i+1], alors A[i,j] = data[k], sinon A[i,j] = 0.  

    Arguments
        fromiter: (list) A list of tuple (i, j, v) containing the coordinates (i, j) 
            of the non-zero element of a dense matrix with the corresponding value `v`
        shape: (tuple) Dimension (n, m) of a dense matrix
    """

    def __init__(self, fromiter, shape): 
        n, m = shape 
        self.n = n 
        self.m = m 
        self.nnz = len(fromiter)  # nombre de valeurs non-nulles 
        self.rowptr = self._make_rowptr(fromiter) # liste de taille n + 1 des intervalles des colonnes 
        self.colind = [x[1] for x in fromiter] # liste de taille nnz des indices des valeurs non-nulles 
        self.data = [x[2] for x in fromiter]   # liste de taille nnz des valeurs non-nulles

    def _make_rowptr(self, fromiter):
        """Cree une liste de taille n+1 des intervalles des colonnes"""
        # `non_zero_counter` est une liste contenant le nombre 
        # d'elments non nul de chaque ligne
        non_zero_counter = [0]*self.n 
        for x in fromiter:
            non_zero_counter[x[0]] += 1
        rowptr = [0]*(self.n+1)
        for i in np.arange(1, self.n+1):
            rowptr[i] = rowptr[i-1] + non_zero_counter[i-1]
        return rowptr

    def _find_index(self, j, colind, first_idx, last_idx):
        """binary search: find index of j in O(log(m))"""
        n_idx = last_idx - first_idx # number of index to search
        if n_idx <= 2:
            return colind.index(j, first_idx, last_idx)
        median = first_idx + n_idx // 2
        if j == colind[median]:
            return median
        elif j < colind[median]:
            return self._find_index(j, colind, first_idx, median)
        elif j > colind[median]:
            return self._find_index(j, colind, median+1, last_idx)

    def __getitem__(self, k):
        """retourne la valeur correspondant à l'indice k=(i, j)"""
        i, j = k 
        n_prev = self.rowptr[i] # nombre d'element non nul des lignes precedentes
        n_curr = self.rowptr[i+1]
        if n_prev == n_curr:
            return 0
        cols = self.colind[n_prev:n_curr] # colonnes des element non nuls de la ligne i 
        try:
            idx_elmt = self._find_index(j, cols, first_idx=0, last_idx=len(cols))
        except ValueError:
            return 0                                             
        return self.data[n_prev+idx_elmt]
        
    def todense(self): 
        """Encode la matrice en format dense""" 
        return np.array([[self[i, j] for j in range(self.m)] for i in range(self.n)])

class SparseTensor: 
    """CSR implementation for a Tensor (or an array of dimension (l, n, m)).

    nnz est le nombre de valeur non nulle du tensor

    colind est une liste de taille nnz des indices des colonnes des valeurs non-nulles 

    rowptr est une lite de taille l*n + 1 et est construit de la facon suivante:

        rowptr[0] = 0
        s - 1 = i*n + j  
        rowptr[s] = rowptr[s-1] + #element de la ligne (i, j)

    Arguments:
        fromiter: (list) A list of tuple (i, j, k, v) containing the coordinates (i, j) 
            of the non-zero element of a dense matrix with the corresponding value `v`
        shape: (tuple) Dimension (l, n, m) of a dense tensor
    """

    def __init__(self, fromiter, shape):
        l, n, m = shape
        self.n = n 
        self.m = m 
        self.l = l
        self.nnz = len(fromiter)  # nombre de valeurs non-nulles 
        self.rowptr = self._make_rowptr(fromiter)
        self.colind = [x[2] for x in fromiter] # liste de taille nnz des indices des valeurs non-nulles 
        self.data = [x[3] for x in fromiter]   # liste de taille nnz des valeurs non-nulles

    def _count_non_zero(self, fromiter):
        """Retourne une liste de longueur l*n ou l'element de la 
        position s = i*n + j correspond au nombre de valeur non 
        nulle de la ligne (i, j)"""
        # nombre total de ligne si le tensor etait reshape 
        # dans les dimensions (l*n, m)
        n_rows = self.l*self.n 
        non_zero_counter = [0]*n_rows
        for coord in fromiter:
            i = coord[0]
            j = coord[1]
            non_zero_counter[i*self.n+j] += 1
        return non_zero_counter

    def _make_rowptr(self, fromiter):
        non_zero_counter = self._count_non_zero(fromiter)
        rowptr = [0]*(self.l*self.n + 1)
        rowptr[0] = 0
        for i in range(self.l):
            for j in range(self.n):
                s = i*self.n + j + 1  
                rowptr[s] = rowptr[s-1] + non_zero_counter[s-1]
        return rowptr 
    
    def _find_index(self, j, colind, first_idx, last_idx):
        """binary search: find index of j in O(log(m))"""
        n_idx = last_idx - first_idx # number of index to search
        if n_idx <= 2:
            return colind.index(j, first_idx, last_idx)
        median = first_idx + n_idx // 2
        if j == colind[median]:
            return median
        elif j < colind[median]:
            return self._find_index(j, colind, first_idx, median)
        elif j > colind[median]:
            return self._find_index(j, colind, median+1, last_idx)

    def __getitem__(self, coord):
        """retourne la valeur correspondant à l'indice coord=(i, j, k)"""
        i, j, k = coord
        s = i*self.n + j # jth row of the ith matrix
        n_prev = self.rowptr[s]
        n_curr = self.rowptr[s+1]
        if n_prev == n_curr:
            return 0
        cols = self.colind[n_prev:n_curr] # colonnes des element non nuls de la ligne j de l'image i
        try:
            idx_elmt = self._find_index(k, cols, first_idx=0, last_idx=len(cols))
        except ValueError:
            return 0                                             
        return self.data[n_prev+idx_elmt]
        
    def todense(self): 
        """Encode la matrice en format dense""" 
        dense = [[[self[i, j, k] for k in range(self.m)] for j in range(self.n)] for i in range(self.l)]
        return np.array(dense)

if __name__ == '__main__':
    mat = SparseMatrix(fromiter=[(0, 1, 1), (1, 0, 2), (2, 1, 4), (2, 2, 3)], shape=(3, 3))

