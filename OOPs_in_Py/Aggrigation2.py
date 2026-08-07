class Student:
    def __init__(self,name,age,laptop):
        self.name=name
        self.age=age
        self.laptop=laptop



class Laptop:
    def __init__(self,brand,ram,processor,ssd,graphic_card,display):
        self.brand=brand
        self.ram=ram
        self.processor=processor
        self.ssd=ssd
        self.graphic_card=graphic_card
        self.display=display


lap=Laptop("Lenovo","16GB RAM","i5 13gen","512 SSD","RTX 4050","16.9 inch")

stud=Student("Stejin",19,lap)

print("Name:",stud.name)
print("Age:",stud.age)
print("Brand:",stud.laptop.brand)
print("Ram:",stud.laptop.ram)
print("Processor:",stud.laptop.processor)
print("SSD:",stud.laptop.ssd)
print("Graphic_Card:",stud.laptop.graphic_card)
print("Display:",stud.laptop.display)
        