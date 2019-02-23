#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "28 janvier 2018"
#
# Programme Python pour IFT2015/Types abstraits/Liste
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# utilise la fonction getsize de sys
import sys

data = [ ]
for k in range( 32 ):
    a = len(data) # nombre d'éléments
    b = sys.getsizeof(data) # taille en bytes
    print( 'Taille: {0:3d}; Capacité en bytes: {1:4d}'.format(a, b))
    data.append( None ) # ajout de 1 élément
    
