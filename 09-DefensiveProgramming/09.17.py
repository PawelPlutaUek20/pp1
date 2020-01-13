number = int(input("Podaj liczbową reprezentację dnia tygodnia: "))
assert number in range(1,8) and type(number) == int
days = ["monday", "tuesday", "wednesday",  "thursday", "friday", "saturday", "sunday"]
print(days[number-1].capitalize())
