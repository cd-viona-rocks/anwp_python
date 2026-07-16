
from datetime import datetime

from classes.tickets import Ticket
from classes.enumerations import WorkingHours, TicketOptions

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

    def give_change(self, price: float, money: float) -> dict:
        to_give_back = {}
        change = 0.0
        if price > money:
            raise ValueError("not enough money. operation canceled")
        elif price == money:
            pass
        else:
            change = money - price
            in_cash = sorted(self.cash.keys()) # [1,2,5,..,500]
            if change < min(in_cash):
                # it occurs if "change to give back" < "the smallste bill possible available"
                raise ValueError("change not possible due not enough bills. operation canceled.")
            else:
                rest = change
                while rest > 0:
                    if rest < 0:
                        raise ValueError("not possible to give change. please use other bills.")
                    bill = max(list(filter(lambda x: x <= rest, in_cash)))
                    q = rest // bill
                    rest -= bill * q
                    if self.cash[bill] - q >= 0:
                        to_give_back[bill] = q
                        self.cash[bill] -= q
                    else:
                        to_give_back[bill] = self.cash[bill]
                        rest -= bill * self.cash[bill]
                        self.cash[bill] = 0
                        in_cash.remove(bill)

        return to_give_back


    def sell(self, 
            option: TicketOptions, 
            cash: dict, 
            hasSubscription: bool = False, 
            create_at: int = 0,
            allowSauna: bool = False,
            client: int = None
        ) -> dict:
        """Simulate a ticket sale for one supported area option."""
        if option not in TicketOptions:
            return f"Invalid option: {option}"

        if hasSubscription:
            # Free ticket for subscription holders
            option = TicketOptions.DAY_PASS
            change = cash
        else:
            # DONE: cash as dict; money is the total of cash (float). when pay, add bills -> update cash.
            for k,v in cash.items():
                self.cash[k] += v
            change = self.give_change(option.value[1], sum([k*v for k,v in cash.items()]))

            # - - replaced by the logic give_change - - 
            # if money < option.value[1]:
            #     return "Please insert more money. The operation will be canceled."
        
        return {
            "ticket": Ticket(option, create_at, allowSauna, self.number, client) ,
            "change": change
        }
    
    def get_cash(self):
        return self.cash
    
    def report_cash(self):
        total = 0
        report = "\n - - - -\nReport Cash\n - - - - \n"
        for k, v in self.cash.items():
            tt = k * v
            total += tt
            report += f"from {v:4d} of {k:6.2f}, total of {tt:8.2f}\n"
        print(report)
        print(f"total amount in cash of {total}\n - - - -\n")


    def __str__(self) -> str:
        """Return a readable representation of the automatic."""
        return f"Automatic(number={self.number})"
    