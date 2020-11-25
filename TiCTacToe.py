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
        if (grille[3*i+j]!= "_":
            grille[3*i+j] = joueur
            choixIncorrect = False
    return grille

def testeVictoireVerticale(grille):
    compteur = 0
    while compteur < 3:
        if (grille[compteur] != "_":
            and grille[compteur] = grille[compteur + 3]
            and grille[compteur] = grille [compteur + 6])
            return True
    return False

def testeVictoireHorizontale(grille):
    compteur = 0
    while compteur < 3:
        if (grille[compteur] != "_":
            and grille[compteur*3] = grille[compteur*3+1]
            and grille[compteur*3] = grille[compteur*3+2])
            return True
    return False

def testeVictoireDiagonale(grille):
    if (grille[compteur]!= "_":
        and grille[4] = grille[0]
        and grille[4] = grille[8]
        return True
    return False
   
def testeJeuNul(gagnantTrouve,tour):
    if tour = 9 and gagantTrouve = False:
        return True
    return False

    

Tableau ["_","_","_","_","_","_","_","_"]
initialiseGrille(Tableau)
print(Tableau)
afficheGrille(Tableau)
print(Tableau)
ajouteSymbole(Tableau)
print(Tableau)
testeVictoireVerticale(Tableau)
testeVictoireHorizontale(Tableau)
testeVictoireDiagonale(Tableau)
testeJeuNul(Tableau)