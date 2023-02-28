def indices_maxi(tab):
    max= tab[0]
    indice = [0]
    for i in range(1,len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice = []
            indice.append(i)
        elif tab[i] == max:
            indice.append(i)

    return (max, indice)

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))