def recherche(tab,elt):
    ind_debut = 0
    ind_fin = len(tab)-1
    while ind_fin > ind_debut:
        ind_milieu = (ind_fin+ind_debut)//2
        if tab[ind_milieu]==elt:
            return ind_milieu
        elif tab[ind_milieu]>elt:
            ind_fin=ind_milieu-1
        else:
            ind_debut=ind_milieu+1
    return -1