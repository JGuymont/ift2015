#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "23 mars 2014"
#
# Programme Python pour IFT2015/5 Dictionnaires/5.1 Dictionnaire
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

#collections inclut MutableMapping
import collections

#ADT Map (Classe de base)
class Map( collections.MutableMapping ):

    #classe imbriquée pour les éléments ( clé, valeur )
    class _Item:
        #enregistrement statique et efficace
        __slots__ = '_key', '_value'

        #constructeur avec valeur None de défaut pour valeur
        def __init__( self, k, v = None ):
            self._key = k
            self._value = v

        #égalité de clé
        def __eq__( self, other ):
            return self._key == other._key

        #non-égalité de clé
        def __ne__( self, other ):
            return not( self == other )

        #clé strictement inférieure
        def __lt__( self, other ):
            return self._key < other._key

        #clé supérieure ou égale
        def __ge__( self, other ):
            return self._key >= other._key

        #prettyprint d'un élément
        def __str__( self ):
            return "<" + str( self._key ) + "," + str( self._value ) + ">"

        #accède la clé
        def key( self ):
            return self._key

        #accède la valeur
        def value( self ):
            return self._value

    #Map vide?
    def is_empty( self ):
        return len( self ) == 0

    #prettyprint de Map
    def __str__( self ):
        if self.is_empty():
            return "{}"
        pp = "{"
        for item in self.items():
            pp += str( item )
        pp += "}"
        pp += " size = "
        pp += str( len( self ) )
        return pp

    #accède l'élément de clé k
    #retourne sa valeur s'il existe, d sinon
    #efficacité de __getitem__ va dépendre de
    #son implémentation dans la sous-classe
    def get( self, k, d = None ):
        try:
            tmp = self[k]
            return tmp
        except KeyError:
            return d

    #assigne et retourne l'élément de clé k
    #rien ne change si il existe, prend la valeur d sinon
    #efficacité de __getitem__ va dépendre de
    #son implémentation dans la sous-classe
    def setdefault( self, k, d = None ):
        try:
            tmp = self[k]
            return tmp
        except:
            self[k] = d
            return d

