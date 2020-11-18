def initooaliseGrille(grille):
    compteur = 0
    for compteur in range (0,9):
        grille[compteur] = " "
    return grille

def AfficheGrille(grille):
    for i in range (0,3):
        print(grille[3*i],grille[3*i+1],grille[3*i+2])
    return grille