class Phone:
    def __init__(self):
        self.bettery = 100
        self.volume = 0
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
        
p = Phone()
p.turn_on()
p.turn_off()