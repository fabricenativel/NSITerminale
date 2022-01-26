def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1 #(1)
    while i != j :
        if tab[i]== 0:
            i = i + 1 #(2) 
        else :
            valeur = tab[j]
            tab[j] = tab[i] #(3)
            tab[i] = valeur
            j= j-1 #(4)
    return tab