class University:
    
    def __init__(self):
        self.fullname = "Akademia Gorniczo Hutnicza"
        
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
        
uni = University()
uni.print_fullname()
uni.set_fullname("Akademia Górniczo-Hutnicza im. Stanisława Staszica w Krakowie")
uni.print_fullname()