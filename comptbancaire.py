class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
    def obtenir_solde(self):
        return self.solde