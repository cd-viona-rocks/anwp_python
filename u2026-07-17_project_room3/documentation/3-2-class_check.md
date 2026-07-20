# README PIZZAFLOW


## comparing two class diagramms

classes(BW: 7):  
 * Zahlung(C), attr OK  
    getBetrag(BW) not at (C)  
    getZahlung(BW) not at (C)  
 * Lieferant(C), attr OK  
    getLieferadresse(BW) but lieferadresseAnzeigen(C)  
 * Person(C), attr OK, meth OK  
 * Kunde(C), attr OK, meth OK  
 * Pizza(C), attr OK  
    getPizzaID(BW) not at (C)  
    getGroesse(BW) not at (C)  
 * Bestelung(C)  
    attr pizzen(C) not at (BW)  
    meth pizzaGesamtanzahl(C) not at (BW)
    meth pizzaHinzufuegen(C) not at (BW)
 * Mitarbeiter(C), attr OK, meth  
    bestellungZuweisen(C) has +1 arg (mitarbeiter: Mitarbeiter)  
    bestellungAktualisieren(BW) not at (C)  
    setBestellstatus(C) not at (BW)  

 class names OK!
