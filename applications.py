def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def compter_mots(phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if mot]
    return len(mots_filtres)

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

def est_palindrome(chaine):
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

def calculer_moyenne(liste):
    if not liste:
        return 0
    else:
        return sum(liste) / len(liste)  
