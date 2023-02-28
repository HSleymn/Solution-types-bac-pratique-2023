import random
def lancer(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(1,6))
    return liste

def paire_6(tab):
    compteur = 0
    for j in range(len(tab)):
        if tab[j] == 6:
            compteur += 1
        if compteur >= 2 :
            return True
    return False


a = lancer(0)
print(a)
print(paire_6(a))