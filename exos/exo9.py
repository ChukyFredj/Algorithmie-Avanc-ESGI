from utilitary import *

def exo_9():
    """
    Script permettant de rentrer un nombre renvoyant TRUE si c'est un palindrome
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        n = input("Entrez un nombre : ")
        if n == n[::-1]:
            print("Le nombre", n, "est un palindrome.")
        else:
            print("Le nombre", n, "n'est pas un palindrome.")
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break