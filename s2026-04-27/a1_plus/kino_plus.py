from random import random, randint, sample

# lets create our own theater

# IMPORTANT -> you can print every row you want
#              change the code and insert your own print()'s


def getAge(FSK: int, IS_BORING: float) -> int:
    """returns the age, based on FSK. please, see explanation under"""
    if FSK <= 10:
        # chance to be a kid (must be high, cause has a FSK 10)
        # since kids go not alone, at least half kids, half parents
        chance = 0.75
        p = random()
        age = randint(4,10) if p < chance else randint(20,100)
    elif FSK <= 16:
        # the same idea, but more teens. adults are boring.
        # see: I can calculate random() and compare it directly on the row.
        chance = 0.85
        age = randint(10,16) if random() < chance else randint(20,100)
    elif FSK <= 18:
        # more drama, more kills, more love, no teens under 16 allowed.
        chance = 0.85
        age = randint(16,40) if random() < chance else randint(40,60)
    else:
        # be or not to be boring. that is the question. -> so: IS_BORING is a float number from 0..1
        # a lower  IS_B against any random() has more chance to be "less than" random()
        # a higher IS_B has ------------------>  more chance to be "greater than" random()
        # since IS_B is a constant i.e. calculated only once with FSK input, we can use it directly.
        
        # if IS_B is low -> we want more youth people -> than random() > IS_B has more chance to win
        # alternatively, if IS_B is high -> we want more old people -> than random() loses more -> more else(s)
        age = randint(18,40) if random() > IS_BORING else randint(40,100)
    return age


def print_summary(FSK: int, OCC_RATE: float, MAX_OCC: float) -> None:
    """prints a summary on the screen"""
    print(f"\nSummary:\n---")
    print(f"FSK:                     {FSK: 6} years")
    print(f"Desired occupation rate: {int(OCC_RATE * 100): 6}%")
    print(f"Maximal Capacity:        {MAX_OCC: 6} places")


def print_room(ROOM) -> None:
    print("")
    for r in ROOM:
        for c in r:
            if c > 0:
                print(f"{c:^4}", end="")
            else:
                print(f" __ ", end="")
        print()

def main():

    # first I had an input for FSK, but to input FSK every time I test it was boring
    # then I created this if: set "True" to manually input of "False" to get it randomicaly
    # the variable IS_BORING will be calculated anyway

    if False:
        # first: enter the FSK and check if it is valid (0-18)
        while True:
            FSK = input("bitte geben Sie den FSK Ihres Kinofilm ein: ")
            try:
                FSK = int(FSK)
                if FSK >= 0 and FSK <= 100:
                    break
                print("FSK muss ein Ganzzahl zwischen 0 und 100 sein.")
            except:
                print("FSK muss Nummer sein.")
    else:
        FSK = sample([4,6,8,10,14,16,18,20,25],1)[0]
    
    if FSK >= 18:
        IS_BORING = random()

    # if you've reached this point, it means, fsk is valid
    # this block explains the functions getAge(). lets assume:
    #  * children movies (<10) has parents in the session
    #  * teens movies (10-16) has less parents and more same age people
    #  * from 16, more gasts up to 40 and some older
    #  * and from 18, it varies. the movie room can assume two situations
    #    (and we dont know what it is, because we will use a random function)
    #      * situation 1 -> the movie is nice for youth adults and has more people under 40
    #      * situation 2 -> the movie is boring for youth adults and has more people over 40

    # STOP: now I write the getAge() function and I realised that I need to say previously
    #       if an adult film is boring or not for youth adults. this value must be passed 
    #       also previously and therefore previously calculated too, better directly after FSK.

    # we assume, our kino has capacity for 200 gasts
    # the the chairs are disposed in rows of 20. every chair is empty. good.
    # using the "multiplication of list element" to create a list of same things
    MAX_OCC = 200
    ROOM = [
        [0] * 20
    ] * 10    

    # then lets populate it. We assume our movie has a minimal occupations rate
    # of 20% upt to full. we'll use the built-in functions random () and randint() to get this 
    # value. The code must be so many autonomous as possible.
    # IMPORTANT -> we import only what we need
    MIN_RATE = 0.2
    OCC_RATE = max(random(),MIN_RATE)

    print_summary(FSK, OCC_RATE, MAX_OCC)

    # ok! let's use probability. random() returns a number between 0 and 1; and this is our room occ rate.
    # but it means also, that each chair has a change of OCC_RATE to be occupied or not,
    # and we can tst it and calculate the real occupation rate in the end
    for index_row in range(len(ROOM)):
        new_row = []
        for index_chair in range(len(ROOM[index_row])):
            p = random()
            if p <= OCC_RATE:
                # it means, if a randomic propability number is less than a randomic number above the minimal
                # the minimal occupation rate, then the chair has one above it.
                new_row.append(getAge(FSK, IS_BORING=0))
            else:
                new_row.append(0)
        ROOM[index_row] = new_row

    # now we have our room and can proceed with the solution for any movie room
    # you can set the control variable as a function or input
    PRINT_ROOM = 1
    if PRINT_ROOM:
        print_room(ROOM)

    # and we can calculate the effective occupation rate and compare with the theoretical rate above
    # this formula is the solution from question A1
    gasts = sum([sum([1 if chair>0 else 0 for chair in row]) for row in ROOM])
    print(f"\ncalculated occupation rate: {int(OCC_RATE * 100):4}%")
    print(f"effective occupation rate : {int(gasts/MAX_OCC * 100):4}%")
    print("\n\n")




if __name__ == "__main__":
    main()        