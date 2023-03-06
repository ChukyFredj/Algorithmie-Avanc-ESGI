from utilitary import *

def mod(a,b):
    return a%b

def exo_10():
    """
    Script permettant de calculer La distance de Hamming entre deux chaine de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        chaine1 = input("Entrer une chaine de caractères : ")
        chaine2 = input("Entrer une autre chaine de caractères : ")

        if len(chaine1) != len(chaine2):
            print("Les deux chaine de caractères doivent être de même longueur.")
        else:
            distance = 0
            for i in range(len(chaine1)):
                if chaine1[i] != chaine2[i]:
                    distance += 1
            print("La distance de Hamming entre les deux chaine de caractères est :", distance)
            
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break