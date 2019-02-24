"""Devoir 1 IFT2015

@author Jonathan Guymont

Script ecrit dans le cadre du cours IFT2015

"""

import numpy as np
import matplotlib.pyplot as plt

from sparse import SparseMatrix, SparseTensor

MNIST_DATASET = np.memmap('train-images-idx3-ubyte', offset=16, shape=(60000, 28, 28))

def array_to_coord(dense):
    coord = []
    n, m = dense.shape
    for i in range(n):
        for j in range(m):
            if not dense[i, j] == 0:
                coord.append((i, j, dense[i, j]))
    return n, m, coord

def tensor_to_coord(tensor):
    l, n, m = tensor.shape
    coord = []
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if not tensor[i, j, k] == 0:
                    coord.append((i, j, k, tensor[i, j, k]))
    return l, n, m, coord

def question2():
    first_image1 = np.array(MNIST_DATASET[0].tolist())
    n, m, coord = array_to_coord(first_image1)
    mat = SparseMatrix(fromiter=coord, shape=(n, m))
    first_image2 = mat.todense()
    for i in range(n):
        for j in range(m):
            if not first_image1[i, j] == first_image2[i, j]:
                print('Erreur, les images sont differentes')
                return None
    print('Les deux images sont identiques')
    return None

def question4b():
    dense_tensor = np.array(MNIST_DATASET)
    l, n, m, coords = tensor_to_coord(dense_tensor)
    sparse_tensor = SparseTensor(coords, shape=(l, m, n))
    recon_tensor = sparse_tensor.todense()
    for i in range(l):
        if not (dense_tensor[i]==recon_tensor[i]).all():
            print('Erreur, les tensor sont differentes')
            return None
    print('Les deux tensor sont identiques')
    return None

def question4c():
    dense_tensor = np.array(MNIST_DATASET)
    l, n, m, coords = tensor_to_coord(dense_tensor)
    sparse_tensor = SparseTensor(coords, shape=(l, m, n))
    rowptr = sparse_tensor.rowptr  
    print('nnz:', sparse_tensor.nnz)
    print('lenght rowptr:', len(rowptr))
    zero_row = 0
    for i, _ in enumerate(rowptr[:-1]):
        if rowptr[i+1] == rowptr[i]:
            zero_row += 1
    print('number of null row:', zero_row)

def question5():
    tensor = np.array(MNIST_DATASET)
    l, n, m, coords = tensor_to_coord(tensor)  
    sparse_tensor = SparseTensor(coords, shape=(l, m, n))
    nnz = sparse_tensor.nnz
    print("Nombre d'element non nul nnz du tensor: {}".format(nnz))
    print('Espace occupe par colind: {}'.format(len(sparse_tensor.colind)))
    print('Espace occupe par data: {}'.format(len(sparse_tensor.data)))
    print('Espace occupe par rowptr: {}'.format(len(sparse_tensor.rowptr)))
    total_space = len(sparse_tensor.data) + len(sparse_tensor.colind) + len(sparse_tensor.rowptr)
    print('Espace total occupe par sparse_tensor: {}'.format(total_space))
    print('Espace total occupe par le tensor dense: {}'.format(l*n*m))  

if __name__ == '__main__':

    question2()
    #question4b()
    #question4c()
    #question5()