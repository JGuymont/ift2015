#!/usr/bin/python3

# author = "Francois Major"
# date = "11 janvier 2014"
# version = "1.0"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Facteurs d'un entier
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input un entier > 0, k,
# et retourne en output le kième terme de la suite
# de Fibonacci
def main():
    # Prompter l'usager et
    # lire en entrée l'entier k
    print( "Ce programme retourne le kième terme de la suite de Fibonacci." )
    try:
        k = int( input( 'Entrez un entier k plus grand que 0 : ' ) )
    except ValueError:
        print( "Ce n'est pas un entier !" )
        exit()

    # Ici k contient une valeur entière
    # Si k est positif, on envoit à l'usager le kième terme de la suite
    # Sinon, on envoit un message d'erreur
    if k > 0:
        # on retient le rang du terme extrait de la suite à partir de 1
        rang = 1
        for fibo in fibonacci():
            if rang == k:
                # fibo contient le kème nombre de la suite
                # on le retourne à l'usager et on sort
                print( "Le kème élément de la suite de Fibonacci est : ", str( fibo ) )
                break
            # on est pas rendu au kième terme, on incrémente rang car au prochain
            # tour on va aller chercher le prochain
            rang += 1
    else:
        print( "L'entier entré n'est pas plus grand que 0. " )


# Fonction fibonacci utilisant un generateur infini
def fibonacci( ):
    # la suite débute avec 0, 1
    # par la suite c'est la somme des deux nombres précédents
    # on utilise a et b pour stocker ces deux nombres
    # en débutant avec 0 et 1
    a = 0
    b = 1
    # on boucle à l'infini...
    while True:
        # on ajoute a à la suite
        yield a
        # on sauvegarde la somme des 2 derniers nombres
        portee = a + b # Fibonacci calcule des portées de lapins !
        # on avance de 2 positions dans la suite
        # a prend la valeur du nombre suivant, b
        a = b
        # b devient le nouveau nombre généré
        b = portee

# Appel de la fonction principale
main()


