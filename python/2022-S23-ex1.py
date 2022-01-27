def max_dico(dico):
    max_like = 0
    for pseudo in dico:
        if dico[pseudo]>max_like:
            max_pseudo = pseudo
            max_like=dico[pseudo]
    return max_pseudo,max_like