def separe(tab):
    i = 0
    j = len(tab)-1 #(1)
    while i < j :
        if tab[i] == 0 :
            i = i + 1 #(2)
        else :
            tab[i], tab[j] = tab[j],tab[i] #(3)
            j = j-1
    return tab