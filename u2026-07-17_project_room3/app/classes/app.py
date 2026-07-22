from datetime import datetime
import sys
from pathlib import Path
import pandas as pd

from hashlib import pbkdf2_hmac
from hmac import compare_digest
from base64 import b64decode  # b64encode when create hashes to save

from data.data import *
from data.log import LOG

from classes.person import Person
from classes.kunde import Kunde
from classes.mitarbeiter import Mitarbeiter
from classes.lieferant import Lieferant

SEPARATOR = "\n" + " ="*20 + "\n"

class App:
    """implements the activity diagram and update states"""
    
    def __init__(self):
        # load some clients, employees, delivery people as instantiated object
        self.kunden = []
        self.mitarbeiter = []
        self.lieferanten = []

        self.user_classes = []

        self.hashes = []

    def run(self):
        """runnable methods for execution."""

        print(SEPARATOR + "  starting system.  " + SEPARATOR)
        self.log_event("system starts.")

        self.load_all_people()

        # ONLY FOR TESTS
        msg = f"\ntry this examples:\n{self.kunden[0]}\n{self.mitarbeiter[0]},\n{self.lieferanten[0]}\n"
        print(msg)

        user_class = self.screen_initial()
        response = self.user_login(*user_class)

        # ONLY FOR TESTS
        print(f"response from login: {response}")




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


    # people methods

    def load_all_people(self) -> None:
        """loads some pre defined people from people.csv,
         separate them into clients, employees and deliveries;
         and save hashes for client login at password.csv
         
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

    def print_option_list(self, title: str, option_list: dict) -> None:
        msg = " "*4 + f"{title}:\n" + " "*4 + " -"*16 + "\n"
        for k,v in option_list.items():
            msg += " "*4 + f"{k}: {v}\n"
        print(msg)

    def screen_initial(self) -> int:
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
        
        if o == 0:
            self.terminate() 

        return (o,options[o]) 


    def user_login(self, user_class: int, user_mode: str) -> bool:
        o, user_name, user_pw = -1, None, None
        options = {}

        c1 = 0
        response = False

        # - - - menu context - - -

        msg = "\n" + " "*4 + f"Sie sind innerhalb des Kontextes: {user_class} - {user_mode}"
        msg += "\n" + " "*4 + " -"*20
        msg += "\n" + " "*4 + "Bitte geben Sie Ihren Benutzername und Passwort Kommagetrennt"
        msg += "\n" + " "*4 + "e.g. maxsupermustermann, banana1234 oder <Enter> zu Abbrechen."

        stop1, stop2 = False, False
        while not stop1:
            c1 += 1
            if c1 > 5:
                raise InterruptedError("tries exceeded. app execution interrupted.")
            try:
                print(SEPARATOR + msg)
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
                print("\n" + " -"*4 + " "*4 + str(e) +" "*4 + " -"*4 + "\n")
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
                            stop1 = True
                            stop2 = True
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

        print(f"o: {o}, user_class: {user_class}")
        if user_class == 1:
            database = self.kunden
        elif user_class == 2:
            database = self.mitarbeiter
        elif user_class == 3:
            database = self.lieferanten
        else:
            raise ValueError("invalid value for user_data within login context.")

        # print(f"len database: {len(database)}\ne.g. database: {database[0]}")

        user = list(filter(lambda x: x["name"] == user_name, database))
        if len(user) != 1:
            raise ValueError("user data not found.")
        user = user[0]

        hash = list(filter(lambda x: x["user_id"] == user["id"], self.hashes))
        if len(hash) != 1:
            raise ValueError("user password hash not found.")
        hash = hash[0]

        # print(user,hash)
        # sys.exit(0)        

        hash_salt = hash["salt"]
        hash_iter = hash["iter"]
        hash_saved = hash["password_hash"]

        # * * * PLEASE NOT, THAT A TABLE USER (as our people.csv) NEVER MUST SAVE THE PASS * * * 
        # * * * THE PASS IS PRIVATE FOR THE USER. WE SAVE PW FOR EDUCATIONAL USE ! ! ! * * * 
        # derived = pbkdf2_hmac(
        #     "sha256", 
        #     user_pw.encode("utf-8"), 
        #     hash_salt, 
        #     hash_iter
        # )
        # if hash_saved == f"pbkdf2_sha256${hash_iter}${hash_salt.hex()}${derived.hex()}":
        #     response = True    

        # import base64, hashlib, hmac

        # salt_b64 = saved_salt_b64   # from storage (string)
        # iters = saved_iters
        b64_hash = b64decode(hash_saved)
        b64_salt = b64decode(hash_salt)  # <-- back to bytes

        attempt_hash = pbkdf2_hmac("sha256", user_pw.encode(), b64_salt, hash_iter)

        if compare_digest(attempt_hash, b64_hash):
            print("ok")
       

        return response
    