from utilitary import *

def mod(a,b):
    return a%b

def exo_6():
    """
    Script permettant de répéter chaque caractère de la chaine de caractère N fois
    """

    while True:
        
        chaine = input("Entrer une chaine de caractères : ")
        n = int(input("Entrer le nombre de fois que vous voulez répéter : "))
        chaine_rep = ""

        for lettre in chaine:
            chaine_rep += lettre*n
        print(chaine_rep)
    
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break