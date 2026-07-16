from datetime import datetime, timedelta

from classes.enumerations import WorkingHours, TicketOptions
from classes.logs import TICKETS


class Ticket:
    """Represent a ticket for the swimming center.

    The ticket will be created for the automatic machine and can be
    assigned (attached) to a client.
    """

    def __init__(
        self,
        ticket_type: TicketOptions = None,
        created_at: int = 0,
        allows_sauna: bool = False,
        automatic: int = None,
        client: int = None,
    ):
        """Initialize a ticket instance.

        Args:
            ticket_type: The ticket option from :class:`TicketOptions`.
            created_at: Unix timestamp for the ticket creation time.
            allows_sauna: Whether the ticket includes sauna access.
            automatic: Identifier of the automatic that created the ticket.
            client: Identifier of the client associated with the ticket.

        Raises:
            ValueError: If the ticket type is not valid.
        """

        if ticket_type not in TicketOptions:
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
        if allows_sauna:
            self.include_sauna()

        self.log_ticket()

    def set_automatic(self, n: int):
        """Assign the automatic machine associated with the ticket.

        Args:
            n: The identifier of the automatic.
        """
        self.automatic = n

    def set_deadline(self):
        """Calculate and store the ticket deadline.

        The deadline depends on the ticket type:
        - DAY_PASS: the deadline is the configured closing time of the day.
        - SHORT_TERM and LONG_TERM: the deadline is the configured duration
          or the closing time, whichever comes first.
        """

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
            raise ValueError(
                f"Invalid ticket type. Must be one {[o.name for o in TicketOptions]}"
            )

    def include_sauna(self):
        """Add sauna access to the ticket and increase the price."""
        self.price += 1.5
        self.sauna = True

    def log_ticket(self):
        """Store the ticket in the ticket registry."""
        TICKETS[self.ticket_number] = self
        # print(TICKETS)

    @classmethod
    def report(self):
        """Print a summary of all created tickets."""
        print(f"\n\ntotal of tickets created: {len(TICKETS)}")
        print(" - - - -\nReport\n - - - -")
        for t in TICKETS.values():
            print(t)

    def __str__(self):
        """Return a readable string representation of the ticket."""
        return f"Ticket(type={self.ticket_type}, number={self.ticket_number}, sauna={self.sauna}, price={self.price}, deadline={self.deadline}, automatic={self.automatic}, client={self.client})"
    
