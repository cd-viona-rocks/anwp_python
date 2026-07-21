from datetime import datetime
import pandas as pd
print("print1")

from data.data import *
from data.log import LOG
print("print2")

from classes.person import Person
from classes.kunde import Kunde
from classes.mitarbeiter import Mitarbeiter
from classes.lieferant import Lieferant
print("print3")

class App:
    """implements the activity diagram and update states"""
    print("print4. class read") 
    
    def __init__(self):
        print(" ="*10 + "\n  starting system.  \n" + " ="*10)
        self.log_event("system starts.")

        # load some clients, employees, delivery people as instantiated object
        self.kunden = []
        self.mitarbeiter = []
        self.lieferanten = []

        self.hashes = []

    def run(self):
        """runnable method for execution."""
        pass

    def terminate(self):
        print(" ="*10 + "\n  closing system.  \n" + " ="*10)
        self.log_event("system closes.")

    def log_event(self, event_description: str) -> None:
        log_time = datetime.now().timestamp()
        LOG.append(log_time, event_description)
        print(f"LOG at {log_time}: {event_description}")

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


    def login_client(self, client: Kunde) -> bool:
        return False
    
