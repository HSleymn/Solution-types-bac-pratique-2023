def recherche(tab, elt):
    if len(tab) == 0:
        return 0
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    else:
        return -1

print(recherche([2,3,4,5,6],5))
print(recherche([2,3,4,5,6],9))