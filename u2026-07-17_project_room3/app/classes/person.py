from typing import Any, Dict


class Person:
    """Basisklasse für Personenobjekte."""
    PERMITTED_ATTR = ["name", "strasse", "hausnummer", "plz", "telefon", "id"]
    ERROR_ATTR = f"Die Attributen müssen genau die folgenden sein: {', '.join([a for a in PERMITTED_ATTR])}"

    def __new__(cls, *args: Any, **kwargs: Any) -> "Person":
        """Erstellt eine neue Instanz der Klasse oder einer Unterklasse.

        Args:
            *args: Positionale Argumente für die Initialisierung.
            **kwargs: Schlüsselwortargumente für die Initialisierung.

        Returns:
            Person: Neue Instanz der Klasse.
        """
        if cls is Person:
            raise TypeError("Can't instantiate abstract class directly.")
        return super().__new__(cls)

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert Attribute über Schlüsselwortargumente.

        Args:
            **kwargs: Attribute und deren Werte.

            **USE THE FOLLOWING MASK FOR KWARGS**
            name: str
            strasse: str
            hausnummer: str
            plz: str
            telefon: str (use +COUNTRY PREFIX NUMBER)
            id: str
        """
        if len(kwargs.keys()) != 6:
            raise ValueError()
        for key, value in kwargs.items():
            if key not in Person.PERMITTED_ATTR:
                raise ValueError(Person.ERROR_ATTR)
            setattr(self, key, value)


    def set_attribute(self, key: str, value: Any) -> None:
        """Setzt ein beliebiges Attribut auf der Instanz.

        Args:
            key: Name des Attributs.
            value: Wert des Attributs.
        """
        attr_for_set = Person.PERMITTED_ATTR
        attr_for_set.remove("id")
        err_msg = f"Falsche Eingabe von Attributen. Es muss einer von"
        err_msg += f" {', '.join([a for a  in Person.attr_for_set])} sein."
        if key not in Person.attr_for_set:
            raise ValueError(err_msg)
        setattr(self, key, value)


    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Gibt den Wert eines Attributes zurück.

        Args:
            key: Name des Attributs.
            default: Standardwert, falls das Attribut nicht existiert.

        Returns:
            Any: Wert des Attributes oder der Default-Wert.
        """
        err_msg = f"Falsche Eingabe von Attributen. Es muss einer von "
        err_msg += f"{', '.join([a for a  in Person.PERMITTED_ATTR])} sein."
        if key not in Person.PERMITTED_ATTR:
            raise ValueError(err_msg)
        return getattr(self, key, default)
