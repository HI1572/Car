class Car(object):
    condition = 'new'
    print(condition)
    
    def __init__(self, model, color, mpg, condition):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = condition
    
    def display_car(self):
        print('This is a ' + self.model + ' and I am ' + self.color + ' my mpg is ' + self.mpg)  
    
    def drive_car(self, model, color, mpg, condition):
        print('My car is ' + self.condition)

my_car = Car('Delorean', 'silver', '88', 'old')
my_car.display_car()
    
class ElectricCar(Car):
    condition = 'new'
    print(condition)
    
    def __init__(self, model, color, mpg, condition, battery):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = condition
        self.battery = battery
        
    def display_car(self):
        print('This is a ' + self.model + ' and I am ' + self.color + ' my mpg is ' + self.mpg + ' my battery type is ' + self.battery)

my_eletric_car = ElectricCar('Tesla', 'black', '62', 'new', 'calcium battery')