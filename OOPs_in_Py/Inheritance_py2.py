class Device:
    def __init__(self,name,year):
        self.name=name
        self.year=year

    def call(self):
        print(f"i am calling using {self.name}")

        print("The call quality is good!!!!!!")

    def cam(self):
        print(f"I took a snap using {self.name}")

        print("The camera  quality is good!!!!!!")

    def per(self):

        print(f"The performance of {self.name}is very good")

class Mobile(Device):

   

    def gaming(self):
        print (f"The {self.name} is the best for gaming in mobile ")

class Laptop(Device):

    def coading(self):
        print(f"The {self.name} is good for coading ")

class Tab(Device):

    def drawing(self):
        print(f"The {self.name} is best for drawing")

mob1 = Mobile("IQOO NEO 10", 2025)
lap1 = Laptop("Lenovo LOQ", 2026)
tab1 = Tab("Samsung TAB", 2023)

print(mob1.name)
print(mob1.year)

print()

print(lap1.name)
print(lap1.year)

print()

print(tab1.name)
print(tab1.year)
print()

mob1.call()
mob1.cam()
mob1.per()
print()

lap1.call()
lap1.cam()
lap1.per()
print()

tab1.call()
tab1.cam()
tab1.per()
print() 

mob1.gaming()
print()
lap1.coading()
print()
tab1.drawing()