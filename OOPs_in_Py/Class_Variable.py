class student:

    Gr_year=2029

    num_std=0

    def __init__ (self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
std1=student("Stejin",19,56)
std2=student("Shanic",18,53)
student.num_std +=1

print(std1.name)
print(std1.age)
print(std1.roll)

print(std2.name)
print(std2.age)
print(std2.roll)

print(student.Gr_year)
print(student.num_std)


