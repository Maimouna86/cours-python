from Vehicule import Vehicule


class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int):
        super().__init__(marque, modele, annee)
        self.nombre_portes: int = nombre_portes

    # GETTERS / SETTERS

    @property
    def nombre_portes(self) -> int:
        return self.__nombre_portes

    @nombre_portes.setter
    def nombre_portes(self, valeur) -> None:
        self.__nombre_portes = valeur if valeur > 2 else 2

    # METHODES

    def klaxonner(self) -> str:
        return f"{self.marque} {self.modele} klaxonne."
