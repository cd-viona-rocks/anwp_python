# TODOS

Tasks Notation:  

 * [ ] open task / to be done / TODO
 * [O] At work / running / hinter dem Schwanz hinterherlaufen
 * [/] abandones task - then say why. / ggf [//] auf den Mond geworfen
 * [X] Done!
 
## 3. Ihr Auftrag (Task Description TD)

Entwickeln Sie auf Basis der vorliegenden Diagramme eine **(TD001)** lauffähige Terminalanwendung (Kommandozeile), die den Bestellprozess von PizzaFlow aus Kundensicht simuliert. Eine grafische Oberfläche wird nicht erwartet – Ein- und Ausgabe erfolgen über die Konsole. 

 [ ] TODO **TD001** lauffähige Terminalanwendung (siehe 3.1) aus Kundensicht

Die Anwendung soll die zentralen Abläufe aus dem **(TD002)** Aktivitäts- und **(TD003)** Zustandsdiagramm abbilden und auf den im **(TD004)** Klassendiagramm definierten Klassen und Attributen aufbauen **(TD005)**. 
 
 [O] TODO **TD002** Ablauf aus dem Aktivitätsdiagramm
 [O] TODO **TD003** Ablauf aus dem Zustandsdiagramm
 [O] TODO **TD004** Check Diagrams - assumed to be right, cause there's no "check it" for these diagrams
 [O] TODO **TD005** assumed: we can only use the methods and classes present in the two class diagrams

### 3.1 Pflichtumfang (Mandatory Requirements)

Die folgenden Kernfunktionen müssen in der Terminalversion enthalten und über ein einfaches Text-/Auswahlmenü bedienbar sein: 

 [X] TODO check activity / sequence diagrams here
 [/] TODO - replaced by 4., 5.
     [/] 1. check each step under against the activity diagramm; 
     [/] 2. decide if right / wrong, document it; 
     [/] 3. after decision, implement exactly "as is"

[O] TODO      
     [O] 4. try to implement "as is"
     [O] 5. then correct / change it "as necessary".

• [O] **MR001** Kunde anmelden / erkennen  
• [ ] **MR002** Pizza(s) auswählen und zur Bestellung hinzufügen (mehrere Pizzen pro Bestellung müssen möglich sein) 
• [ ] **MR003** Bestellung überprüfen und bestätigen oder abbrechen 
• [ ] **MR004** Bezahlvorgang durchführen 
• [ ] **MR005** Bestellstatus verfolgen (inkl. Statuswechsel gemäß Zustandsdiagramm) 

    *** WHERE IS THE PREPARATION ?!?!?! ***

• [ ] **MR006** Bestellung durch Mitarbeiter entgegennehmen, bestätigen und einem Lieferanten zuweisen 
                            *** BESTÄTIGEN, VORBEREITEN, BACKEN ?!?!?! wie werden Pizzen geboren ?!?!?!? ***

• [ ] **MR007** Lieferant aktualisiert den Status bis zur Zustellung 
                                *** LIEFERANT liefert ?!?!?! Angenommen: JA! ***



 [ ] TODO documentation "this is a optional requirement OR"

• [ ] **OR001** Die Anwendung darf im Terminal simuliert mehrere Rollen abbilden (z. B. per Menüauswahl "Sie sind: Kunde / Mitarbeiter / Lieferant") – ein Mehrbenutzerbetrieb über Netzwerk ist nicht gefordert. 

 [ ] QUESTION according to description above, a multi role termianl app is desired - how to write a multi role threadless over terminal ?!?!?!
 [ ] QUESTION "Terminal simuliert mehrere Rollen abbilden" Optional task into "Pflichtumfang" ?!?!?!
 [ ] QUESTION is ti optional ?!?!?
 

### 3.2 Umgang mit den Diagrammen (Diagramm Requirements)

• [X] **DR001** Prüfen Sie das Klassendiagramm auf Vollständigkeit und Konsistenz zu den anderen Diagrammen (Attribute, Methoden, Beziehungen). 
• [O] **DR002** Prüfen Sie, ob Aktivitäts- und Zustandsdiagramm zueinander passen (z. B. Bezeichnungen der Status/Übergänge). 
• [O] **DR003** Wo Diagramme unklar, widersprüchlich oder lückenhaft sind, treffen Sie eine sinnvolle eigene Entscheidung und dokumentieren Sie diese kurz (siehe Punkt 5). 

• [ ] **DR004** Sie müssen keine Fehler "beheben", indem Sie die Diagramme selbst neu zeichnen – es reicht, den Code korrekt und nachvollziehbar zu gestalten. 
        DR004 is not consistent against DR003 - we should follow or criticize and decide ?!?!?

 [X] TODO class diagramm check - DONE, see it
 [X] TODO confront activity against state, document it
 [/] TODO DR003 DONT ASK ! ! ! DECIDE AND DOCUMENT IT ! ! !
 [/] TODO we shouldn't create any class, attribute or method - is it good or bad ?!?!?!

### 3.3 Optional / Erweiterung (nur falls Zeit bleibt) (Extended Requirements EX)

• [ ] **EX001** Bestellung stornieren (Abbruch) - bis zum welchen Zeitpunkt kann man stornieren ?!?!?! Ich denke, nach Zahlung aber immer noch vor der Vorbereitung
• [ ] **EX002** Pizza bewerten nach Zustellung 
• [ ] **EX003** Einfache Persistenz (z. B. Bestellungen in einer Datei/JSON zwischenspeichern) - if we do, do with sqlite. but then, in this case, we need to chenge some code.
• [ ] **EX004** Einfache Rabatt- oder Rechnungslogik - 