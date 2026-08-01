from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def stop(self):
        pass
    @abstractmethod    
    def start(self):
        pass

class Bike(Vehicle):
    def stop(self):
            print("The Bike Is stoped")
       

    def start(self):
            print("The Bike Is started")

class Car(Vehicle):
    def stop(self):
        print("The car Is stoped")
            
     
    def start(self):
        print("The car Is started")
    

bike=Bike()
car=Car()
bike.start()
print()
bike.stop()
print()
car.start()
print()
car.stop()