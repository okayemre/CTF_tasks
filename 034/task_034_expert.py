from pprint import pprint

# Aufgabe 1: Log-Analyse und Statistik-Extraktion

log_eintraege = [
    ("user_001", "Login", "2023-10-26 09:00:00"),
    ("user_002", "ProductView", "2023-10-26 09:01:15"),
    ("user_001", "ProductView", "2023-10-26 09:02:30"),
    ("user_003", "Login", "2023-10-26 09:03:00"),
    ("user_002", "AddToCart", "2023-10-26 09:04:00"),
    ("user_001", "Logout", "2023-10-26 09:05:00"),
    ("user_004", "Login", "2023-10-26 09:06:00"),
    ("user_003", "ProductView", "2023-10-26 09:07:00"),
    ("user_002", "ProductView", "2023-10-26 09:08:00"),
    ("user_001", "AddToCart", "2023-10-26 09:09:00"),
    ("user_004", "AddToCart", "2023-10-26 09:10:00"),
    ("user_003", "Logout", "2023-10-26 09:11:00"),
    ("user_005", "Login", "2023-10-26 09:12:00"),
    ("user_002", "Logout", "2023-10-26 09:13:00"),
    ("user_001", "Login", "2023-10-26 09:14:00"),
    ("user_005", "ProductView", "2023-10-26 09:15:00"),
    ("user_001", "Logout", "2023-10-26 09:16:00"),
    ("user_002", "Login", "2023-10-26 09:17:00"),
    ("user_004", "ProductView", "2023-10-26 09:18:00"),
    ("user_002", "ProductView", "2023-10-26 09:19:00"),
    ("user_001", "ProductView", "2023-10-26 09:20:00"),
]
# 1. Ermittle die Anzahl der eindeutigen Aktionen, die über alle Log-Einträge hinweg durchgeführt wurden.

aktionen = set()

for _, action, _ in log_eintraege:
    aktionen.add(action)

print("\n**************1.1.Task Start**************\n")
pprint(f"Eindeutigen Aktionen: {aktionen}")
print(f"Anzah von Eindeutigen Aktionen: {len(aktionen)})")
print("\n**************1.1.Task Finish**************\n\n")


# 2. Erstelle eine Übersicht (Dictionary), welche Benutzer-ID wie viele verschiedene Aktionen durchgeführt hat. Beispiel: { 'user_001': 3, 'user_002': 2, ... }.
anzahl_user_id = {}

for entrag in log_eintraege:
    user_id = entrag[0]
    anzahl_user_id[user_id] = anzahl_user_id.get(user_id, 0) + 1

print("\n**************1.2.Task Start**************\n")
print(f"Anzahl der jeweiligen User im log_eintraege: {anzahl_user_id}")
print("\n**************1.2.Task Finish**************\n\n")

# 3. Identifiziere die Top 3 Aktionen basierend auf ihrer Gesamthäufigkeit. Gib diese Aktionen zusammen mit ihrer Häufigkeit zurück.
anzahl_actionen = {}

for _, action, _ in log_eintraege:
    anzahl_actionen[action] = anzahl_actionen.get(action, 0) + 1

sorted_actionen = sorted(anzahl_actionen.items(), key=lambda x: x[1], reverse=True)
top_3_actionen = sorted_actionen[0:3]

print("\n**************1.3.Task Start**************\n")
print(f"Top 3 Actonen: {top_3_actionen}")
print("\n**************1.3.Task Finish**************\n\n")

# 4. Finde alle Benutzer-IDs, die sowohl die Aktion 'Login' als auch 'Logout' durchgeführt haben.

login_logout_ids = []
login_ids = []
logout_ids = []


for entrag, action, _ in log_eintraege:
    if action == "Login":
        login_ids.append(entrag)
    elif action == "Logout":
        logout_ids.append(entrag)

login_logout_ids = set(login_ids) & set(logout_ids)

print("\n**************1.4.Task Start**************\n")
pprint(login_ids)
pprint(logout_ids)
pprint(login_logout_ids)
print("\n**************1.4.Task Finish**************\n\n")


# Aufgabe 2: Bestandsverwaltung für ein Lagerhausnetzwerk

# add_product(warehouse_name, product_details): Adds a new product to a specific warehouse. product_details is a dictionary with {'sku': 'P001', 'name': 'Laptop', 'price': 1200.0, 'quantity': 10}. If the product (identified by sku) already exists in the warehouse, only the quantity should be updated accordingly (i.e., the new quantity is added to the existing quantity).

product_details_list = {}

example_details_list = {
    "sku": "P001",
    "name": "Laptop",
    "price": 1200.0,
    "quantity": 10,
}

warehouse_names = [
    "Berlin_Central",
    "Hamburg_South",
    "Munich_North",
    "Stuttgart_West",
    "Frankfurt_East",
    "Cologne_Main",
    "Dresden_Hub",
    "Leipzig_Storage",
    "Dortmund_Logistics",
    "Nuremberg_Distribution",
]

warehouses = {
    "Berlin_Central": {"location": "Berlin", "products": {}},
    "Hamburg_South": {"location": "Hamburg", "products": {}},
}


def add_product(warehouse_name, product_details):
    if warehouse_name not in warehouse_names:
        print(f"Warehouse not found: {warehouse_name}")
        return False

    products = warehouses[warehouse_name]["products"]

    sku = product_details["sku"]

    if sku in products:
        products[sku]["quantity"] += product_details["quantity"]
    else:
        products[sku] = product_details.copy()

    return True


add_product(
    "Berlin_Central", {"sku": "P001", "name": "Laptop", "price": 1200.0, "quantity": 10}
)

add_product(
    "Berlin_Central", {"sku": "P001", "name": "Laptop", "price": 1200.0, "quantity": 5}
)

add_product(
    "Hamburg_South", {"sku": "P002", "name": "Mouse", "price": 25.0, "quantity": 50}
)


print("\n**************2.1.Task Start**************\n")
print(warehouses)
print("\n**************2.1.Task Finish**************\n\n")


# add_product(warehouse_name, product_details): Belirli bir depoya yeni bir ürün ekler. product_details, {'sku': 'P001', 'name': 'Laptop', 'price': 1200.0, 'quantity': 10} içeren bir sözlüktür. Ürün (sku ile tanımlanır) depoda zaten mevcutsa, sadece miktar buna göre güncellenmelidir (yani, yeni miktar mevcut miktara eklenir).
