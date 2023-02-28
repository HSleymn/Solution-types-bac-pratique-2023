ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def position_alphabet(lettre):
    for i in range(len(ALPHABET)):
        if ALPHABET[i] == lettre:
            return int(i)

        else:
            pass


def cesar( decalage,message=""):
    if type(message) != str or type(decalage) != int:
        return "Veuillez vérifier les types de vos entrées. "
    mes_chiff = ""
    for carac in range(len(message)):
        if message[carac].lower() in ALPHABET:
            position = position_alphabet(message[carac].lower()) + decalage
            mes_chiff += ALPHABET[position]
        else:
            mes_chiff += message[carac]
    return mes_chiff

print( cesar(10, "je m'appelle Jean Michel"))