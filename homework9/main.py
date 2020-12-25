import datetime
import json

z = [
    {"Id": 1, "username": "admin",       "email": "admin@example.com",       "registered_at": datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")},
    {"Id": 2, "username": "first_user",  "email": "first_user@example.com",  "registered_at": datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")},
    {"Id": 3, "username": "second_user", "email": "second_user@example.com", "registered_at": datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}

]







with open("json_file", "w") as file:
    json.dump(z, file)

with open("json_file") as file:
    print(json.load(file))