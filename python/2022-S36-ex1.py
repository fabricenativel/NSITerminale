def recherche(elt,tab):
    for i in range(len(tab)-1,-1,-1):
        if elt==tab[i]:
            return i
    return len(tab)
