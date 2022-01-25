def maxi(tab):
    if tab==[]: return None,None
    indice_maxi,maxi = 0, tab[0]
    for indice in range(1,len(tab)):
        if tab[indice]>maxi:
            indice_maxi,maxi = indice,tab[indice]
    return maxi,indice_maxi
