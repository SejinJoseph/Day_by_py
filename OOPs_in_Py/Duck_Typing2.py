class Bird:
    alive=True 
    def eat(self):
        print("It Can eat!!")

class sparrow(Bird):
    

    def fly(self):
        print("Sparrow Can  fly")


class Eagle(Bird):
    

    def fly(self):
        print("Eagle Can  fly")

class aeroplane:
    alive=False

    def fly(self):
        print("Aeroplane Can  fly")

    def eat(self):
        print("It Cannot  eat!!")

Birds=[sparrow(),Eagle(),aeroplane()]

for bird in Birds :
    bird.fly()
    bird.eat()
    print("Is_Alive:",bird.alive)
    print("-"*30)
