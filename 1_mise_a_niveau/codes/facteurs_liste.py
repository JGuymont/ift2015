#!/usr/bin/python3

# author = "Francois Major"
# date = "11 janvier 2014"
# version = "1.0"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Facteurs d'un entier
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input une valeur entière
# et retourne en output les facteurs de cette valeur.
def main():
    # Prompter l'usager et
    # lire en entrée un entier
    print( "Ce programme retourne les facteurs d'un entier positif." )
    try:
        n = int( input( 'Entrez un entier positif : ' ) )
    except ValueError:
        print( "Ce n'est pas un entier !" )
        exit()

    # Ici n contient une valeur entière
    # Si n est positif, on envoit à l'usager ses facteurs
    # Sinon, on envoit un message d'erreur

    if n >= 0:
        print( 'Les facteurs de', n, 'sont :', facteurs( n ) )
    else:
        print( "L'entier entré n'est pas positif. " )


# Fonction facteurs retourne dans une liste
# les facteurs d'un entier positif n.
def facteurs( n ):
    # liste pour stocker les facteurs de n
    # initialement vide
    resultats = []

    # pour chaque entier k de 1 à n
    # si n se divise entièrement par k (vérifié par modulo)
    # alors k est un facteur de n
    for k in range( 1, n + 1 ):
        if n % k == 0:
            # division entière
            # on ajoute le facteur à la fin de la liste
            resultats.append( k )
    return resultats

# Appel de la fonction principale
main()




