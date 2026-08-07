# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck.

class Animal:
    Alive=True

class Dog(Animal):
    def speak(self):
        print("Dog barks !!!")
class Cat(Animal):
    def speak(self):
        print("Cat meows!!!")
class car():
    Alive=False
    def speak (self):
        print("HOORNNNNNN.......")

animals=[Dog(),Cat(),car()]


for animal in animals:
    animal.speak()
    print("Alive:",animal.Alive)
    print()