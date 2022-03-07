alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def occurrence_max(ch):
    occurrence = [0]*26
    for caractere in ch:
        if caractere in alphabet:
            index_caractere = alphabet.index(caractere)
            occurrence[index_caractere] += 1
    indice_max_occurence = 0
    max_occurence = occurrence[0]
    for i in range(0,len(occurrence)):
        if occurrence[i]>max_occurence:
            max_occurence = occurrence[i]
            indice_max_occurence = i 
    return alphabet[indice_max_occurence]