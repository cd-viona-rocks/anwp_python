from typing import Any, Dict

from classes.person import Person
from classes.bestellung import Bestellung

class Mitarbeiter(Person):
    """Repräsentiert einen Mitarbeiter aus der Klasse Person."""

    PERMITTED_ATTR = [*Person.PERMITTED_ATTR, "employee_number"]

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert einen Kunden.

        Args:
            **kwargs: Attribute für Person und die Mitarbeiternummer.
        """
        person_args: Dict[str, Any] = {}
        for key in Person.PERMITTED_ATTR:
            if key in kwargs:
                person_args[key] = kwargs[key]

        super().__init__(**person_args)
        self.mitarbeiternummer: str = kwargs.get("employee_number", "")

    # + bestellungBestätigen(bestellung : Bestellung) : void
    def bestellungBestaetigen(self, bestellung: Bestellung) -> None:
        pass

    # + bestellungZuweisen(bestellung : Bestellung, mitarbeiter : Mitarbeiter) : void
    # Note: Using 'Mitarbeiter' as a type hint inside its own class works 
    # out of the box in Python.
    def bestellungZuweisen(self, bestellung: Bestellung, mitarbeiter: 'Mitarbeiter') -> None:
        pass

    # + setBestellstatus(bestellung : Bestellung, neuerBestellstatus : string) : void
    def setBestellstatus(self, bestellung: Bestellung, neuerBestellstatus: str) -> None:
        pass