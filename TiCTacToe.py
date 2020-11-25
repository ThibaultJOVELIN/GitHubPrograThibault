def initialiseGrille(grille):
    compteur = 0
    for compteur in range (0,9):
        grille[compteur] = "_"
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

def testeVictoireVerticale (grille,joueur)
    compteur = 0
    while compteur > 3:
        if (grille[compteur] != "_"
            and grille[compteur] = grille[compteur + 3]
            and grille[compteur] = grille [compteur + 6]


Tableau 1","2","3","4","5","6","7","8"]
initialiseGrille(Tableau)
print(Tableau)
rvbuffdgfdfdgdvv