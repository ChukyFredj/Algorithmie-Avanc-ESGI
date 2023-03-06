from exos import *
from utilitary import *


# Fonction de lancement du menu pour le choix des exercices disponibles
def menu():
    while True:
        print("\n\nListe des exercices de L'examen disponibles (Taper le numéro de l'exercice) :\n")
        print("Exercice 1 > Inverser les caractères d'une chaine de caractères")
        print("Exercice 2 > Chaine de caractères est-il triée par ordre croissant ? ")
        print("Exercice 3 > Nombre de mots")
        print("Exercice 4 > Compte nombre de majuscules et minuscules dans une chaine de caractères")
        print("Exercice 5 > Supprimer tous les caractères spéciaux d'une chaine de caractères")
        print("Exercice 6 > Répèter chaque caractère de la chaine de caractère N fois")
        print("Exercice 7 > Calcule la sommes des nombres entiers impairs jusqu'à X")
        print("Exercice 8 > Nombre paires de 1 à X")
        print("Exercice 9 > Est-ce que c'est un palindrome ? ")
        print("Exercice 10 > La distance de Hamming entre deux séquences de caractères")
        print("0 > Quitter\n")
        choice = verif_1error("Choisissez l'exercice voulu : ")
        print("\n\n\n")
        match choice:
            case 0:
                print("Très bien, au revoir...")
                return
            case 1:
                 exo_1()
            case 2:
                exo_2()
            case 3:
                exo_3()
            case 4:
                exo_4()
            case 5:
                exo_5()
            case 6:
                exo_6()
            case 7:
                exo_7()
            case 8:
                exo_8()
            case 9:
                exo_9()
            case 10:
                exo_10()
        if not choice_():
            print("Très bien, au revoir...")
            return
