from utilitary import *



def exo_2():
    """
    Script permettant de rentrer une chaine de caractères 
    et si la chaine est triée par ordre croissant return vrai, sinon return faux
    """

    while True:
        
        chaine = input("Entrer une chaine de caractères : ")
        
        chaine_list = list(chaine)

        chaine_list_triee = sorted(chaine_list)

        if chaine_list == chaine_list_triee:
            print("La chaine est triée par ordre croissant")
        else:
            print("La chaine n'est pas triée par ordre croissant")

        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break


