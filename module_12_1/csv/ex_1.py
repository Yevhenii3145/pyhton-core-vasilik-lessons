import csv

# newline='\n' - замена python переведения на новую строку
with open("names.csv", "w", newline="\n") as csvfile:
    field_names = ["first_name", "last_name"]

    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({"first_name": 'Tony', "last_name": 'Stark'})
    writer.writerow({"first_name": 'Bob', "last_name": 'Smitt'})
    writer.writerow({"first_name": 'Alice', "last_name": 'Stark'})

with open("names.csv") as file:
    print(file.read())
# first_name,last_name
# Tony,Stark
# Bob,Smitt
# Alice,Stark
