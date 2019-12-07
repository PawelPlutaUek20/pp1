class University:
    
    def __init__(self):
        self.name = "UEK"
        
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name
        
uni = University()
uni.set_name("AGH")
uni.print_name()