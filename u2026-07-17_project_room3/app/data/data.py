PIZZAS = [
    {"id": 10, "name":"Margherita", "size":"M", "price": 6.50, "currency":"EUR"},
    {"id": 20, "name":"Salami", "size":"M", "price": 7.50, "currency":"EUR"},
    {"id": 30, "name":"Funghi", "size":"M", "price": 7.90, "currency":"EUR"},
    {"id": 40, "name":"Quattro Stagioni", "size":"G", "price": 9.50, "currency":"EUR"},
    {"id": 50, "name":"Diavola", "size":"G", "price": 8.90, "currency":"EUR"},
]


# PERMITTED ORDER STATUS FOR REFERENCE
ORDER_STATUS = [
    "bestellt",
    "bestätigt",
    "in Zulieferung",
    "zugestellt"
]


# PERMITTED PAYMENT STATUS FOR REFERENCE
PAYMENT_STATUS = [
    "bezahlt",
    "nicht bezahlt",
]

# Bestellungen
# {client_id: str, pizza_id: str[], order_status: str, payment_status: str}
ORDERS = []


CLIENTS = [
    {"id":"1001", "first_name": "Max", "last_name": "Mustermann", "age": 32, "address": "main str 123, Big City"},
    {"id":"1002", "first_name": "Maria", "last_name": "Musterfrau", "age": 26, "address": "farm str 123, Green Village"},
    {"id":"1003", "first_name": "Diana", "last_name": "de Temiscira", "age": 5000, "address": "Temiscira Island"},
]

