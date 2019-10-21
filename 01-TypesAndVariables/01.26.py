#26
x = float(input("Podaj wzrost w cm: "))
y = float(input("Podaj wagę w kg: "))
z = y/x/x*10000
if z>=18.5 and z<=24.9:
    print("Wskaźnik BMI: {:.2f} (waga prawidłowa)".format(z))
else:
    print("Wskaźnik BMI: {:.2f} (waga nieprawidłowa)".format(z))