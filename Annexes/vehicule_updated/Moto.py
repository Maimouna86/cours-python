from Vehicule import Vehicule


class Moto(Vehicule):
    def __init__(self, marque: str, modele: str, annee: int, cylindree: int):
        super().__init__(marque, modele, annee)
        self.cylindree: int = cylindree

    # GETTERS / SETTERS

    @property
    def cylindree(self) -> int:
        return self.__cylindree

    @cylindree.setter
    def cylindree(self, valeur) -> None:
        self.__cylindree = valeur

    # METHODES

    def accelerer(self) -> str:
        self.vitesse += 30
        return f"{self.marque} {self.modele} accélère à {self.vitesse} km/h."

    def faire_des_acrobaties(self) -> str:
        return f"{self.marque} {self.modele} fait des acrobaties."
