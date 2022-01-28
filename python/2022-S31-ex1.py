def recherche(a,t):
    nb_occurence = 0
    for elt in t:
        if elt==a:
            nb_occurence +=1
    return nb_occurence