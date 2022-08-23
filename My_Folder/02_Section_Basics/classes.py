#OOPS

from http.client import METHOD_NOT_ALLOWED


class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "Driving"
        self.speed = speed
        
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2    
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcyle at", self.speed)

Car1 = Car("gas")
Car2 = Car("electric")
mc1 = Motorcycle("gas", False)
mc2 = Motorcycle("petrol", True)  


Car1.drive(30)
Car2.drive(40)
mc1.drive(50)


print(mc1.wheels)
print(Car1.enginetype)
print(Car2.doors)
print(Car2.enginetype)
print(mc2.enginetype,  mc2.wheels)
