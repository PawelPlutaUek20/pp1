class Vehicle():
    def __init__(self, brand, registration_number):
        self.brand = brand
        self.registration_number = registration_number
        self.mileage = 0
        self.is_rented = False
    def __str__(self):
        return f'''   Brand: {self.brand}
    Registration number: {self.registration_number}
    Mileage: {self.mileage}
    Rented: {self.is_rented}
    '''

    def rent(self):
        self.is_rented = True
        
    def return_car(self):
        self.is_rented = False
        
    def increase_mileage(self, number):
        self.mileage += number

class Rental():
    def __init__(self):
        self.name = "CRENTALS"
        self.cars = []
    def add_car(self, *args):
        for car in args:
            self.cars.append(car)
    def list_cars(self):
        for  i, car in enumerate(self.cars):
            print(i+1, end="")
            print(f'{car}')
    def list_available_cars(self):
        i=1
        for car in (self.cars):
            if car.is_rented == False:
                print(i, end="")
                print(f'{car}')
                i+=1
    def list_rented_cars(self):
        i=1
        for car in (self.cars):
            if car.is_rented == True:
                print(i, end="")
                print(f'{car}')
                i+=1
    def rent_by_registration(self, registration):
        for car in self.cars:
            if car.registration_number == registration:
                if car.is_rented == False:
                    car.rent()
                    break
            
    def return_by_registration(self, registration, km=0):
        for car in self.cars:
            if car.registration_number == registration:
                if car.is_rented == True:
                    car.increase_mileage(km)
                    car.return_car()
                    break
                
class Car(Vehicle):
    def __init__(self, brand, registration_number, sites):
        Vehicle.__init__(self, brand, registration_number)
        self.sites = sites
    def __str__(self):
        return f'''   Brand: {self.brand}
    Registration number: {self.registration_number}
    Mileage: {self.mileage}Km
    Rented: {self.is_rented}
    Sites: {self.sites}
    '''
class Van(Vehicle):
    def __init__(self, brand, registration_number, capacity):
        Vehicle.__init__(self, brand, registration_number)
        self.capacity = capacity
    def __str__(self):
        return f'''   Brand: {self.brand}
    Registration number: {self.registration_number}
    Mileage: {self.mileage}Km
    Rented: {self.is_rented}
    Capacity: {self.capacity}T
    '''
        

# c1 = Car("Opel", "4859CMN", 5)
# c2 = Car("BMW", "2137JP2", 4)
# c3 = Car("Ferrari", "3810ADL", 2)
# v1 = Van("Fiat", "2000NOV", 3.5)
# v2 = Van("Ford", "9023JAS", 2.2)
# rental = Rental()
# rental.add_car(c1,c2,c3,v1,v2)
# rental.list_cars()
# rental.rent_by_registration("4859CMN")
# rental.rent_by_registration("2000NOV")
# rental.list_rented_cars()
# rental.list_available_cars()
# rental.return_by_registration("4859CMN",950)
# rental.list_rented_cars()
# rental.list_available_cars()