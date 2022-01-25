def recherche(caractere,mot):
    occurrence = 0
    for c in mot:
        if c == caractere:
            occurrence += 1
    return occurrence
