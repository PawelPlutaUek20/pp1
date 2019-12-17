import json

Euro = {
    "table": "C",
    "currency": "euro",
    "code": "EUR",
    "rates": [
        {
            "no": "233/C/NBP/2019",
            "effectiveDate": "2019-12-03",
            "bid": 4.2447,
            "ask": 4.3305
        },
        {
            "no": "234/C/NBP/2019",
            "effectiveDate": "2019-12-04",
            "bid": 4.2389,
            "ask": 4.3245
        },
        {
            "no": "235/C/NBP/2019",
            "effectiveDate": "2019-12-05",
            "bid": 4.2349,
            "ask": 4.3205
        },
        {
            "no": "236/C/NBP/2019",
            "effectiveDate": "2019-12-06",
            "bid": 4.2334,
            "ask": 4.3190
        },
        {
            "no": "237/C/NBP/2019",
            "effectiveDate": "2019-12-09",
            "bid": 4.2412,
            "ask": 4.3268
        },
        {
            "no": "238/C/NBP/2019",
            "effectiveDate": "2019-12-10",
            "bid": 4.2392,
            "ask": 4.3248
        },
        {
            "no": "239/C/NBP/2019",
            "effectiveDate": "2019-12-11",
            "bid": 4.2473,
            "ask": 4.3331
        },
        {
            "no": "240/C/NBP/2019",
            "effectiveDate": "2019-12-12",
            "bid": 4.2434,
            "ask": 4.3292
        },
        {
            "no": "241/C/NBP/2019",
            "effectiveDate": "2019-12-13",
            "bid": 4.2418,
            "ask": 4.3274
        },
        {
            "no": "242/C/NBP/2019",
            "effectiveDate": "2019-12-16",
            "bid": 4.2281,
            "ask": 4.3135
        }
    ]
}

with open('euro.json', 'w') as f:
    json.dump(Euro, f, indent=4)

with open("euro.json") as file:
    data = json.load(file)

print("NBP – 10 ostatnich notowań EURO")
print()
print(f"%-13s %-9s %s" % ("Data", "Kupno", "Sprzedaż"))
print("="*32)
for i in range(len(data['rates'])):
    print(f"%-13s %-9s %s" % (data['rates'][i]['effectiveDate'], data['rates'][i]['bid'], data['rates'][i]['ask']))