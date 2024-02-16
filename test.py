from applications import compter_mots, est_premier,somme_liste,est_palindrome,calculer_moyenne
from comptbancaire import CompteBancaire
from regtangle import Rectangle
def test_est_premier():
    assert est_premier(0) == False
    assert est_premier(1) == False
    assert est_premier(2) == True
    
def test_compter_mots():
    # Test avec une phrase vide
    assert compter_mots("") == 0

    # Test avec une phrase ne contenant que des espaces
    assert compter_mots("   ") == 0

    # Test avec une phrase contenant des espaces supplémentaires
    assert compter_mots("Bonjour    tout   le   monde") == 4

    # Test avec une phrase contenant un seul mot
    assert compter_mots("Hello") == 1

    # Test avec une phrase contenant des nombres
    assert compter_mots("123 456 789") == 3

def test_compte_bancaire():
    compte_bancaire = CompteBancaire(500)
    compte_bancaire.deposer(300)
    compte_bancaire.retirer(100)
    solde = compte_bancaire.obtenir_solde()
    assert solde == 700  
    
def test_somme_liste():
    liste=[1,2,3]
    assert somme_liste(liste)==6
    listepaire=[1.2,2,3]
    assert somme_liste(listepaire)==6.2

def test_rectangle():
    ractangle=Rectangle(5,10)
    ractangle.calculer_perimetre()==30
    ractangle.calculer_surface()==30

def test_est_palindrome():
    assert est_palindrome("") == True
    # Test avec une chaîne de caractères non palindrome
    assert est_palindrome("hello") == False
    # Test avec une chaîne de caractères palindrome
    assert est_palindrome("radar") == True
    # Test avec une chaîne de caractères palindrome avec des espaces
    assert est_palindrome("a man a plan a canal panama") == False
    assert est_palindrome("Able was I ere I saw Elba") == False

def test_calculer_moyenne():
    assert calculer_moyenne([]) == 0
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0
    assert calculer_moyenne([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5
    assert calculer_moyenne([10]) == 10.0
    assert calculer_moyenne([-1, -2, -3, -4, -5]) == -3.0



