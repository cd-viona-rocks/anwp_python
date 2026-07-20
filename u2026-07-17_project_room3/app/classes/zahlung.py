from typing import Any, Dict


class Zahlung:
    PERMITTED_ATTR = ["zahlungId", "betrag", "zahlungsart", "status"]
    ERROR_ATTR = f"Die Attributen müssen genau die folgenden sein: {', '.join([a for a in PERMITTED_ATTR])}"

    def __init__(self, **kwargs: Any) -> None:
        """Initialisiert Attribute über Schlüsselwortargumente.

        Args:
            **kwargs: Attribute und deren Werte.

            **USE THE FOLLOWING PERMITTED ARGS FOR KWARGS**
            zahlungsId: str
            betrag: float
            zahlungsart: str
            status: str
        """
        if len(kwargs.keys()) != 6:
            raise ValueError()
        for key, value in kwargs.items():
            if key not in Zahlung.PERMITTED_ATTR:
                raise ValueError(Zahlung.ERROR_ATTR)
            setattr(self, key, value)

    
    # + zahlungAusfuehren() : void
    def zahlungAusfuehren(self) -> None:
        pass

    # + getStatus() : string
    def getStatus(self) -> str:
        pass