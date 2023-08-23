import csv

FILENAME = 'users.csv'

users = [
    {'name': 'Bob', 'age': 22, 'sex': 'male'},
    {'name': 'Alice', 'age': 21, 'sex': 'female'},
    {'name': 'Иван', 'age': 22, 'sex': 'male'}
]

with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'])
        print(row)
# Bob
# {'name': 'Bob', 'age': '22', 'sex': 'male'}
# Alice
# {'name': 'Alice', 'age': '21', 'sex': 'female'}
# Иван
# {'name': 'Иван', 'age': '22', 'sex': 'male'}
