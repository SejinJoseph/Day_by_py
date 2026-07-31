class family:

     def __init__(self,name):
          self.name=name

class father(family):
    def smart(self):
        print(f"{self.name} is very smart.... ")

    def hard_work(self):
        print(f"{self.name} is a hard worker......")

class mother(family):
    
    def kind(self):
        print(f"{self.name} is very kind....")

    def caring(self):
        print(f"{self.name} is caring....")


class child(father,mother):
    def cute(self):
        print(f" {self.name} is sooo cute..... ")

    def Fst_gra(self):
        print(f"{self.name} is a first graduate")
    

son=child("Senku")


print(f"The child name is {son.name}")
print()
son.smart()
print()
son.hard_work()
print()
son.kind()
print()
son.caring()
print()
son.cute()
print()
son.Fst_gra()
