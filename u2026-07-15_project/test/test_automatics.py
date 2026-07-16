from datetime import datetime, timedelta

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
classes_path = project_root / "classes"
sys.path.insert(0, str(classes_path))

from enumerations import TicketOptions
from tickets import Ticket

from automatics import Automatic

a1 = Automatic(
        number=1001,
        cash={
            0.5: 200,
            1: 100,
            2: 100,
            5: 100,
            10: 50,
            50: 10,
        }
    )

print(a1)
a1.report_cash()

# returns error -> ok!
# a1.give_change(5,1)

# returns 0.0 -> ok!
# back = a1.give_change(5,5)

# returns 1: 1 -> ok! (one bill of 1.00)
# back = a1.give_change(5,6)

# returns 5: 1 -> ok! (one bill of 5.00)
# back = a1.give_change(5,10)

# returns  {10: 4, 5: 1 }- ok! (4x bill of 10 + 1x bill of 5)
back = a1.give_change(5,50)

print(f"back {back}")
a1.report_cash()