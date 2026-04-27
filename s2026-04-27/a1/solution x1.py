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


belegt = get_chairs(kinosaal)
leere = get_empty(kinosaal)

# 1. gesamtanzahl
count_chair = sum([len(r) for r in belegt])



# 2. avg present persons
sum_ages = sum([sum(c) for c in belegt])
avg_ages = sum_ages / count_chair



# 3. more chairs
max_nr_per_reihe = -1
nr_von_der_reihe = -1

# loop over belegt (oder kino) and find row more number of belegt
# rows 1,2,3,4 . . . from kino 2d list
for reihe_nummer_minus_eins in range(len(belegt)):
    nr_of_belegt_in_dieser_reihe = len(belegt[reihe_nummer_minus_eins])
    if nr_of_belegt_in_dieser_reihe > max_nr_per_reihe:
        nr_von_der_reihe = reihe_nummer_minus_eins
        max_nr_per_reihe = nr_of_belegt_in_dieser_reihe
print("reihe mit meinsten belegten Sitze ist die: ", nr_von_der_reihe+1)






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
 
 
 
 
 