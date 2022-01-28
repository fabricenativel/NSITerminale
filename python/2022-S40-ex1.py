def recherche(elt,tab):
    liste_indice=[]
    for i in range(len(tab)):
        if tab[i]==elt:
            liste_indice.append(i)
    return liste_indice