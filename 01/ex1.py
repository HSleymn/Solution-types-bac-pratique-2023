def verifie(tab):
    max = tab[0]
    for i in range(1,len(tab)):
        if tab[i] < max:
            return False
        elif tab[i]>=max:
            pass
    return True



print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))