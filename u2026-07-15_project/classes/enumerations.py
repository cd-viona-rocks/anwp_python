from enum import Enum

class WorkingHours(Enum):
    """Enum for swimming center working hours (hh, mm, ss), 
    by default 06:00 AM to 22:00 PM, every day."""
    
    OPENING = (6, 0, 0),  # 6 AM
    CLOSING = (22, 0, 0)  # 10 PM


class TicketOptions(Enum):
    """Enum for ticket options available in the swimming center. 
    OPTION_NAME = (ID, price, deadline, description)
    
    SHORT_TERM: 3 hours ticket.
    LONG_TERM: Either morning, afternoon or evening ticket, up to 6 hours.
    DAY_PASS: Day pass ticket option.
    """

    SHORT_TERM = (0, 2.50, 3, "3 hours")
    LONG_TERM = (1, 4.00, 6, "Up to 6 hours")
    DAY_PASS = (2, 5.00, 0, "Day pass")
    

class Areas(Enum):
    """pair: name = value; from Type ENUM for permitted swimming areas."""

    ENTRANCE = (0, "Entrance area, bistro, tickets, info point.")
    CHILD = (1, "A safe area for children to play.")
    SWIMMING = (2, "The main swimming area with different lanes.")
    SAUNA = (3, "A relaxing sauna area.")