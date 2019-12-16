import json
with open("euro.json") as file:
    data = json.load(file)

print("NBP – 10 ostatnich notowań EURO")
print()
print(f"%-13s %-9s %s" % ("Data", "Kupno", "Sprzedaż"))
print("="*32)
for i in range(len(data['rates'])):
    print(f"%-13s %-9s %s" % (data['rates'][i]['effectiveDate'], data['rates'][i]['bid'], data['rates'][i]['ask']))
