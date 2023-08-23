# Сохранить в файле таблицу квадратов и кубов целых чисел от 1 до 20
import csv

name = 'table.csv'
with open(name, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1, 21):
        writer.writerow([i, i**2, i**3])

with open(name, 'r') as file:
    reader = csv.reader(file)
    res = []
    for line in reader:
        res.append(line)
print(res)
