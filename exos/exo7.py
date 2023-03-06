from utilitary import *

def mod(a,b):
    return a%b

def exo_7():
    """
    Script prenant en un nombre entier impair et renvoye la somme de tous les nombres impairs inférieurs à cet entier
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        n = int(input("Entrez un nombre entier impair : "))
        if n % 2 == 0:
            print("Erreur : le nombre n'est pas impair.")
        else:
            somme = 0
            for i in range(1, n, 2):
                somme += i
            print("La somme de tous les nombres impairs inférieurs à", n, "est :", somme+n)

        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break