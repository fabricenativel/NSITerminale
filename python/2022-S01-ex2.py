Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution #(1)
    p = Pieces[i]
    if p <= arendre : #(2)
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1) #(3)
