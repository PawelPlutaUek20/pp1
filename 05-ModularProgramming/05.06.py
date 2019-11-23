import csv
j=1
a=[]
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    print('#     ', end='')
    for i in next(reader):
        if i == 'age':
            print('%-8s'%i.upper(), end='')
        else:
            print('%-16s'%i.upper(), end='')
    print('\n',end='')
    print('='*75)
    for row in reader:
        print('%-2s'%j, end='    ')
        j+=1
        print('%-15s %-15s %-7s %s'%(row[1], row[0].upper(), row[2], row[3]))
        a.append(int(row[2]))
print(f'\n\nSrednia arytmetyczna wieku pracowników wynosi: {sum(a)/len(a)}')