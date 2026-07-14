# test class Tickets
from datetime import datetime, timedelta

from enumerations import TicketOptions
from tickets import Ticket

from logs import TICKETS

create_at = datetime.now().timestamp()

# t0 = Ticket()

t1 = Ticket(TicketOptions.SHORT_TERM, create_at)
t2 = Ticket(TicketOptions.LONG_TERM, create_at)
t3 = Ticket(TicketOptions.DAY_PASS, create_at)

t4 = Ticket(TicketOptions.LONG_TERM, create_at, True)

Ticket.report()