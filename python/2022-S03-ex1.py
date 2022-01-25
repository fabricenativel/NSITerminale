def delta(liste):
    codage=[liste[0]]
    for i in range(1,len(liste)):
        codage.append(liste[i]-liste[i-1])
    return codage
