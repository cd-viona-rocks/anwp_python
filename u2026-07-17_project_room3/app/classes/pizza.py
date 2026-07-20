class Pizza:
    PERMITTED_ATTR = ["pizzaId", "name", "groesse", "preis"]
    ERROR_ATTR = f"Die Attributen müssen genau die folgenden sein: {', '.join([a for a in PERMITTED_ATTR])}"

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert Attribute über Schlüsselwortargumente.

        Args:
            **kwargs: Attribute und deren Werte.

            **USE THE FOLLOWING MASK FOR KWARGS**
            pizzaId: str
            name: str
            groesse: str
            preis: float
        """
        if len(kwargs.keys()) != 4:
            raise ValueError()
        for key, value in kwargs.items():
            if key not in Pizza.PERMITTED_ATTR:
                raise ValueError(Pizza.ERROR_ATTR)
            setattr(self, key, value)


    def getName(self) -> str:
        return self.name

    def getPreis(self) -> float:
        return self.preis