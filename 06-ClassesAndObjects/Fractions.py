class fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def show_fraction(self):
        if int(self.numerator) == self.numerator and int(self.denominator) == self.denominator:
            print(f'{int(self.numerator)}/{int(self.denominator)}')
        else:
            print(f'{self.numerator}/{self.denominator}')
    def reduce_fraction(self):
        import math
        gcd = math.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator/gcd
        self.denominator = self.denominator/gcd
fr = fraction(1, 2)
fr.show_fraction()
fr = fraction(12, 21)
fr.reduce_fraction()
fr.show_fraction()