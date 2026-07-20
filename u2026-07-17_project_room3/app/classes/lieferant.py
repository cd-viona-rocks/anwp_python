from typing import Any, Dict

from person import Person
from bestellung import Bestellung

class Lieferant(Person):
    """Repräsentiert einen Lieferant aus der Klasse Person."""

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
        self.fahrzeugKlasse: str = kwargs.get("fahrzeugKlasse", "")
        self.standort: str = kwargs.get("standort", "")

    # + lieferadresseAnzeigen(bestellung : Bestellung) : string
    def lieferadresseAnzeigen(self, bestellung: Bestellung) -> str:
        pass

    # + setBestellstatus(bestellung : Bestellung, neuerBestellstatus : string) : void
    def setBestellstatus(self, bestellung: Bestellung, neuerBestellstatus: str) -> None:
        pass