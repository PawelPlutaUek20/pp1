import csv
import statistics
with open('employees.csv', newline='') as f:
    x=1
    wiek=[]
    reader = csv.reader(f)
    print('#   ',end='')
    for row in next(reader):
        print(f'%-15s'%row.upper(), end='')
    print('')
    print('='*80)
    for row in reader:
        print(f'%-3d %-14s %-14s %-14s %s'%(x, row[1], row[0].upper(), row[2], row[3]))
        x+=1
        wiek.append(int(row[2]))
    print('\nSrednia arytmetyczna wieku pracownikow wynosi:', end=' ')
    print(statistics.mean(wiek))