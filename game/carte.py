class Carte:
    def __init__(self, valeur, couleur):
        self._valeur = valeur  # La valeur de la carte (par exemple, 1, 2, '+2')
        self._couleur = couleur  # La couleur de la carte ('Rouge', 'Bleu', 'Vert', 'Jaune')

    @property
    def valeur(self):
        return self._valeur

    @property
    def couleur(self):
        return self._couleur

    def __str__(self):
        return f"{self._valeur}, {self._couleur}"