import statistics
import csv
age=[]
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    for row in next(reader):
        pass
    for row in reader:
        age.append(int(row[2]))
    print("Srednia arytmetyczna:", statistics.mean(age))
    print("Mediana:", statistics.median(age))
    print("Odchylenie standardowe:", f'%.1f'%statistics.stdev(age))