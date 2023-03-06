from utilitary import *


def exo_5():
    """
    Script permettant de prendre une chaine de caractère et de supprime tous les caractères spéciaux
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        chaine = input("Entrer une chaine de caractères : ")
        caracteres_speciaux = "@!&?-_#;"
        chaine_sans_caracteres_speciaux = ""

        for caractere in chaine:
            if caractere not in caracteres_speciaux:
                chaine_sans_caracteres_speciaux += caractere
        
        print("La chaine sans caractères spéciaux : ", chaine_sans_caracteres_speciaux)
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break