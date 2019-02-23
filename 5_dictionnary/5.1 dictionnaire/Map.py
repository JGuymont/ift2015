#!/usr/local/bin/python3
"""
Expected behavior:
    map = Map()
"""

import collections

class Map(collections.MutableMapping):
    """
    ADT Map (Classe de base)
    """
    
    class _Item:
        """
        classe imbriquée pour les éléments (clé, valeur)
        """

        __slots__ = '_key', '_value'

        def __init__( self, k, v = None ):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not self == other

        def __lt__(self, other):
            return self._key < other._key

        def __ge__(self, other):
            return self._key >= other._key

        def __str__(self):
            return "<" + str(self._key) + "," + str(self._value) + ">"

        def key(self):
            return self._key

        def value( self ):
            return self._value

    def is_empty( self ):
        return len( self ) == 0

    #prettyprint de Map
    def __str__( self ):
        if self.is_empty():
            return "{}"
        pp = "{"
        for item in self.items():
            pp += str(item)
        pp += "}"
        pp += " size = "
        pp += str( len( self ) )
        return pp

    def get(self, k, d=None):
        """
        Accèder l'élément de clé k
        retourne sa valeur s'il existe, d sinon
        efficacité de __getitem__ va dépendre de
        son implémentation dans la sous-classe
        """
        try:
            tmp = self[k]
            return tmp
        except KeyError:
            return d

    def setdefault(self, k, d = None):
        """
        assigne et retourne l'élément de clé k
        rien ne change si il existe, prend la valeur d sinon
        efficacité de __getitem__ va dépendre de
        son implémentation dans la sous-classe
        """
        try:
            tmp = self[k]
            return tmp
        except:
            self[k] = d
            return d
