def multiplication(a,b):
    produit=0
    for i in range(abs(a)):
        produit += abs(b)
    if (a>0 and b<0) or (a<0 and b>0): 
        return -produit
    else:
        return produit