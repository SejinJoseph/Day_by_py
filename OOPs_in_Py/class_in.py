class car:
    def __init__(self,model,year,colour,on_sale):

        self.model=model
        self.year=year
        self.colour=colour
        self.on_sale=on_sale

Car1=car("BMW",2025,"RED",True)
Car2=car("Thar",2026,"Black",False)

print(Car1.model,Car1.year)
print(Car2.model)