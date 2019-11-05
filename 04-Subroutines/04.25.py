imiona=['Janek','Ania','Wojtek','Zosia']
def jestimie(imie,imiona):
    if imie in imiona:
        return 'jest'
    else:
        return 'nie jest'
imie=input('Podaj imie: ')
jestimie(imie, imiona)
print('Imiona:',end=' ')
print(*imiona, sep=' ')
print('Imie:',imie)
print('Rezultat: imię {} zawarte w wykazie imion'.format(jestimie(imie,imiona)))
