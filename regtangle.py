class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)
    def calculer_surface(self):
        return self.longueur * self.largeur