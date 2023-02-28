def voisinage(n, ligne, colonne):

    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(5, 5, 5 )
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1 

def genere_grille(bombes):
    
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] =    -1 # place la bombe
        incremente_voisins(bombes, 5, 5) # incrémente ses voisins
    return grille


print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))