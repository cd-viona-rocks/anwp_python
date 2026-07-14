
from datetime import datetime
from tickets import Ticket

from enumerations import WorkingHours, TicketOptions

class Automatic:
    """Represents a ticket vending machine for the swimming center.

    This class models aggregation: the machine can exist independently of a
    swimming center and may be attached or removed without owning the center's
    lifecycle.
    """
    Serial = []

    def __init__(self, number: int, cash: dict):
        """Create an Automatic instance.

        Args:
            number: The machine number.
            cash: a dictionary of notes and coins by value

        Raises:
            ValueError: If the machine number already exists or is not an integer.
        """
        if not isinstance(number, int):
            raise ValueError("Automatic number must be an integer.")

        if number in Automatic.Serial:
            raise ValueError(f"Automatic number {number} already exists.")

        self.number = number
        self.cash = cash
        Automatic.Serial.append(number)

    def give_change(self, price: float, money:float) -> float:
        if price > money:
            raise ValueError("not enough money. operation canceled")
        elif price == money:
            return 0.0
        else:
            change = money - price
            in_cash = sorted(self.cash.keys())
            if change < min(in_cash):
                raise ValueError("change not possible due not enough bills. operation canceled.")
            else:
                # TODO - do it better ! ! !
                return change
            


    def sell(self, 
            option: TicketOptions, 
            money: float, 
            hasSubscription: bool = False, 
            create_at: int = 0,
            allowSauna: bool = False,
            client: int = None
        ) -> Ticket:
        """Simulate a ticket sale for one supported area option."""
        if option not in TicketOptions:
            return f"Invalid option: {option}"

        # - - replaced by the logic give_change - - 
        # if money < option.value[1]:
        #     return "Please insert more money. The operation will be canceled."
        
        change = self.give_change(option.value[1], money)

        # Free ticket for subscription holders
        if hasSubscription:
            ticket = Ticket(option.DAY_PASS, create_at, allowSauna, self.number, client)
        else:
            ticket = Ticket(option, create_at, allowSauna, self.number, client)        

        return ticket

    def __str__(self) -> str:
        """Return a readable representation of the automatic."""
        return f"Automatic(number={self.number})"
    