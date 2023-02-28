def fusion(tab1, tab2):
    elt1 = tab1[0]
    elt2 = tab2[0]
    result = []
    compteur1=0
    compteur2=0
    taille = len(tab1) + len(tab2)
    for i in range(taille) :
        
        
         
        try:
            if tab1[compteur1] < tab2[compteur2]:
                result.append(tab1[compteur1])
                compteur1 +=1

            elif tab1[compteur1] > tab2[compteur2]:
                result.append(tab2[compteur2])
                compteur2 +=1

            elif tab1[compteur1] == tab2[compteur2]:
                result.append(tab2[compteur2])
                result.append(tab1[compteur1])
                compteur1 += 1
                compteur2 +=1

        except IndexError:
            if compteur2 == len(tab2):
                for i in range(compteur1,len(tab1)):
                    result.append(tab1[i])
                return result
            if compteur1 == len(tab1) :
                for i in range(compteur2,len(tab2)):
                    result.append(tab2[i])
                return result
print(fusion([3, 4,19], [-3,-1, 5, 10,87]))
a = fusion([3, 5], [2, 5])
print(fusion([4], [2, 6]))
fusion([3, 5], [2, 5])
print(fusion([3, 5], [2, 5]))
