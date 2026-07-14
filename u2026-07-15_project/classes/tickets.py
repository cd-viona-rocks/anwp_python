from datetime import datetime, timedelta
from enumerations import WorkingHours, TicketOptions
from logs import TICKETS


class Ticket:
    """Represents a ticket for the swimming center.

    This class models aggregation: the ticket can exist independently of a
    swimming center and may be attached or removed without owning the center's
    lifecycle.
    """

    def __init__(self, 
            ticket_type: TicketOptions = None, 
            created_at: int = 0, 
            allows_sauna: bool = False,
            automatic: int = None,
            client: int = None
        ):
        """Create a Ticket instance.

        Args:
            ticket_type: The type of the ticket (e.g., "ENTRANCE", "CHILD").
            price: The price of the ticket.
            dealine: The deadline for the ticket in unix timestamp (optional).
        """

        if ticket_type == None: 
            raise ValueError("Ticket type must be one of TicketOptions")

        self.ticket_number = id(self)  # Unique identifier for the ticket
        self.ticket_type = ticket_type.name
        self.ticket_code = ticket_type.value[0]
        self.description = ticket_type.value[3]
        self.price = ticket_type.value[1]
        self.sauna = False
        self.created_at = created_at
        self.deadline = None
        self.automatic = automatic
        self.client = client
        
        self.set_deadline()
        if allows_sauna: self.include_sauna()

        self.log_ticket()

    def set_automatic(self, n: int):
        self.automatic = n

    def set_deadline(self):
        """Set the creation time for the ticket. sets automatically deadline."""

        created_dt = datetime.fromtimestamp(self.created_at)
        closing_dt = created_dt.replace(
                hour=WorkingHours.CLOSING.value[0],
                minute=WorkingHours.CLOSING.value[1],
                second=WorkingHours.CLOSING.value[2],
                microsecond=0,
            )
        
        # DAY_PASS: deadline is the closing time on the same day
        if self.ticket_type == "DAY_PASS":            
            self.deadline = int(closing_dt.timestamp())
        # SHORT_TERM / LONG_TERM: period ends after a duration (hours) defined
        elif self.ticket_type in ("SHORT_TERM", "LONG_TERM"):
            hours = TicketOptions[self.ticket_type].value[2]
            period_ends = created_dt + timedelta(hours=hours)
            if period_ends > closing_dt:
                period_ends = closing_dt
            self.deadline = int(period_ends.timestamp())
        else:
            raise ValueError(f"Invalid ticket type. Must be one {[o.name for o in TicketOptions]}")

    def include_sauna(self):
        self.price += 1.5
        self.sauna = True

    def log_ticket(self):
        """Log the ticket information to the database."""
        TICKETS[self.ticket_number] = self
        # print(TICKETS)

    @classmethod
    def report(self):
        print(f"\n\ntotal of tickets created: {len(TICKETS)}")
        print(" - - - -\nReport\n - - - -")
        for t in TICKETS.values():
            print(t)

    def __str__(self):
        return f"Ticket(type={self.ticket_type}, number={self.ticket_number}, sauna={self.sauna}, price={self.price}, deadline={self.deadline}, automatic={self.automatic}, client={self.client})"
    
