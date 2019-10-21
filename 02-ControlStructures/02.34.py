#34
x = str(input("Podaj Pesel: "))
if int(x[9])%2==0:
    print("Płeć: kobieta")
else:
    print("Płeć: mężczyzna")
if int(x[:2])>18:
    print("Wiek: "+str(2018-(1900+int(x[:2]))))
elif int(x[:2])<=18 and int(x[:2])>=0:
    print("Wiek: "+str(2018-(2000+int(x[:2]))))
