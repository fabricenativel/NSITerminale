def xor(a,b):
    resultat = []
    for i in range(len(a)):
        if a[i]==b[i]:
            resultat.append(0)
        else:
            resultat.append(1)
    return resultat