from datetime import datetime
import sys
from pathlib import Path
import pandas as pd
from random import random

from hashlib import pbkdf2_hmac
from hmac import compare_digest
from base64 import b64decode  # b64encode when create hashes to save

from data.log import LOG
from data.data import *
# from data/data.py import PIZZAS, ORDERS as list[dict] and it works as a skizze for DB
# an instantiation is not necessary, because the data can be directly processed as python dict

from classes.person import Person
from classes.kunde import Kunde
from classes.mitarbeiter import Mitarbeiter
from classes.lieferant import Lieferant

# from classes.pizza import Pizza
# from classes.bestellung import Bestellung
# NOTE: see the comments at import data

SEPARATOR = "\n" + " ="*20 + "\n"

class App:
    """implements the activity diagram and update states"""
    
    def __init__(self):
        # load some clients, employees, delivery people as instantiated object
        self.kunden = []
        self.mitarbeiter = []
        self.lieferanten = []

        self.hashes = []

        self.user_classes = []
        self.user_loggedin = None

    def run(self):
        """runnable methods for execution."""

        print(SEPARATOR + "  starting system.  " + SEPARATOR)
        self.log_event("system starts.")

        # since this version doesn't use a database, all data is loaded either 
        # from a csv file or from a python variable, as a list (see method docs)
        self.load_data()

        self.log_event("loaded pizzas menu by imports")
        self.log_event("loaded orders list by imports")
        self.log_event("loaded logs by imports")

        # ONLY FOR TESTS
        msg = f"\ntry this examples:\n{self.kunden[0]}\n{self.mitarbeiter[0]},\n{self.lieferanten[0]}\n"
        print(msg)

        self.screen_initial()

    def terminate(self):
        print(SEPARATOR + "\n  closing system.  \n" + SEPARATOR)
        self.log_event("system closes.")

        # a dump print log - don't do it ! ! !
        for log in LOG:
            print(log)
        print("\n\n")

        # a smart view log - do it, when we can ! ! !
        # df_logs = pd.DataFrame(LOG)
        # df_logs.to_csv("./data/log.csv")

        sys.exit(0)

    def log_event(self, event_description: str) -> None:
        log_time = datetime.now().timestamp()
        LOG.append({"timestamp":log_time, "description":event_description})
        # print(f"LOG at {log_time}: {event_description}")           


    # data methods

    def load_data(self) -> None:
        """loads some pre defined people from people.csv,
         separate them into clients, employees and deliveries;
         and save hashes for client login at password.csv;
         load pizza menu from data.data.PIZZAS (a python list).
         
         the csv files should be seen as a possible extension for DB see file: 
         Aufgabenstellung, 3.3. Optional / Exweiterung: EX003 and EX004
         """
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        # print(BASE_DIR.name)

        path_people_csv = BASE_DIR / "data" / "people.csv"
        if not path_people_csv.exists():
            raise ImportError("people.csv couldn't be imported.")
        
        path_pw_hashes_csv = BASE_DIR / "data" / "password_hashes.csv"
        if not path_people_csv.exists():
            raise ImportError("password_hashes.csv couldn't be imported.")

        # for the three instantiations under, use the following method:
        # 1. select the desired columns
        # 2. filter the dataframe and convert it as a list of dictionaries
        # 3. instantiate it as a list compreehnsion for object attribute

        df_people = pd.read_csv(path_people_csv)
        print("\n" + " "*4 + "all data from people imported" + " "*4 + "\n")

        # - - - user class [ client | employee | delivery ] - - -
        df_user_classes = df_people[["id", "class"]]
        self.user_classes = df_user_classes.to_dict(orient="records")

        # - - - clients - - -
        df_clients = df_people[df_people["class"] == "client"]
        df_clients["client_number"] = df_clients["id"]
        
        cols = Person.PERMITTED_ATTR[:]
        df_clients = df_clients[cols]
        kwargs_clients = df_clients.to_dict(orient="records")

        self.kunden = [Kunde(**kwargs).to_dict() for kwargs in kwargs_clients]
        self.log_event("loaded clients")

        df_pw_db = pd.read_csv(path_pw_hashes_csv)
        print("\n" + " "*4 + "all data from hashes imported" + " "*4 + "\n")
        self.hashes = df_pw_db[["user_id", "salt", "iter", "password_hash"]].to_dict(orient="records")
        self.log_event("loaded password hashes")


        # - - - employees - - -
        df_emplo = df_people[df_people["class"] == "employee"]
        df_emplo["employee_number"] = df_emplo["id"]
        
        cols = Person.PERMITTED_ATTR[:]
        df_emplo = df_emplo[cols]
        kwargs_emplo = df_emplo.to_dict(orient="records")

        self.mitarbeiter = [Mitarbeiter(**kwargs).to_dict() for kwargs in kwargs_emplo]
        self.log_event("loaded employees")


        # - - - delivery - - -
        df_deliv = df_people[df_people["class"] == "delivery"]
        df_deliv["employee_number"] = df_deliv["id"]
        
        cols = Person.PERMITTED_ATTR[:]
        df_deliv = df_deliv[cols]
        kwargs_clients = df_deliv.to_dict(orient="records")

        self.lieferanten = [Lieferant(**kwargs).to_dict() for kwargs in kwargs_clients]
        self.log_event("loaded deliveriy people")


    # - - - screen methods - - - 

    def print_message(self, text: str, n: int = 4) -> None:
        """prints a default one row message between empty rows and with n indentation
           don't use it for multi rows messages. instead considere use print_option_list.
        """
        print("\n" + " "*n + text + " "*n + "\n")

    def print_warning(self, text: str, n: int = 4) -> None:
        """prints a warning on the screen"""
        print("\n" + " !"*n + " "*4 + text +" "*4 + " !"*n + "\n")
        self.log_event(text)

    def print_option_list(self, title: str, option_list: dict) -> None:
        msg = " "*4 + f"{title}:\n" + " "*4 + " -"*16 + "\n"
        for k,v in option_list.items():
            msg += " "*4 + f"{k}: {v}\n"
        print(msg)


    def screen_initial(self) -> int:
        """MR001 'Anmelden' """
        counter = 0
        o = -1
        title = "Bitte wählen Sie eine Option"
        options = {0: "wenn Sie die App schließen möchten.", 1: "Kunde", 2: "Mitarbeiter", 3: "Lieferant"}
        print(SEPARATOR)
        while True:
            counter += 1
            if counter > 5:
                raise InterruptedError("tries exceeded. app execution interrupted.")
            try:
                self.print_option_list(title, options)
                o = int(input(" "*4 + "Geben Sie den passenden Wert ein: "))
                if o == 0:
                    print(" "*4 + "Option Schließen aufgerufen.\n")
                    break                       
                elif o in options.keys():
                    print("\n" + " "*4 + f"Weiter zur Anmeldung als {options[o]}\n")
                    break
                else:
                    # simple raise to terminate try block
                    raise 
            except:
                print("\n" + " -"*20 + "\n\nIhre Option muss einer davon sein: 1, 2, 3 oder 0 um abzubrechen.\n")

        if o not in options.keys() or o < 0:
            raise ValueError("invalid value for option at this point.")
        elif o == 0:
            self.terminate() 
        else:
            self.user_login(o,options[o]) 

        raise InterruptedError("unexpected point at App.screen_initial() have been reached.")


    def user_login(self, user_class: int, user_mode: str) -> bool:
        o, user_name, user_pw = -1, None, None
        options = {}

        c1 = 0
        response = {"access": False, "user": None}

        # - - - menu context - - -

        msg = "\n" + " "*4 + f"Sie sind innerhalb des Kontextes: {user_class} - {user_mode}"
        msg += "\n" + " "*4 + " -"*20
        msg += "\n" + " "*4 + "Bitte geben Sie Ihren Benutzername und Passwort Kommagetrennt"
        msg += "\n" + " "*4 + "e.g. maxsupermustermann, banana1234 oder <Enter> zu Abbrechen."
        print(SEPARATOR + msg)

        # - - - OPTION BLOCK ONE - - -

        stop1, stop2 = False, False
        while not stop1:
            c1 += 1
            if c1 > 5:
                raise InterruptedError("tries exceeded. app execution interrupted.")
            try:
                user_data = input("\n" + " "*4 + "Geben Sie Ihre Logindaten ein: ")
                if user_data == "" or "," not in user_data:
                    # simple raise to interrupt try block
                    raise ValueError("Vorgang abgebrochen.")
                user_name, user_pw = [x.strip() for x in user_data.split(",")]
                if " " in user_name or " " in user_pw:
                    raise ValueError("Benutzername und Passwort dürfen keinen Leerzeichen enthalten.")
                print(f"    Benutzername: {user_name}\n    Passwort: {user_pw}")
                stop1 = True
            except Exception as e:
                self.print_warning(str(e))

                # - - - OPTION BLOCK TWO - - -
            
                c2 = 0
                stop2 = False
                while not stop2:
                    c2 += 1
                    if c2 > 5:
                        raise InterruptedError("tries exceeded. app execution interrupted.")
                    try:
                        title = "\n" + " "*4 + "Möchten Sie zurück zur Optionen oder nochmal versuchen"
                        options = {0: "zurück zur Menu Optionen.", 1: "nochmal versuchen, die Benutzername und Passwort einzugeben."}
                        self.print_option_list(title, options)
                        o = int(input("\n" + " "*4 + "Geben Sie den passenden Wert ein: "))
                        if o == 0:
                            self.print_message("Sie werden zurück zum Menu Optionen weitergeleitet")
                            self.screen_initial()
                            # stop1 = True
                            # stop2 = True
                        elif o == 1:
                            stop2 = True
                        else:
                            msg = "\n" + " "*4 + "Sie haben einen falschen Wert eingegeben."
                            msg += "\n" + " "*4 + "Bitte versuchen Sie es noch einmal.\n"
                            print(msg)
                    except:
                        pass

        # runs only if once into second while
        if stop2:
            if o not in options.keys() or o < 0:
                raise ValueError("invalid value for option at this point.")

            if o == 0:   
                self.screen_initial()

        # - - - login context - - -

        # print(f"o: {o}, user_class: {user_class}")
        if user_class == 1:
            database = self.kunden
        elif user_class == 2:
            database = self.mitarbeiter
        elif user_class == 3:
            database = self.lieferanten
        else:
            raise ValueError("invalid value for user_data within login context.")

        # print(f"len database: {len(database)}\ne.g. database: {database[0]}")

        # user name must be unique
        user = list(filter(lambda x: x["name"] == user_name, database))
        if len(user) != 1:
            raise ValueError("user data not found.")
        user = user[0]

        # can more than one pw be equals ?!?!?! i don't know. Banana12341234@!
        hash = list(filter(lambda x: x["user_id"] == user["id"], self.hashes))
        if len(hash) != 1:
            raise ValueError("user password hash not found.")
        hash = hash[0]

        # print(f"{user}\n{hash}")
        # sys.exit(0)        

        hash_salt = hash["salt"]
        hash_iter = hash["iter"]
        hash_saved = hash["password_hash"]

        # * * * PLEASE NOT, THAT A TABLE USER (as our people.csv) NEVER MUST SAVE THE PASS * * * 
        # * * * THE PASS IS PRIVATE FOR THE USER. WE SAVE PW FOR EDUCATIONAL USE ! ! ! * * * 
        
        b64_salt = b64decode(hash_salt)  # <-- back to bytes
        b64_hash = b64decode(hash_saved)

        attempt_hash = pbkdf2_hmac("sha256", user_pw.encode(), b64_salt, hash_iter)

        if compare_digest(attempt_hash, b64_hash):
            """MR001 'Kunden erkennen' """
            self.user_loggedin = user
            self.print_warning(f"User {self.user_loggedin["id"]}: login successful.")
            self.create_order({"access":True, "user":user})
        else:
            self.print_warning("Login fehlerhaft. Sie werden zurück zur Menu Optionen weitergeleitet.")
            self.screen_initial()

        raise InterruptedError("unexpected point at App.login_user have been reached.")


    def create_order(self, rsp_login: dict) -> None:
        """ MR002 'Pizza auswählen, bestätigen, wiederholen'
            implements the order process with choice menu
            {"id": 10, "name":"Margherita", "size":"M", "price": 6.50, "currency":"EUR"},
            """

        NEW_ORDERS = []
        PERMITTED_CODES = [p["id"] for p in PIZZAS]
        print(" "*4 + " -"*20)
        self.print_message("Sii benvenuto alla pizzeria di Radu. Sentiti libero di sentirti a tuo agio, Belo!")

        pizza_title = "Pizza Menu"
        pizza_options = dict()
        for x in [{p["id"]: f'{p["name"]:<20s}{p["size"]:<4s}{p["price"]:>6s} EUR'} for p in PIZZAS]:
            k, v = next(iter(x.items()))
            pizza_options[k] = v
        self.print_option_list(pizza_title, pizza_options)

        # - - - WHILE ONE - - -

        stop1 = False
        while not stop1:
            counter = 0
            msg = " "*4 + "Bitte geben Sie Ihre Bestellung nach 'Pizza Code' ein."
            msg += "\n" + " "*4 + "Geben Sie 0, um die Bestellung zu beenden"
            msg += "\n" + " "*4 + "     oder 1, um den Pizza Menu zu wiederholen.\n"
            print(msg)

            stop2 = False
            while not stop2:
                p_id = input(" "*4 +"Gewünschter Code: ")
                if p_id == "0":
                    if len(NEW_ORDERS) > 0:
                        # show the order
                        stop2 = True
                    else:
                        self.print_message("Sie haben keine Pizza bestellt. Möchten Sie wiederholen?")
                elif p_id == "1":
                    print("\n\n")
                    self.print_option_list(pizza_title, pizza_options)
                elif p_id in PERMITTED_CODES:
                    # create / add to order -> add an elem to ORDERS LIST
                    order = {"client_id": self.user_loggedin["id"], "pizza_id":p_id, "order_status":0, "payment_status":0}
                    NEW_ORDERS.append(order)
                    self.log_event(f"user {self.user_loggedin["id"]} ordered: {str(order)}")
                else:
                    self.print_warning("Sie haben einen ungültigen Code eingegeben.")


                if p_id == "0":
                    """MR005 'Bestellung einsehen' """
                    self.log_event(f"user {self.user_loggedin["id"]} calls the bill to confirm.")
                    msg = "\n" + " "*4 + f"Va bene Belo {self.user_loggedin["name"]}. Preparo subito il suo ordine. Buon appetito!"
                    msg += "\n" + " "*4 + " -"*20
                    msg += "\n\n" + " "*4 + "Ihre Bestellung ist die folgende: \n"
                    print(msg)

                    total = 0
                    qty = len(NEW_ORDERS)
                    for o in NEW_ORDERS:
                        pizza_obj = list(filter(lambda x: x["id"] == o["pizza_id"], PIZZAS))[0]
                        total += float(pizza_obj["price"])
                        order_str = " "*6 + f'{pizza_obj["name"]:<20s}{pizza_obj["size"]:<4s}{pizza_obj["price"]:>6s} EUR'
                        print(order_str)
                    msg = " "*4 + " -"*20
                    msg += "\n" + " "*6 + f"Belo {self.user_loggedin["name"]}, Ihre Bestellung enthält {qty} Pizz{"en" if qty > 1 else "a"}."
                    msg += "\n" + " "*6 + f"Gesamtkosten: {total:8.2f} EUR, MwSt Niemals."
                    print(msg)

                    msg += "\n" + " "*4 + " -"*20
                    msg = "\n" + " "*4 + "Sie haben Ihre Bestellungsliste vorübergehende beendet. Bitte drucken Sie:"
                    msg += "\n" + " "*6 + "<ENTER> um Ihre Bestellung zu bestätigen und weiter zur Bezahlung gehen"
                    msg += "\n" + " "*6 + "  0     um den Vorgang zu wiederholen. Ihre Bestellung wird gespeichert. "
                    msg += "\n" + " "*6 + "  1     um den Vorgang abzubrechen. Ihre Bestellung wird gelöscht. \n"
                    print(msg)

                    stop3 = False
                    while not stop3:
                        o = input(" "*6 + "Wie möchten Sie weiter: ")
                        print("\n\n")
                        if o == "":
                            self.log_event(f"user {self.user_loggedin["id"]} confirms the order and follow to payment.")
                            for o in NEW_ORDERS:
                                o["order_status"] = 1
                            ORDERS.extend(NEW_ORDERS)
                            self.payment_process()
                            stop1 = True
                            stop2 = True
                            stop3 = True
                        elif o == "0":
                            stop2 = True
                            stop3 = True
                        elif o == "1":
                            self.log_event(f"user {self.user_loggedin["id"]} cancels the order and terminate the execution.")
                            msg = "\n" + " "*4 + " -"*20
                            msg += "\n" + " "*4 + "Ihr Vorgang wurde abgebrochen und Ihre Bestellung gelöscht.\n"
                            msg += "\n" + " "*4 + "Grazie per la sua visita.\nCiao Belo!\n"
                            print(msg)
                            self.terminate()
                        else:
                            msg = "\n" + " "*4 + " -"*20
                            msg += "\n" + " "*4 + "Bitte geben Sie eine gültige Option ein: <ENTER> , 0 oder 1.\n"
                            print(msg)


        raise InterruptedError("unexpected point at App.create_order have been reached.")


    def payment_process(self):
        """MR004 'Zahlung erstellen, Bestellung bezahlen' 
            use 2% from random to cancel the payment due technical factors
            use 1% for insuficient founds
        """

        # TODO

        n = random()
        if n <= 0.01:
            # w/o founds
            # cancel order and visit
            # terminate
            pass
        elif n <= 0.03:
            # technical interruption e.g. phone line / internet
            # show excuse message
            # terminate
            pass
        else:
            # really a pass, go ahead.
            # wait some secs, then show payment proceeded. 
            # update payment status - TODO needed a way to follow order/paym status.
            # prepare my pizza.
            # show my order
            # ahead to self.prepare_pizza()
            pass

        # raise unexpected point

        print("WE ARE AT PAYMENT PROCESS.\nCALL TERMINATE()\n"+" -"*20)
        for o in ORDERS:
            print(o)
        self.terminate()
        # sys.exit(0)
