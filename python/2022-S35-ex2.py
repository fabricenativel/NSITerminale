def dichotomie(tab, x):
    """
        tab : tableau trie dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab==[]: #(1)
        return False,1

    # cas ou x n'est pas compris entre les valeurs extremes
    if (x < tab[0]) or (x>tab[len(tab)-1]):
        return False,2 #(2)
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 #(3)
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1 
    return False,3 #(4)
