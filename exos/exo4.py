from utilitary import *

def exo_4():
    """
    Script permettant de compter dans une chaine de caractères le nombre de majuscules et minuscules
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        chaine = input("Entrer une chaine de caractères : ")
        majuscules = 0
        minuscules = 0
        for lettres in chaine:
            if lettres.isupper():
                majuscules += 1
            elif lettres.islower():
                minuscules += 1
            else:
                pass
        print("Il y a :", majuscules, "majuscules et", minuscules, "minuscules dans la chaine")
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break