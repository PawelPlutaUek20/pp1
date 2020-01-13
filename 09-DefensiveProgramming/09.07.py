wzrost = int(input("Podaj wzrost w cm: "))
assert wzrost in range(150,221) and type(wzrost) == int
waga = float(input("Podaj wage w kg: "))
assert type(waga) == float and waga <= 150.0 and waga >= 40.0
BMI = waga/((wzrost/100)**2)
print(BMI)