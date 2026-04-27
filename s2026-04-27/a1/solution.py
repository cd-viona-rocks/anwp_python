kinosaal = [
    [25, 34, 0, 18, 42],
    [0, 0, 51, 60, 33],
    [19, 22, 23, 0, 0],
    [45, 38, 0, 29, 31],
]


def get_chairs(kino: list[list[int]]) -> list[list[int]]:
    """returns a 2d liste of occupied chairs"""
    chairs = []
    for r in kinosaal:
        one_row = [c for c in r if c != 0]
        chairs.append(one_row)
    return chairs


def get_empty(kino: list[list[int]]) -> list[list[int]]:
    """returns a 2d liste of empty chairs"""
    chairs = []
    for r in kinosaal:
        one_row = [c for c in r if c == 0]
        chairs.append(one_row)
    return chairs


def main():
    belegt = get_chairs(kinosaal)
    leere = get_empty(kinosaal)

    # 1. gesamtanzahl
    count_chair = sum([len(r) for r in belegt])

    # 2. avg present persons
    sum_ages = sum([sum(c) for c in belegt])
    avg_ages = sum_ages / count_chair

    # 3. more empties
    max_b = 0
    r = -1
    for x in range(len(belegt)):
        b = len(belegt)
        if b > max_b:
            r = x
            max_b = b
    print("reihe mit meinsten belegten Sitze ist die: ", r)

    # 4. 
    

    # - - - ignore this - - -
    # # 1. sol2
    # sitze_per_reihe_von_belegt = []
    # for r in belegt:
    #     sitze_per_reihe_von_belegt.append(len(r))
    # anzahl_belegt = sum(sitze_per_reihe_von_belegt)

    # # 1. sol3
    # count = 0
    # for r in kinosaal:
    #     for s in r:
    #         if s != 0:
    #             count += 1
    # # pass
    # - - - ignore end - - -


if __name__ == "__main__":
    main()




def belegte_sitze_berechnen(kinosaal_plan):  # Erstellen einer Funktion
    belegte_sitze = 0  # Initiierung belegte_sitze
 
    for sitzreihe in kinosaal_plan:  # Kinosaal von oben nach unten durchgehen.
        for platz in sitzreihe:  # Kinosaal von links nach recht durchgehen
            if platz > 0:  # Prüfen index > 0
                belegte_sitze += (1)  # Bei jedem belegten Platz wird belegte_sitze um ein erweitert
 
    return belegte_sitze  # Die Ausgabe
 
def durchschnitt_alter(kinosaal_plan):
    alter_gesammt = 0
    anzahl_sitzte = belegte_sitze_berechnen(kinosaal_plan)
 
    for sitzreihe in kinosaal_plan:
        for platz in sitzreihe:
            if platz != 0:
 
                alter_gesammt += platz
    ergebnis = alter_gesammt / anzahl_sitzte
    return ergebnis
        
def vollste_reihe(kinosaal_plan):
    maximale_anzahl = 0
    reihen_nummer = 0
 
    for i,sitzreihe in enumerate(kinosaal_plan):
        anzahl = belegte_sitze_berechnen(sitzreihe)
        if anzahl > maximale_anzahl:
            reihen_nummer = i +1
            maximale_anzahl = anzahl
    return reihen_nummer
print("\n--- -1.- ---")
print(f"Aktuell belegte Plätze: {belegte_sitze_berechnen(kinosaal)}")
print("\n--- -2.- ---")
print(f"Das Durchschnittsalter beträgt: {durchschnitt_alter(kinosaal)}")
print("\n--- -3.- ---")
print(f"Am meisten belegte Plätze in Reihe: {vollste_reihe(kinosaal)}")
 
 
 
 
 