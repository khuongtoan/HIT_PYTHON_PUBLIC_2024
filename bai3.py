
class Vehicle :
    def __init__(self,make):
        self.make =make
    def description (self):
        print(self.make)
class Car(Vehicle):
    def __init__(self,make, model):
        super().__init__(make)
        self.model = model
    def description (self):
        print(self.make)
        print(self.model)
class ElectricCar(Car):
    def __init__(self,make, model, battery_size ):
        super().__init__(make,model)
        self.battery_size = battery_size
    def description (self):
        print(self.make)
        print(self.model)
        print(self.battery_size)

a =Vehicle("VN")
b= Car("VN", "TE")
c = ElectricCar("VN","TE","5000")
a.description()
b.description()
c.description()

