from utilitary import *

def exo_8():
    """
    Script qui crée une fonction qui prend en paramètre un nombre entier et qui trouve tous les paires de 1 à ce nombre donné
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        nombre = int(input("Entrer a : "))
        for i in range(1, nombre+1):
            if i % 2 == 0:
                print(i)

        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break