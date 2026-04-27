kinosaal = [
    [25, 34, 0, 18, 42],
    [0, 0, 51, 60, 33],
    [19, 22, 23, 0, 0],
    [45, 38, 0, 29, 31],
]
 
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
 
 
 
 
 