#29
import random
x = random.randint(1,6)
y = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
print("Komputer wyrzucił: " + str(x))
print("Zgadłeś: "+ str(bool(x == y)))