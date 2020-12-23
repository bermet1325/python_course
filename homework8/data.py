

import csv

def csv_read(file):
    reader = csv.reader(file)

    for row in reader:
        print(" ".join(row))


csv_path = "data.csv"
with open(csv_path,  "r") as file:
    csv_read(file)


print("-----------------------------------------------------")

def to_csv_writer(data, path):
    with open(path, "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter= ",")
        for line in data:
            csv_writer.writerow(line)


data = [" username,   email,                  ip_address ".split(";"),
        " root,       root@example.com,       192.168.0.1 ".split(";"),
        " admin,      admin@example.com,      192.168.0.2 ".split(";"),
        " test_user,  test_user@example.com,   192.168.0.3 ".split(";"),
        " second_user,second_user@example.com, 192.168.0.4 ".split(";")]

path = "output.csv"
to_csv_writer(data, path)

def csv_reader(file, delimiter=","):
    reader = csv.DictReader(file, delimiter=delimiter)
    for line in reader:
         print(line)



csv_path = "data.csv"

with open(csv_path, "r") as file:
    csv_reader(file, ",")

