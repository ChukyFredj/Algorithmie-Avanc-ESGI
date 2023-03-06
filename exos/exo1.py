from utilitary import *


def exo_1():
    """
    Script permettant de rentrer une chaine de caractères et d'inverser une chaine de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        chaine = input("Entrer une chaine de caractères : ")
        print("La chaine de caractères inversé : ", chaine[::-1])
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
