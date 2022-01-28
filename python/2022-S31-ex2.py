def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = [] #(1)
    a_rendre = s_versee - s_due #(2)
    i = len(pieces) - 1
    while a_rendre > 0 : #(3)
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i]) #(4)
            a_rendre = a_rendre - pieces[i]
        else :
            i = i-1
    return rendu