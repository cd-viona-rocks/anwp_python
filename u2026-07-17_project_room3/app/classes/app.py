from datetime import datetime
import sys
import pandas as pd

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
        print(SEPARATOR + "  starting system.  " + SEPARATOR + "\n\n")
        self.log_event("system starts.")

        # load some clients, employees, delivery people as instantiated object
        self.kunden = []
        self.mitarbeiter = []
        self.lieferanten = []

        self.user_classes = []

        self.hashes = []

    def run(self):
        """runnable methods for execution."""

        user_class = self.screen_initial()
        self.user_login(user_class)



    def terminate(self):
        print(SEPARATOR + "\n  closing system.  \n" + SEPARATOR)
        self.log_event("system closes.")
        sys.exit(0)

    def log_event(self, event_description: str) -> None:
        log_time = datetime.now().timestamp()
        LOG.append({"timestamp":log_time, "description":event_description})
        # print(f"LOG at {log_time}: {event_description}")

    # screen methods

    def print_option_list(self, title: str, option_list: dict) -> None:
        msg = " "*4 + f"{title}:\n" + " "*4 + " -"*16 + "\n"
        for k,v in option_list.items():
            msg += " "*4 + f"{k}: {v}\n"
        print(msg)

    def screen_initial(self) -> int:
        counter = 0
        user_class = 0
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
                    break                       
                elif o in [1,2,3]:
                    print("\n" + " "*4 + f"Weiter zur Anmeldung als {options[o]}\n")
                    break
                else:
                    raise
            except:
                print("\n" + " -"*20 + "\n\nIhre Option muss einer davon sein: 1, 2, 3 oder 0 um abzubrechen.\n")

        if o == 0:
            self.terminate() 

        return user_class
            


    # people methods

    def load_all_people(self) -> None:
        """loads some pre defined people from people.csv,
         separate them into clients, employees and deliveries;
         and save hashes for client login at password.csv
         
         the csv files should be seen as a possible extension for DB see file: 
         Aufgabenstellung, 3.3. Optional / Exweiterung: EX003 and EX004
         """
        df_people = pd.read_csv("people.csv")

        # for the three instantiations under, use the following method:
        # 1. select the desired columns
        # 2. filter the dataframe and convert it as a list of dictionaries
        # 3. instantiate it as a list compreehnsion for object attribute

        # - - - user class [ client | employee | delivery ] - - -
        df_user_classes = df_people[["id", "class"]]
        self.user_classes = df_user_classes.to_dict(orient="records")

        # - - - clients - - -
        df_clients = df_people[df_people["class"] == "client"]
        df_clients["client_number"] = df_clients["id"]
        
        cols = Person.PERMITTED_ATTR.append("client_number")
        df_clients = df_clients[cols]
        kwargs_clients = df_clients.to_dict(orient="records")

        self.kunden = [Kunde(**kwargs) for kwargs in kwargs_clients]
        self.log("clients loaded")

        df_pw_db = pd.read_csv("password_hashes.csv")
        self.hashes = df_pw_db[["user_id", "password_hash"]].to_dict(orient="records")
        self.log("password hashes loaded")


        # - - - employees - - -
        df_emplo = df_people[df_people["class"] == "employee"]
        df_emplo["employee_number"] = df_emplo["id"]
        
        cols = Person.PERMITTED_ATTR.append("employee_number")
        df_emplo = df_emplo[cols]
        kwargs_emplo = df_emplo.to_dict(orient="records")

        self.mitarbeiter = [Mitarbeiter(**kwargs) for kwargs in kwargs_emplo]
        self.log("employees loaded")


        # - - - delivery - - -
        df_deliv = df_people[df_people["class"] == "delivery"]
        df_deliv["employee_number"] = df_deliv["id"]
        
        cols = Person.PERMITTED_ATTR.append("city")
        df_deliv = df_deliv[cols]
        kwargs_clients = df_deliv.to_dict(orient="records")

        self.lieferanten = [Lieferant(**kwargs) for kwargs in kwargs_clients]
        self.log("deliveriy people loaded")


    def user_login(self, user_class: int) -> bool:
        counter = 0
        response = False
        msg = "\n" + " "*4 + "Bitte geben Sie Ihren Benutzername und Passwort Kommagetrennt"
        msg += "\n" + " "*4 + "e.g. maxsupermustermann, banana1234 oder <Enter> zu Abbrechen."
        while True:
            counter += 1
            if counter > 5:
                raise InterruptedError("tries exceeded. app execution interrupted.")
            try:
                print(SEPARATOR + msg)
                user_data = input("\n" + " "*4 + "Geben Sie Ihre Logindaten ein: ")
                user, pw = [x.strip() for x in user_data.split(",")]
                print(user, len(user))
                print(pw,len(pw))
                # CONTINUE FROM HERE
                # CONTINUE FROM HERE
                # CONTINUE FROM HERE
                # CONTINUE FROM HERE
                # CONTINUE FROM HERE
                # CONTINUE FROM HERE
                break
            except:
                c2 = 0
                while True:
                    c2 += 1
                    if c2 > 5:
                        raise InterruptedError("tries exceeded. app execution interrupted.")
                    try:
                        title = "\n" + " "*4 + "Möchten Sie zurück zur Optionen oder nochmal versuchen"
                        options = {0: "zurück zur Menu Optionen.", 1: "nochmal versuchen, die Benutzername und Passwort einzugeben."}
                        self.print_option_list(title, options)
                        o = int(input("\n" + " "*4 + "Geben Sie den passenden Wert ein: "))
                        if o == 0:
                            self.screen_initial()
                        break
                    except:
                        pass

        return user_class

        return response
    