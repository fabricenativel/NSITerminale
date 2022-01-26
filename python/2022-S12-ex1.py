def moyenne(tab):
    assert tab!=[], "erreur"
    somme = 0
    for valeur in tab:
        somme = somme + valeur
    return somme/len(tab)
