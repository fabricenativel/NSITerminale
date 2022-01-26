def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result #(1)
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse==chaine #(2)
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre) #(3)
    return est_palindrome(chaine)