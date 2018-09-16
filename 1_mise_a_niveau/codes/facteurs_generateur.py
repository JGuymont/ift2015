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
        # La fonction facteurs retourne un générateur
        # des facteurs de n.
        # Pour former un output de type liste, on utilise
        # un iterateur et on ajoute les facteurs un à un
        # à une liste initialement vide.
        s = []
        for f in facteurs( n ):
            s.append( f )
        # on trie la liste puisque le générateur ne sort pas
        # les facteurs dans l'ordre
        s.sort()
        print( 'Les facteurs de', n, 'sont :', s )
    else:
        print( "L'entier entré n'est pas positif. " )


# Fonction facteurs utilise un générateur.
def facteurs( n ):
    # pour k allant de 1 à la racine carrée de n
    k = 1
    while k * k < n:
        if n % k == 0:
        # si n se divise par k
        # on génère sa valeur et son co-facteur
            yield k
            yield n // k
        k += 1
    # on arrête juste avant la racine carrée de n
    # sinon on insèrerait 2 fois sa valeur
    # alors si n contient un carré parfait
    # on le génère ici
    if k * k  == n:
        yield k

# Appel de la fonction principale
main()
