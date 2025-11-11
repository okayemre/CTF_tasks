from pprint import pprint

# Task 1: Log Analysis and Statistics Extraction

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

print("\n1.Task Start\n")
print(aktionen)
print(len(aktionen))
print("\n1.Task Finish\n")


# 2. Erstelle eine Übersicht (Dictionary), welche Benutzer-ID wie viele verschiedene Aktionen durchgeführt hat. Beispiel: { 'user_001': 3, 'user_002': 2, ... }.
zahl_user = {}
for entry in log_eintraege:
    username = entry[0]  # erstes Element des Tupels ist der Benutzername
    zahl_user[username] = zahl_user.get(username, 0) + 1

print("\n2.Task Start\n")
print(f"Anzahl der jeweiligen User im log_eintraege: {zahl_user}")
print("\n2.Task Finish\n")

# 3. Identifiziere die Top 3 Aktionen basierend auf ihrer Gesamthäufigkeit. Gib diese Aktionen zusammen mit ihrer Häufigkeit zurück.
import math

zahl_actionen = {}
for action in log_eintraege:
    action_1 = action[1]  # erstes Element des Tupels ist der Benutzername
    zahl_actionen[action_1] = zahl_actionen.get(action_1, 0) + 1


from collections import Counter

zahl_actionen = Counter(entry[1] for entry in log_eintraege)
top_3_actionen = zahl_actionen.most_common(3)

print("\n3.Task Start")
print(f"Top 3 Actonen: {top_3_actionen}")
print("3.Task Finish\n")

# 4. Finde alle Benutzer-IDs, die sowohl die Aktion 'Login' als auch 'Logout' durchgeführt haben.

login_logout_ids = []
login_ids = []
logout_ids = []


for user_id, action, _ in log_eintraege:
    if action == "Login":
        login_ids.append(user_id)
    elif action == "Logout":
        logout_ids.append(user_id)

login_logout_ids = set(login_ids) & set(logout_ids)

pprint(login_ids)
pprint(logout_ids)
pprint(login_logout_ids)
