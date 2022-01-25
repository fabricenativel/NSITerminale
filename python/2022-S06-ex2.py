def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0 #(1)
    trouve = False
    while i < n-g and trouve == False : #(2)
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1 #(3)
        if j == g:
            trouve = True
        i+=1 #(4)
    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))
print(recherche("AGTC", "GTACAAATCTTGCC"))