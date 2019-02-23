#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "9 février 2014"
#
# Programme Python pour IFT2015/Types abstraits/Liste
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Module pour créer des tableaux
import ctypes

class DynamicArray:

    # retourne un pointeur sur une zone mémoire
    # pouvant stocker c objets Python contigus
    def _makeArray( self, c ):
        return( c * ctypes.py_object )()

    # constructeur
    # on commence avec 1 élément
    def __init__( self ):
        # nombre d'éléments dans le tableau
        self._n = 0
        # capacité : nombre d'éléments maximum possible
        self._capacity = 1
        # référence au tableau
        self._A = self._makeArray( self._capacity )

    # convertir un tableau en chaînes de caractères
    # utilisant les crochets pour délimiter le tableau
    # des virgules pour séparer les éléments
    # indiquant la capacité courante du tableau
    def __str__( self ):
        if self._n == 0:
            return "[](size = 0; capacity = " + str( self._capacity ) + ")"
        pp = "[" + str( self._A[0] )
        for k in range( 1, self._n ):
            pp += ", " + str( self._A[k] )
        pp += "](size = " + str( self._n )
        pp += "; capacity = " + str( self._capacity ) + ")"
        return pp      

    # retourne le nombre d'éléments dans le tableau
    def __len__( self ):
        return self._n

    # retourne la capacité courante
    def capacity( self ):
        return self._capacity

    # retourne l'élément à l'index k
    # notation avec crochets
    def __getitem__( self, k ):
        if not 0 <= k < self._n:
            raise IndexError( 'index out of bounds' )
        return self._A[k]

    # retourne l'élément à l'index k
    def get( self, k ):
        if not 0 <= k < self._n:
            raise IndexError( 'index out of bounds' )
        return self._A[k]

    # ajoute à la fin du tableau
    def append( self, obj ):
        # si le tableau est plein
        if self._n == self._capacity:
            # on double sa capacité
            self._resize( 2 * self._capacity )
        # on ajoute le nouvel élément à la fin du tableau
        self._A[self._n] = obj
        # on incrémente le nombre d'éléments
        self._n += 1

    #remove and return the ith element of the list
    def remove( self, i ):
        # on vérifie si i est un index valide
        if not 0 <= i < self._n:
            raise IndexError( 'index out of bounds' )
        obj = self._A[i]
        # on décale les éléments i+1 à n-1
        for k in range( i+1, self._n ):
            self._A[k-1] = self._A[k]
        # on décrémente le nombre d'éléments
        self._n -= 1
        self._A[self._n] = None #avoid loitering
        return obj

    #retourne et retire le dernier élément du tableau
    def pop( self ):
        # si le tableau est vide, on ne peut pas retirer d'élément
        if self._n == 0:
            raise IndexError( 'index out of bounds' )
        else:
            # on garde une référence à l'objet à retourner
            obj = self._A[self._n - 1]
            # on met la valeur du dernier élément à None
            # pour libérer la mémoire (garbage collection)
            self._A[self._n - 1] = None # avoid loitering
        # on décrémente le nombre d'éléments
        self._n -= 1
        # si l'occupation descend au quart ou moins
        if self._n <= self._capacity / 4:
            # on réduit la capacité de 2 fois
            self._resize( self._capacity // 2 )
        return obj

    # trouve et retourne l'index d'un élément si dans la liste
    # None sinon
    def find( self, obj ):
        # on parcourt les éléments de la liste
        for k in range( self._n ):
            # si l'élément est trouvé
            if self._A[k] == obj:
                # on retourne son index
                return k
        # ici l'élément n'a pas été trouvé, on retourne None
        return None

    # redimensionne le tableau à capacité c
    def _resize( self, c ):
        # on crée un nouveau tableau de capacité c
        B = self._makeArray( c )
        # on copie les éléments de l'ancien tableau dans le nouveau
        for k in range( self._n ):
            B[k] = self._A[k]
        # on garde la référence sur le nouveau tableau
        self._A = B
        # on met sa capacité à c
        self._capacity = c

"""unit testing
"""
if __name__ == '__main__':

    data = DynamicArray()
    print( data )

    data.append( 'titi' )
    print( "append( 'titi' )" )
    print( data )
    data.append( 'toto' )
    print( "append( 'toto' )" )
    print( data )
    data.append( 'tata' )
    print( "append( 'tata' )" )
    print( data )
    data.append( 'lastit' )
    print( data )

    idx = data.find( 'titi' )
    if idx is not None:
        print( "found titi ranked", idx )
    else:
        print( "titi not found" )
    idx = data.find( 'cece' )
    if idx is not None:
        print( "found cece ranked", idx )
    else:
        print( "cece not found" )

    print( "remove( 0 ) = ", data.remove( 0 ) )
    print( data )
    print( "remove( 1 ) = ", data.remove( 1 ) )
    print( data )
    print( "remove( 0 ) = ", data.remove( 0 ) )
    print( data )
    print( "pop() = ", data.pop() )
