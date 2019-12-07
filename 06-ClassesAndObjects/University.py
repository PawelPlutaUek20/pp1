class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = "Akademia Gorniczo Hutnicza"
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
        
uni = University()
uni.set_name("AGH")
uni.print_name()
uni.print_fullname()
uni.set_fullname("Akademia Górniczo-Hutnicza im. Stanisława Staszica w Krakowie")
uni.print_fullname()

