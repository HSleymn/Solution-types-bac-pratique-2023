def recherche(tab, elt):
    if len(tab) == 0:
        return 0
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
        
    return indice

print(recherche([2,3,4,5,6],5))
print(recherche([2,3,4,5,6],9))
print(recherche([5, 3], 1))

print(recherche([2, 4], 2))

print(recherche([2, 3, 5, 2, 4], 2))