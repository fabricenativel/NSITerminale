def nb_repetitions(elt,tab):
    nb_rep = 0
    for x in tab:
        if x==elt:
            nb_rep += 1
    return nb_rep