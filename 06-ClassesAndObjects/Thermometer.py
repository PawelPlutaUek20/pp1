import random
class Thermometer():
    def __init__(self):
        self.temperature = 0
        self.is_on = False
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def measure(self):
        self.temperature += random.uniform(34,42)
    def show_status(self):
        if self.is_on:
            print(f'Zmierzona temperatura: {self.temperature:.1f}C',end=' ')
            if self.temperature > 41:
                print("(Stan zagrożenia życia!!!)")
            elif self.temperature >= 37:
                print("(gorączka)")