def maxliste(liste):
    maxi = liste[0]
    for elt in liste:
        if elt > maxi:
            maxi=elt
    return maxi