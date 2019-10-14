#6
# print(type(50))
# print(type('Janusz'))
# print(type(True))
# print(type(149.17))
# print(type(4*7))
# print(type(4.0*7))
# print(type(2>5))

#7
# print(5 + 10 * 5)
# print(3 - 2 + 1)
# print(2 + - 3)
# print(2 ** 8)
# print(4 + 4 / 2 ** 2)
# print(4 % 3 % 2 % 1)
# print(1 + (2 % (3 ** 4)) * 5)
# print(True != False)
# print(2 <= 3 or False)
# print(not True or not False and not True)
# print(2 < 3 and 4 < 5 or not 6 < 7)
# print(2 % 3 < 4 / 5 and 6 + 7 < 8 or not 9 + 10 == 19)
# print(0b11111 >> 1 >> 1 >> 1)
# print(0x11 + 0b11 + 11)
# print(2 << 3 >> 4)

#8
# print(15*38)
# print((3+4)*(5+9))
# print(7//2)
# print(48%5)
# print((8+7+4+2)/4)
# print(2**10)
# print(49**(1/2))
# print(25/100*80)

#9
# import random
# if x != 1:
#     for i in range(3):
#         print(random.uniform(0,1))
# import random
# if x!= 100:
#     for i in range(3):
#         print(random.randint(0,100))
# import random
# for i in range(3):
#     print(random.randint(5,10))
# import random
# x= ("karo", "kier", "pik", "trefl")
# for i in range(3):
#     print(random.choice(x))

#10
# x,y = 7,34
# z = x
# x = y
# y = z
# print(x)
# print(y)

#10.1
# x,y = 7,34
# x,y = y,x
# print(x)
# print(y)

#11
# liczba1 = 5
# liczba2 = 1
# liczba3 = 8
# liczba4 = 6
# liczba5 = 3
# 
# print(liczba1+liczba2+liczba3+liczba4+liczba5)
# print(liczba1**2+liczba2**2+liczba3**2+liczba4**2+liczba5**2)
# print(liczba3/liczba5)
# print(liczba1%liczba5)
# print((liczba1+liczba2)*(liczba4+liczba5))
# print(liczba1%3)
# print(liczba3 == liczba4)
# print(liczba3<<2)

#12
# uczelnia = "Uniwersytet Ekonomiczny w Krakowie"
# print(uczelnia)
# print(len(uczelnia))
# print(uczelnia[0])
# print(uczelnia[3:9])
# print("'"+uczelnia+"'")

#13
# imiona = ["Agata", "Sandra", "Wiktoria"]
# print(len(imiona))
# print(imiona[0])
# print(imiona[len(imiona)-1])

# 14
# liczby = [2,7,3,5]
# print(liczby[1])
# print(sum(liczby))
# print(len(liczby))
# print(liczby[-2])
# print(sum(liczby)/len(liczby))

# 15
# liczba=18
# print("Wartość liczby to {}, a {} to jej druga potęga".format(liczba, liczba**2))

# 16
# imie = "Pawel"
# lata = 18
# wzrost = 185
# print("Mam na imię {} i mam {} lat, a mój wzrost to {} cm".format(imie,lata,wzrost))

# 17
# kwota = 15.84
# VAT = 23/100
# print("Kwota: {} zł\nVAT 23%: {:.2f} zł".format(kwota, kwota*VAT))

#18
# x = input("Podaj swoje imie: ")
# y = input("Podaj swoje nazwisko: ")
# print(x, y)

#19
# x = int(input("Podaj liczbe calkowita: "))
# y = int(input("Podaj druga liczbe calkowita: "))
# print(x+y)

#20
# import math
# pi = math.pi
# r = float(input("Podaj promien kola: "))
# P = pi*r**2
# Obw = 2*pi*r
# print("Pole koła o promieniu {} wynosi {:.2f}".format(r,P))
# print("Obwód koła o promieniu {} wynosi {:.2f}".format(r,Obw))

#21
# Celsjusz = input("Podaj temperature w stopniach Celsjusza: ")
# Fahrenheit = (float(Celsjusz) * 1.8) + 32
# Kelvin = float(Celsjusz) + 273.15
# print(str(Celsjusz) + "°C" + " to " + str(Fahrenheit) + "°F i " + str(Kelvin) + "K")

#22
# a,b,c=3,4,5
# p = 1/2*(a+b+c)
# S = (p*(p-a)*(p-b)*(p-c))**(1/2)
# print(S)

#24
# cm = float(input("Podaj swoj wzrost: "))
# inch = cm/2.54
# ft=int(inch/12)
# rin=inch-ft*12
# print("Mam {:.0f} cm wzrostu, tj. {} stóp i {:.0f} cali.".format(cm,ft,rin))

#25
# x = int(input("Podaj nr rachunku bankowego: "))
# print(str(x)[:2] + " " + ' '.join(str(x)[i:i+4] for i in range(2, 26, 4)))

#26
# x = float(input("Podaj wzrost w cm: "))
# y = float(input("Podaj wagę w kg: "))
# z = y/x/x*10000
# if z>=18.5 and z<=24.9:
#     print("Wskaźnik BMI: {:.2f} (waga prawidłowa)".format(z))
# else:
#     print("Wskaźnik BMI: {:.2f} (waga nieprawidłowa)".format(z))

#27
# import math
# x = int(input("Podaj liczbe naturalna: "))
# y = int(input("Podaj druga liczbe naturalna: "))
# z = math.gcd(x,y)
# print("największy wspólny podzielnik liczb {} i {} jest liczba {}".format(x,y,z))

#28
# import random
# x = random.randint(1,6)
# y = random.randint(1,6)
# z = random.randint(1,6)
# suma = x+y+z
# print("Pierwsza kostka: {}\nDruga kostka: {}\nTrzecia kostka: {}\nSuma: {}".format(x,y,z,suma))

#29
# import random
# x = random.randint(1,6)
# y = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
# print("Komputer wyrzucił: " + str(x))
# print("Zgadłeś: "+ str(bool(x == y)))

#30
# x = [12,6,4,9,3]
# i=0
# while i<5:
#     print(str(x[i])+": "+str("*"*x[i]))
#     i+=1

