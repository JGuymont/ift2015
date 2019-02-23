#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "8 janvier 2014"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input une valeur entière
# et la recherche dans une séquence indexable
# telle une liste en python

# utilise sys pour saisir les arguments de la ligne de commande
import sys

# utilise optparse pour parser la ligne de commande
from optparse import OptionParser

# Usage: factorielle.py [options]
#
# Options:
#   -h, --help     show this help message and exit
#   -n N, --n=N    entier entre 0 et 100 à chercher dans la liste
#   -v, --verbose  trace les appels récursifs de la recherche binaire

# Fonction principale
def main( argv ):

    data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
    # Imprimer en output les data
    print( data )

    # variables globales pour les options et arguments
    global opts
    global args

    # mettre les options et arguments
    parser = OptionParser()
    parser.add_option( "-n", "--n", dest = "n", default = 0,
                       help = "entier entre 0 et 100 à chercher dans la liste", metavar = "N" )
    parser.add_option( "-v", "--verbose",
                       action = "store_true", dest = "verbose", default = False,
                       help = "trace les appels récursifs de la recherche binaire" )

    # parse the options and arguments
    opts, args = parser.parse_args()

    # s'assurer que n est un entien entre 0 et 100
    try:
        n = int( opts.n )
    except ValueError:
        print( opts.n, "n'est pas un entier !" )
        exit()

    # ici n est un entier
    # on s'assure qu'il est entre 0 et 100
    if n < 0 or n > 100:
        print( n, "doit être entre 0 et 100 !" )
        exit()
    else:
        # on cherche l'entier entré
        trouve = recherche_binaire( data, n, 0, len( data ) - 1, opts.verbose )
        if trouve is not None:
            print( "J'ai trouvé", n, "dans data à l'index", trouve, '!' )
        else:
            print( "Je n'ai pas trouvé", n, 'dans data !' )

# Fonction recherche binaire d'un élément cible dans une
# séquence de données implantée avec une liste. La liste,
# la cible, et les indices min et max qui bornent la recherche
# dans la séquence sont passés en arguments.
def recherche_binaire( data, cible, min, max, trace = False, profondeur = 0 ):
    if trace:
        print( profondeur * ' ', 'recherche_binaire(', data[min:max+1], ',', cible, ',', min, ',', max, ',', trace, ')', )
    if min > max:
        # liste vide
        return None #interval vide, pas de match
    else:
        # on essaye au milieu
        milieu = (min + max) // 2
        if cible == data[milieu]:
            # la cible est au milieu, eureka !
            return milieu
        elif cible < data[milieu]:
            # cible plus petite que la valeur au milieu
            # on cherche la portion gauche de la liste
            return recherche_binaire( data, cible, min, milieu-1, trace, profondeur+1 )
        else:
            # cible plus grande que la valeur au milieu
            # on cherche la portion droite de la liste
            return recherche_binaire( data, cible, milieu+1, max, trace, profondeur+1 )

# Appeler la fonction principale
if __name__ == "__main__":
   main( sys.argv[1:] )
