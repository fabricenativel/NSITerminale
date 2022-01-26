def maxi(tab):
    indice_maximum, maximum = 0,tab[0]
    for indice in range(len(tab)):
        if tab[indice]>maximum:
            indice_maximum,maximum = indice, tab[indice]
    return maximum, indice_maximum