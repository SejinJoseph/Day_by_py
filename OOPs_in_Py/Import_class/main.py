from car import Car

Car1=Car("BMW",2025,"RED",True)
Car2=Car("Thar",2026,"Black",False)

print(Car1.model,Car1.year)

print(Car2.model)

Car1.drive()

Car2.stop()