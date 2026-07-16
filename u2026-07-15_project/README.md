# README

## Task description / Scope of work

```
Aufgabenstellung:
Wir haben 4 Gruppen. Diese Woche Mittwoch/Donnerstag soll die Aufgabenstellung  
abgeschlossen sein. Kommende Woche dann die Umsetzung (bis Donnerstag vielleicht).  
Zeitbudget für die Umsetzung: etwa 7-8 Zeit-Stunden, also a 60 Minuten.
```

This project must be done in 08:00 running development hours.  
The label [EXTENSION] marks possible continuations for this project.  

### Your tasks are:

**Mandatory (must be done within given BG)**  

1. implement the classes Automatic and Ticket according to the use cases under.  
   1.1. create test cases for each class  
   1.2. run the test cases in separated files (use from filename import classname)  

**Extension (can be done acoording to working hours availability)**  

2. Run a simple case, where one / some clients buy ticktes in different situations.  
   2.1. use the scenario under to simulate one case  
   2.2. as extension you can implement a small simulation according to the the section "Running it"  

3. With in the implementation of the case "Running it" you can create te following diagramms
   3.1. Activity Diagramm
   3.2. Sequence Diagramm

### HINT

Follow the method [MoSCow][https://en.wikipedia.org/wiki/MoSCoW_method] [must have, should have, could have, won't have]  
  

## USE CASES / USE STORIES

The object of development is the buying process of tickets for an hipothetical  
swimming center.

CONTEXT AND SITUATION - - -   

there is at least a client and the client wants to visit the swimming center.  

the swimming center has different areas: entrance, swimming area, child area  
and sauna.  

when the client arrives at first the entrance area (not for swimming) and  
can buy a ticket from one of the automatic machines.  

TICKET OPTIONS - - -  

buying a ticket offer to the client 3 options of tickets, according to  
how many time, the client wants to stay: 
 * SHORT_TERM for 3 hours from the check-in, for 2.50 Banana-Cashes;  
 * LONG_TERM for 6 hours from the check-in, for 4.00 Banana-Cashes, and;  
 * DAY_PASS for the whole day, for 5.00 Banana-Cashes.  

A valid Ticket allows access to the swimming area and child area   
for the ticket time.  

When buying a ticket, the client should be asked if he wants access to the sauna.  

A valid ticket doesn't allow automatically access to the sauna.  
The client can give the aditional option for sauna,  
for an extra-price of 1.50 Banana-Cashes.

CLIENT SUBSCRIPTION - - -  

When buying a ticket, the client should be asked if he has a valid subscription  
then he receives automatically a DAY_PASS Ticket.  

The subscription doesn't allow automatically access to the sauna.  
It must be separated indicated when buying a ticket.  

The price of a subscription will be not threated here. The client simply   
has one or not. [EXTENSION] This is a possible extension for the code.  

AUTOMATIC MACHINE - - -  

An automatic machine can sell a ticket.  

An automatic machine starts the working cycle with a certain amount of Banana-  
-Cash.

On the buying process, the client must insert Banana-Cash or tell the machine,  
he has a valid subscription. [EXTENSION] One can check, if the subscription is  
valid, e.g. through a limit date. [EXTENSION] One can define, if subscription  
should be payed monthly or annualy.  

On the buying process, the automatic itself, gives the ticket creation date  
and time in.  

On the buying process, the automatic itself, can print on the ticket,  
the client number, if this has a valid subscription. [EXTENSION] One can create  
a database of clients or randomimize it.  

The automatic should calculate if there is enough money to pay the ticket.  

The automatic should calculate if there is something to give back and how many.  

## Running it

This section shows a possible scenario to run a simple simulation.

A simple run can be described as follows:

1. Select a group of visitors from the client list:
   - one full family group,
   - one second family group with only one adult and one child,
   - and ten single visitors.
2. Give money to the visitors before they buy their tickets.
   - family members pay together through the oldest family member,
   - single visitors receive their own cash options.
3. Let each visitor choose a ticket type.
   - families usually buy a LONG_TERM or DAY_PASS ticket,
   - single visitors may choose a random ticket and optionally sauna access.
4. Run the automatic machine and print a short report:
   - which tickets were sold,
   - how much cash remains in the machine,
   - and which clients visited the swimming center.

## Tests

#### tested files

 * 2026-07-14 test_tickets.py
 * 2026-07-14 test_automatics.py

[https://en.wikipedia.org/wiki/MoSCoW_method]: https://en.wikipedia.org/wiki/MoSCoW_method