from typing import Any, Dict
from random import choice

from classes.person import Person
from classes.bestellung import Bestellung

class Lieferant(Person):
    """Repräsentiert einen Lieferant aus der Klasse Person."""

    PERMITTED_ATTR = [*Person.PERMITTED_ATTR, "fahrzeugKlasse", "city"]

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert einen Kunden.

        Args:
            **kwargs: Attribute für Person und die Lieferantinformationen.
        """
        person_args: Dict[str, Any] = {}
        for key in Person.PERMITTED_ATTR:
            if key in kwargs:
                person_args[key] = kwargs[key]

        super().__init__(**person_args)
        # self.fahrzeugKlasse: str = kwargs.get("vehicle_type", "")
        self.vehicle: str = choice(["Auto", "Truck", "Bicicle", "Motocicle"])
        self.city: str = kwargs.get("city", "")

        # get vehicle from choice(["Auto", "Truck", "Bicicle", "Motocicle"])
        # get standort from city

    # + lieferadresseAnzeigen(bestellung : Bestellung) : string
    def lieferadresseAnzeigen(self, bestellung: Bestellung) -> str:
        pass

    # + setBestellstatus(bestellung : Bestellung, neuerBestellstatus : string) : void
    def setBestellstatus(self, bestellung: Bestellung, neuerBestellstatus: str) -> None:
        pass