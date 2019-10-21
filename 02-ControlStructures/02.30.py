#30
PIN = "0805"
turns = 0
while turns < 3:
    x = input("Podaj kod PIN: ")
    if x == PIN:
        print("Kod PIN poprawny.")
        break
    elif x != PIN:
        print("Kod PIN niepoprawny.")
    turns += 1
else:
    print("Karta ppłatnicza zostaje zablokowana.")
