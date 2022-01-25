def conv_bin(n):
    liste_bit=[n%2]
    n=n//2
    while n!=0:
        liste_bit.append(n%2)
        n=n//2
    liste_bit.reverse()
    return liste_bit,len(liste_bit)