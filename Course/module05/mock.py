import csv

from faker import Factory
from random import randint
from pprint import pprint

fake =  Factory.create('uk_UA')
USER_TABLE = 'data/users.csv'
amount = int(input("Count:"))
users: list[dict] = []

for _ in range(amount):
    user = {}
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = fake.random_int(min=5, max=60, step=3)
    phone = fake.phone_number()
    email = fake.email()
    user ={"first_name":f_name,
            "last_name": l_name,
            "age": age,
            "phone": phone,
            "email": email
            }
    users.append(user)

# pprint(users)

#  write to csv
with open(USER_TABLE, 'w', encoding="utf-8", newline='') as csvFile:
    fieldnames = list(users[0].keys())
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)
    print("Table saved")

# read csv
with open(USER_TABLE,  encoding="utf-8", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    info = [list(row.values()) for row in reader]
    # info = list(reader)
    pprint(info)