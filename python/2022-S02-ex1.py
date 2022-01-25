def moyenne(donnees):
    somme_notes = 0
    somme_coefficients = 0
    for d in donnees:
        note = d[0]
        coefficient = d[1]
        somme_notes += note*coefficient
        somme_coefficients += coefficient
    return somme_notes/somme_coefficients

