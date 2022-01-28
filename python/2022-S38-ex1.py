def minimum(tab, i):
    ind_minimum = i
    for j in range(i+1, len(tab)):
        if tab[j] < tab[ind_minimum]:
            ind_minimum = j
    return ind_minimum

def echange(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def tri_selection(tab):
    for i in range(len(tab)):
        ind_minimum = minimum(tab, i)
        echange(tab, i, ind_minimum)
    return tab