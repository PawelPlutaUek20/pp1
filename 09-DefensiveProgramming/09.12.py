wiek = 19
if type(wiek) != int:
 raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek <= 0 or wiek >= 120:
    raise TypeError("Wiek powinin być liczbą dodatnią, mniejszą od 120")
print(f'Masz {wiek} lat')