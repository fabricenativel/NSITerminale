def convertir(T):
    poids =  len(T)-1
    valeur = 0
    for elt in T:
        valeur += 2**poids * elt
        poids -=1
    return valeur
