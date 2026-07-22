from typing import List
from typing import Any, Dict

from classes.pizza import Pizza
from classes.kunde import Kunde

class Bestellung:
    PERMITTED_ATTR = ["bestellnummer", "pizzen", "datum", "status"]
    ERROR_ATTR = f"Die Attributen müssen genau die folgenden sein: {', '.join([a for a in PERMITTED_ATTR])}"

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert Attribute über Schlüsselwortargumente.

        Args:
            **kwargs: Attribute und deren Werte.

            **USE THE FOLLOWING MASK FOR KWARGS**
            bestellnummer: str
            pizzen: str
            datum: str
            status: str
        """
        if len(kwargs.keys()) != 6:
            raise ValueError()
        for key, value in kwargs.items():
            if key not in Bestellung.PERMITTED_ATTR:
                raise ValueError(Bestellung.ERROR_ATTR)
            setattr(self, key, value)
            

    # + pizzaGesamtanzahl(pizzen : Pizzen) : integer
    def pizzaGesamtanzahl(self) -> int:
        pass

    # + pizzaHinzufügen(pizza : Pizza) : void
    def pizzaHinzufügen(self, pizza: Pizza) -> None:
        pass

    # + getStatus() : string
    def getStatus(self) -> str:
        pass

    # + getKunde() : Kunde
    def getKunde(self) -> Kunde:
        pass

    # + setStatus(neuerStatus : string) : void
    def setStatus(self, neuerStatus: str) -> None:
        pass

    # + berechneGesamtpreis() : double
    # 'float' is the Python equivalent for 'double'
    def berechneGesamtpreis(self) -> float:
        pass