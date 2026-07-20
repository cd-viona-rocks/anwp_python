from typing import Any, Dict

from person import Person
from pizza import Pizza


class Kunde(Person):
    """Repräsentiert einen Kunden aus der Klasse Person."""

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert einen Kunden.

        Args:
            **kwargs: Attribute für Person und die Kundennummer.
        """
        person_args: Dict[str, Any] = {}
        for key in Person.PERMITTED_ATTR:
            if key in kwargs:
                person_args[key] = kwargs[key]

        super().__init__(**person_args)
        self.kundennummer: str = kwargs.get("kundennummer", "")

    # + auswahlPizza() : void
    def auswahlPizza(self) -> None:
        pass

    # + bestellungAufgeben(pizzen : Pizza[ ]) : void
    # 'List[Pizza]' bildet das UML-Array 'Pizza[ ]' exakt ab
    def bestellungAufgeben(self, pizzen: list[Pizza]) -> None:
        pass

    # + bestellungStornieren() : void
    def bestellungStornieren(self) -> None:
        pass

    # + zahlungDurchführen() : void
    def zahlungDurchführen(self) -> None:
        pass

    # + bestellstatusEinsehen() : void
    def bestellstatusEinsehen(self) -> None:
        pass

    # + bewerten(sterne(1-5) : double) : void
    # 'float' ist in Python das Äquivalent zu 'double'
    def bewerten(self, sterne: float) -> None:
        pass