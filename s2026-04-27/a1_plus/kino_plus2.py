from random import random, randint, sample
from math import sqrt, tan, pi

# read the file kino_plus.py to understand the methodic
# many comments will be removed from here

# Max Possible Age for a human being in this cenario
MPA = 100
# FSK universe of possible values - maybe not so realistic
FSK_U = [4,6,8,10,14,16,18,20,25]


def getAge(FSK: int, IS_BORING: float = 0) -> int:
    """returns the age, based on FSK and chance of age stays under FSK"""
    
    if FSK <= 10:
        # more kids
        chance = 0.75
        age = randint(FSK,14) if random() < chance else randint(14,MPA)
    elif FSK <= 16:
        # no little kids, more teens and youth adults
        chance = 0.85
        age = randint(FSK,20) if random() < chance else randint(20,MPA)
    elif FSK <= 18:
        # more drama, more kills, more love, no teens under 16 allowed.
        chance = 0.85
        age = randint(FSK,20) if random() < chance else randint(20,MPA)
    else:
        # to be or not to be boring? that is the question.
        # if IS_B is low  -> we want more youth people -> than random() has more chance to win -> more if(s)
        # if IS_B is high -> we want more old people   -> than random() loses more -> more else(s)
        age = randint(FSK,40) if random() > IS_BORING else randint(40,100)
    return age


def print_summary(FSK: int, OCC_RATE: float, MAX_OCC: float) -> None:
    """prints a summary on the screen"""
    print(f"\nSummary:\n---")
    print(f"FSK:                     {FSK: 6} years")
    print(f"Desired occupation rate: {int(OCC_RATE * 100): 6}%")
    print(f"Maximal Capacity:        {MAX_OCC: 6} places")


def populate_room(ROOM: list[list[int]], OCC_RATE: float, FSK: int, IS_BORING: float) -> list[list[int]]:
    """populates the 2d array theater room"""
    
    for index_row in range(len(ROOM)):
        new_row = []
        for index_chair in range(len(ROOM[index_row])):
            p = random()
            if p <= OCC_RATE:
                # it means, if a randomic propability number is less than a randomic number above the minimal
                # the minimal occupation rate, then the chair has one above it.
                new_row.append(getAge(FSK, IS_BORING))
            else:
                new_row.append(0)
        ROOM[index_row] = new_row

    return ROOM

def print_room(ROOM) -> None:
    """prints the theater room as a rectangle. adapted to print trapezoidical room"""
    print("\n")
    print(" - -" * len(ROOM[0]))
    for r in ROOM:
        for c in r:
            if isinstance(c, int):
                if c > 0:
                    print(f"{c:^4}", end="")
                elif c == 0:
                    print(f" __ ", end="")
            else:
                print(f"{c:^4}", end="")
        print()


def populate_room_realistic(ROOM: list[list[int]], MAX_OCC: int) -> list[list[int]]:
    """prints the theater room, but as a trapezoid. more realistic"""

    # first, the room becomes a single list "places" (a reshape). the number of rows stay equal, at least initialy. 
    # as reference, one uses the square rate of maximal occupation, for the middle
    # expand above and contract under. "no places" positions are fulfilled with slashes. 
    # after process, simply print room simple

    # syntax for reshape as list compreehnsion (see "places" and imagine a for-loop within a for-loop)
    # [ <Ergebnis> <Äußere Schleife> <Innere Schleife> <Optionale Bedingung> ]

    ref_length = int(sqrt(MAX_OCC))
    places = [c for row in ROOM for c in row]

    # so .. the point is, area of rect = base x height -> and this is exactly the area of a trapezodie
    # if the middle is ref_length (because length is the best match), we can assume an angle of 15 degres
    angle = 15
    height = ref_length

    # some geometrie. the length each row by its position related to the height is
    # lenght = ref_length +/- 2 * tan(angle * pi/180) * (height / 2)
    # think about the (larger) upper side and the (smaller) lower side of a trapezoid (our is inverted)
    # then we can write length as function of height "y" as ref_length + 2 * tan(angle * pi/180) * (height/2 - y)
    #
    # if y = h/2, the length = ref_length; i.e. middle value
    # if y = height -> upper side -> bigger; else if y = 0 -> tan becomes negative -> lower side (smaller)
    #
    # we create an inner function to this conversion

    def getRowLength(ref_length: int, angle: int, lp: int, y: int) -> int:
        """returns the number of places per row of chairs, but..must be even"""

        # lp -> L-p -> length previous (same if first row); 
        # ly -> L-y -> length at y
        ly = ref_length + 2 * tan(angle * pi/180) * (ref_length/2 - y)

        # y0 is the initial length. since y must be even, it must also "jump" each two or remain
        # it says if closer to step or next step, then get it
        delta = lp - ly
        steps = delta // 2
        rest = delta % 2
        ly = lp - 2*steps if rest < 1 else lp - 2*(steps+1)
        
        return int(ly)

    new_room = []
    idx = 0
    lp = int(round(ref_length + 2 * tan(angle*pi/180) * (height/2)))
    for y in range(ref_length):
        ly = getRowLength(ref_length, angle, lp, y)
        one_row = places[idx:idx+ly]
        new_room.append(one_row)
        idx += ly
        lp = ly

    return new_room


def print_room_realistic(ROOM: list[list[int]]) -> None:
    """prints the theater, but more real, as a trapezoid and with corridors"""

    lenght_0 = len(ROOM[0])
    lp = lenght_0

    # for not-chair positions
    side_char = {"left":r" \  ", "right": "  / "}
    c1 = lenght_0//4
    c2 = lenght_0 - 1 - c1
        
    for row in ROOM:
        lr = len(row)
        if lr < lp:
            # then complete the row
            delta = lp - lr
            side = delta // 2
            for s in range(side):
                row.insert(0, side_char["left"])
                row.append(side_char["right"])
        # insert the corridors at 1/4 and 3/4 of initial length
        if row[c1] not in list(side_char.values()):
            row.insert(c1, " || ")
        if row[c2] not in list(side_char.values()):
            row.insert(c2, " || ")

    # uses the same (adapted) method.
    print_room(ROOM)



def main():
    # please read the comments at kino_plus.py (version 1)
    FSK = sample(FSK_U,1)[0]    
    IS_BORING = 0
    if FSK >= 18:
        IS_BORING = random()
        
    # maximal occupation and initial list
    MAX_OCC = 200
    ROOM = [
        [0] * 20
    ] * 10    

    # rate of occupation
    MIN_RATE = 0.2
    OCC_RATE = max(random(),MIN_RATE)

    print_summary(FSK, OCC_RATE, MAX_OCC)

    ROOM = populate_room(ROOM, OCC_RATE, FSK, IS_BORING)
    print_room(ROOM)

    ROOM_REAL = populate_room_realistic(ROOM, MAX_OCC)
    print_room_realistic(ROOM_REAL)

    # compare initial and effective occupation rate
    gasts = sum([sum([1 if chair>0 else 0 for chair in row]) for row in ROOM])
    print(f"\ncalculated occupation rate: {int(OCC_RATE * 100):4}%")
    print(f"effective occupation rate : {int(gasts/MAX_OCC * 100):4}%")
    print("\n")




if __name__ == "__main__":
    main()        