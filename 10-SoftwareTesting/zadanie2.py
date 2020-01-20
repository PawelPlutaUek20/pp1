class Miasto:
    def __init__(self, nazwa, populacja):
        self.nazwa = nazwa
        self.populacja = populacja
    def __str__(self):
        return f"{self.nazwa},{self.populacja}"

m1 = Miasto("Zakopane",27000)
m2 = Miasto("Gdynia", 246000)
print(m1)
print(m2)
