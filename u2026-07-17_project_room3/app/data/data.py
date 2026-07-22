# Enumerations with permitted values for assignment

# Possible extension for multi language app: make the value a list or an obj
# e.g. 0: "bestellt" -> 0: {"DE": "bestellt", "EN": "ordered"}

# Another possible extension is the declaration of constant list values as
# an enumeration. Then use from enum import Enum. See https://docs.python.org/3/library/enum.html


# PERMITTED ORDER STATUS FOR REFERENCE
ORDER_STATUS = {
    0:"bestellt",
    1:"bestätigt",
    2:"in Zulieferung",
    3:"zugestellt",
}


# PERMITTED PAYMENT STATUS FOR REFERENCE
PAYMENT_STATUS = {
    0:"nicht bezahlt",
    1:"in bezahlung",
    2:"bezahlt",
    3:"storniert",
}

# - - - PIZZA MENU / Skizze einer Pizza Datenbank - - -

PIZZAS = [
    {"id": 10, "name":"Margherita", "size":"M", "price": 6.50, "currency":"EUR"},
    {"id": 20, "name":"Salami", "size":"M", "price": 7.50, "currency":"EUR"},
    {"id": 30, "name":"Funghi", "size":"M", "price": 7.90, "currency":"EUR"},
    {"id": 40, "name":"Quattro Stagioni", "size":"G", "price": 9.50, "currency":"EUR"},
    {"id": 50, "name":"Diavola", "size":"G", "price": 8.90, "currency":"EUR"},
]

# - - - Skizze einer Bestellungsdatenbank - - - 

# Bestellungen
# {client_id: str, pizza_id: str[], order_status: str, payment_status: str}
ORDERS = []
