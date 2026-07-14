# test class Tickets
from datetime import datetime, timedelta

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
classes_path = project_root / "classes"
sys.path.insert(0, str(classes_path))

from enumerations import TicketOptions
from tickets import Ticket

create_at = datetime.now().timestamp()

# t0 = Ticket()

t1 = Ticket(TicketOptions.SHORT_TERM, create_at)
t2 = Ticket(TicketOptions.LONG_TERM, create_at)
t3 = Ticket(TicketOptions.DAY_PASS, create_at)

t4 = Ticket(TicketOptions.LONG_TERM, create_at, True)

Ticket.report()