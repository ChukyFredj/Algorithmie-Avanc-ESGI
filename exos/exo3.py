def exo_3():
    """
    Script permettant de compter le nombre de mots dans une chaine de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        chaine = input("Entrer une phrases : ")
        chaine_mot = chaine.split()

        print("Il y a :", len(chaine_mot), "mots dans la chaine")
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break