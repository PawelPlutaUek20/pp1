class Plane():
    def __init__(self, name):
        self.name = name
        self.hight = 0
        self.is_flying = False
        
    def set_initial_hight(self, new_hight):
        self.is_flying = True
        if self.hight == 0 and new_hight in range(1000,2001):
            self.hight = new_hight
            
    def increase_hight(self, increase_hight):
        if self.is_flying == True:
            if increase_hight in range(300,11001):
                self.hight += increase_hight
            else:
                print("Petition denied")
            
    def decrease_hight(self, decrease_hight):
        if self.is_flying == True:
            if decrease_hight in range(300,11001) and self.hight-decrease_hight > 0:
                self.hight -= decrease_hight
            else:
                print("Petition denied")
            
    def landing(self):
        if self.is_flying == True:
            if self.hight in range(500):
                self.hight = 0
                self.is_flying = False
            else:
                print("You are too hight to land properly")
    def information(self):
        print(f"Tu {self.name}, moja wysokosc lotu to {self.hight}m")
        
lot = Plane("LOT881")
lot.set_initial_hight(2000)
lot.information()
lot.increase_hight(6900)
lot.information()
lot.decrease_hight(8700)
lot.information()
lot.landing()
lot.information()