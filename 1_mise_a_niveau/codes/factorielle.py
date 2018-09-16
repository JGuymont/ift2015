#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "7 janvier 2014"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input une valeur entière
# et retourne en output la factorielle de cette valeur.

# utilise sys pour saisir les arguments de la ligne de commande
import sys

# utilise time pour mesure le temps d'exécution
import time

# utilise optparse pour parser la ligne de commande
from optparse import OptionParser

# Usage: factorielle.py [options]
#
# Options:
#   -h, --help     show this help message and exit
#   -n N, --n=N    entier positif
#   -v, --verbose  trace les appels récursifs de la fonction factorielle

# Fonction principale
def main( argv ):

    # variables globales pour les options et arguments
    global opts
    global args

    # mettre les options et arguments
    parser = OptionParser()
    parser.add_option( "-n", "--n", dest = "n", default = 0,
                       help = "entier positif", metavar = "N" )
    parser.add_option( "-v", "--verbose",
                       action = "store_true", dest = "verbose", default = False,
                       help = "trace les appels récursifs de la fonction factorielle" )

    # parse the options and arguments
    opts, args = parser.parse_args()

    # s'assurer que n est un entier positif
    try:
        n = int( opts.n )
    except ValueError:
        print( opts.n, "n'est pas un entier !" )
        exit()

    # ici n est un entier
    # on s'assure qu'il est positif
    if n < 0:
        print( n, "doit être un entier positif !" )
        exit()
    else:

        # Calculer la factorielle de cet entier et
        # sauvegarder le résultat dans une variable locale.
        # On peut activer ou non la trace d'exécution de
        # la fonction en 2è argument qui par défaut est False.

        avant = time.time()
        fact = factorielle( n, opts.verbose )
        apres = time.time()
        
        # Afficher le résultat
        print( 'La factorielle de', n, 'est', fact, 'calculée en', apres - avant, 'secondes' )

# Fonction factorielle d'un entier positif n:
#  n! = 1, si n = 0; n.(n-1).(n-2). ... 3.2.1 si n >= 1
#    donne le nombre de permutations de n objets distincts.
#    Par exemple, on peut permutter les trois caractères x, y et z
#    de 3! = 3.2.1 = 6 manières différentes: xyz, xzy, yxz, yzx,
#    zxy et zyx.
#    La fonction possède une definition récursive naturelle, par
#    exemple 13! = 13.12!, et n! = 1 si n = 0; n.(n-1)! si n >= 1.
#    0! représente le cas de base qui n'est pas definit recursivement,
#    le f( n-1 ) dans n x f( n-1 ) représente le cas récursif.
#    Trace d'exécution possible avec le 2è argument par défaut à False.
#    La profondeur d'exécution est initialisée à 0 et on l'utilise
#    pour indenter l'affichage de l'appel de la fonction.

def factorielle( n, trace = False, profondeur = 0 ):
    if n == 0:
        return 1
    else:
        if( trace ):
            print( profondeur * ' ', n, '* factorielle(', n - 1, ')' )
        return n * factorielle( n-1, trace, profondeur+1 )

#    La fonction n'utilise pas d'énoncé de boucle car la répétition
#    est créée par des appels récursifs successifs. Il n'y a pas
#    de circularité car chaque fois l'appel s'applique à un argument
#    de plus en plus petit jusqu'au cas de base.

# Appeler la fonction principale
if __name__ == "__main__":
   main( sys.argv[1:] )
