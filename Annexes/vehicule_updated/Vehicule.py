from abc import ABC


class Vehicule(ABC):
    """Classe abstraite représentant un véhicule.

    Attributs:
        nombre_instance (int): nombre d'instance de la classe.
        marque (str): marque du vehicule.
        modele (str): modèle du vehicule.
        annee (int): année du vehicule.
        vitesse (int): vitesse du véhicule.
    """
    nombre_instance: int = 0  # Propriété statique de la classe

    def __init__(self, marque: str, modele: str, annee: int):
        self.marque: str = marque
        self.modele: str = modele
        self.annee: int = annee
        self.vitesse: int = 0
        Vehicule.nombre_instance += 1  # nombre_instance appartient à User, pas à self

    def __del__(self) -> None:
        print(f"Objet {self.__class__.__name__} est détruit.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} de marque {self.marque}, de modèle {self.modele}, fabriqué en {self.annee}, roule à {self.vitesse} km/h"

    def __repr__(self) -> str:
        return f"Représentation technique de {self.__str__()}"

    # GETTERS / SETTERS

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, valeur) -> None:
        self._marque = valeur

    @property
    def modele(self) -> str:
        return self._modele

    @modele.setter
    def modele(self, valeur) -> None:
        self._modele = valeur

    @property
    def annee(self) -> int:
        return self._annee

    @annee.setter
    def annee(self, valeur) -> None:
        self._annee = valeur

    @property
    def vitesse(self) -> int:
        return self._vitesse

    @vitesse.setter
    def vitesse(self, valeur) -> None:
        self._vitesse = valeur

    # METHODE DE CLASSE

    @staticmethod
    def get_instance_count() -> int:
        return f"Le nombre d'instance est {Vehicule.nombre_instance}"

    # METHODES

    def demarrer(self) -> str:
        return f"{self.marque} {self.modele} démarre."

    def accelerer(self) -> str:
        self.vitesse += 10
        return f"{self.marque} {self.modele} accélère à {self.vitesse} km/h."

    def arreter(self) -> str:
        self.vitesse = 0
        return f"{self.marque} {self.modele} s'arrête."
