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

# utilise time
from time import time

# utilise optparse pour parser la ligne de commande
from optparse import OptionParser

# Usage: factorielle.py [options]
#
# Options:
#   -h, --help     show this help message and exit
#   -n N, --n=N    entier entre 0 et 100 à chercher dans la liste
#   -i, --iterativ utilise la version itérative
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
    parser.add_option( "-n", "--n", dest = "N", default = 0,
                       help = "entier entre 0 et 100 à chercher dans la liste", metavar = "N" )
    parser.add_option( "-c", "--nb", dest = "NB", default = None,
                       help = "comparaison de temps d'exéction avec NB itérations", metavar = "NB" )
    parser.add_option( "-i", "--iterativ",
                       action = "store_true", dest = "iterativ", default = False,
                       help = "utilise la version itérative" )
    parser.add_option( "-v", "--verbose",
                       action = "store_true", dest = "verbose", default = False,
                       help = "trace les appels récursifs de la recherche binaire" )

    # parse the options and arguments
    opts, args = parser.parse_args()

    # voir si on fait une comparaison de temps d'exécution
    if opts.NB is not None:
        try:
            nb = int( opts.NB )
            if nb > 0:
                # test la différence de temps d'exécution entre itératif et récursif
                debut = time()
                for _ in range( 0, nb ):
                    recherche_binaire( data, 0, 0, len( data ) - 1, False )
                fin = time()
                print( nb, 'itérations pour la version récursive a pris', fin - debut, 'secondes' )

                debut = time()
                for _ in range( 0, nb ):
                    recherche_binaire_iterative( data, 0 )
                fin = time()
                print( nb, 'itérations pour la version itérative a pris', fin - debut, 'secondes' )
                exit()
        except ValueError:
            print( opts.NB, "n'est pas un entier !" )
            exit()

    # s'assurer que n est un entien entre 0 et 100
    try:
        n = int( opts.N )
    except ValueError:
        print( opts.N, "n'est pas un entier !" )
        exit()

    # ici n est un entier
    # on s'assure qu'il est entre 0 et 100
    if n < 0 or n > 100:
        print( n, "doit être entre 0 et 100 !" )
        exit()
    else:
        # on cherche l'entier entré
        # soit par la méthode récursive ou itérative selon l'option iterativ
        if opts.iterativ:
            trouve = recherche_binaire_iterative( data, n )
        else:
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

def recherche_binaire_iterative( data, cible ):
    min = 0
    max = len( data ) - 1
    while min <= max:
        milieu = ( min + max ) // 2
        if cible == data[ milieu ]:
            return True
        elif cible < data[ milieu ]:
            max = milieu - 1
        else:
            min = milieu + 1
    return False

# Appeler la fonction principale
if __name__ == "__main__":
   main( sys.argv[1:] )
