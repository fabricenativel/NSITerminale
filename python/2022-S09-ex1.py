def calcul(k):
  resultat=[k]
  while k!=1:
    if k%2==0: 
      k=k//2
    else:
      k=3*k+1
    resultat.append(k)
  return resultat

print(calcul(7))
  
