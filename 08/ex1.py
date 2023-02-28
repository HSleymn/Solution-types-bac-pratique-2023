a =  {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}

def max_dico(dico): 
    name = ""
    like_max = 0
    for i in dico.items():
        if i[1] > like_max:
            like_max = i[1]
            name = i[0]
    return (name, like_max)



print(max_dico(a))

print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))