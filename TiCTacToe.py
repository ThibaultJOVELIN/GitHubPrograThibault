def initooaliseGrille(grille):
    compteur = 0
    for compteur in range (0,9):
        grille[compteur] = " "
    return grille

def afficheGrille(grille):
    for i in range (0,3):
        print(grille[3*i],grille[3*i+1],grille[3*i+2],'\n')
    return grille   

def ajouteSymbole(grille,joueur):
    i = 0
    j = 0
    choixIncorrect = True
    while choixIncorrect :
        i = int(input("Sur quelle ligne voulez vous jouer ?"))
        j = int(input("Sur quelle colonne voulez-vouz jouer ?"))
        if (grille[3*i+j]!= " "
            choixIncorrect = False
    return grille 