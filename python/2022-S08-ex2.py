def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a) 
    i = len(tab)-1 #(1)
    while a < l[i] and i >= 0:  #(2)
      l[i+1] = l[i] #(3)
      l[i] = a
      i = i - 1 #(4)
    return l