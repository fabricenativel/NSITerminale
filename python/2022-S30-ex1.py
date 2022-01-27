def fusion(tab1,tab2):
    i1,i2 = 0,0
    tab = []
    while i1<len(tab1) and i2<len(tab2):
        if tab1[i1]<tab2[i2]:
            tab.append(tab1[i1])
            i1 += 1
        else:
            tab.append(tab2[i2])
            i2 += 1
    tab = tab + tab1[i1:] + tab2[i2:]
    return tab


    
        