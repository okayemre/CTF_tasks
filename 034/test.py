from pprint import pprint

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

userid_list = []
actionen_list = []
actionen_list_mit_anzahl = {}


for user_id, action, date in log_eintraege:
    userid_list.append(user_id)
    actionen_list.append(action)
    actionen_list_mit_anzahl[action] = actionen_list_mit_anzahl.get(action, 0) + 1

pprint(actionen_list_mit_anzahl)

pprint(sorted(actionen_list_mit_anzahl.values()))
