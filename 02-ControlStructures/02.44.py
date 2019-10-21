#44
x=int(input("Podaj limit predkosci (km/h): "))
y=int(input("Podaj prędkość pojazdu (km/h): "))
if y-x <= 10:
    print("Mandat (zł): {}".format((y-x)*5))
else:
    print("Mandat (zł): {}".format(50+(y-x-10)*15))