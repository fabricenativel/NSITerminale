def RechercheMinMax(tab):
    if tab==[]:
        return {'min':None,'max':None}
    mini,maxi = tab[0],tab[0]
    for elt in tab:
        if elt<mini: mini=elt
        if elt>maxi: maxi=elt
    return {'min' : mini, 'max' : maxi}