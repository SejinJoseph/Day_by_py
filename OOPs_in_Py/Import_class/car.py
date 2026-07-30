class Car:
    def __init__(self,model,year,colour,on_sale):

        self.model=model
        self.year=year
        self.colour=colour
        self.on_sale=on_sale

    def drive(self):
        print(f"you drive a {self.model}")

    def stop (self):
        print(f"you stoped the {self.model}!!!")