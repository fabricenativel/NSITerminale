def correspond(mot,mot_a_trous):
    for indice in range(len(mot)):
        if mot_a_trous[indice]!="*" and mot[indice]!=mot_a_trous[indice]:
            return False
    return True