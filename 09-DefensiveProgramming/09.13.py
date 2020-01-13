cena_netto = 15
assert cena_netto > 0 and (type(cena_netto) == int or type(cena_netto) == float)
cena_brutto = cena_netto * 1.23
print("{:.2f} zł".format(cena_brutto))
