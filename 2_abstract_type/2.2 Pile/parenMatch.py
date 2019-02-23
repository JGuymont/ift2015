#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "15 février 2014"
#
# Programme Python pour IFT2015/Types abstraits/Pile
#
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input une expression
# contenant des (), [] et {} et vérifie si ces
# symboles sont bien balancés

# utilise ListStack
from ListStack import ListStack

# Fonction principale
def main():
    # Lire en input une expression
    expr = input( 'Entrez une expression: ' )
    if parenMatch( expr ):
        print( "L'expression ", expr, "est balancée !" )
    else:
        print( "L'expression ", expr, "n'est pas balancée !" )

# fonction parenMatch vérifie si l'expression
# passée en argument est balancée en (), [] et {}
def parenMatch( expr ):
    # symboles de gauche
    aGauche = "({["
    # symboles de droite
    aDroite = ")}]"

    # utilise pile S
    S = ListStack()

    # pour chaque caractère dans l'expression
    for c in expr:
        # si on rencontre un caractère de gauche
        if c in aGauche:
            # on l'empile
            S.push( c )
        elif c in aDroite:
            # si on a un symbole de droite
            if S.is_empty():
                # si la pile est vide, pas de match
                return False
            if aDroite.index( c ) != aGauche.index( S.pop() ):
                # si le symbole à droite ne match pas le symbole à gauche
                return False
    # ici, si la pile est vide, l'expression est balancée
    # sinon il reste un ou des symbole(s) non balancés dans la pile
    return S.is_empty()

# Appeler la fonction principale
main()
