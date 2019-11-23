from dane import pobierzDane
from obliczenia import srednia, mediana, maksimum, minimum
miesiace=['styczen','luty','marzec','kwiecien','maj','czerwiec']
dane = pobierzDane()
def pokazWyniki():
    print('RAPORT Z WYDATKOW')
    print(f'%s %14s'%('MIESIAC', 'WYDATKI'))
    for i in range(len(miesiace)):
        print(f'%-9s %12s'%(miesiace[i], '%.2f'%dane[i]))
    print('\n')
    
    print('STATYSTYKA WYDATKOW')
    nazwyStatystyk=['srednia', 'mediana', 'minimum', 'maksimum']
    statystyki=[srednia(), mediana(), minimum(), maksimum()]
    for i in range(len(nazwyStatystyk)):
        statystyki[i] = '%.2f'%statystyki[i]
        print(f'%-9s %12s'%(nazwyStatystyk[i], statystyki[i]))

def pokazWykres():
    print('GRAFICZNA REPREZENTACJA WYDATKÓW')
    for i in range(len(miesiace)):
        graph = '#'*(int(dane[i])//120)
        print(f'%-9s %-5s'%((str(miesiace[i])+':'), graph))