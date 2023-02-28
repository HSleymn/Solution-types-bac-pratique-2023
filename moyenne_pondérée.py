def moyenne(tab):
    if len(tab) == 0:
        return 0
    denominateur = 0
    numerateur = 0 
    for i in range(len(tab)):
        denominateur += tab[i][1]
        numerateur += tab[i][0] * tab[i][1]
    return numerateur / denominateur

print(moyenne([(15,2),(9,1),(12,3)]))
print(moyenne([]))