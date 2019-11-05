import re
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
srednia = 0
for i in cyfry:
    srednia += int(i)
print(srednia/len(cyfry))