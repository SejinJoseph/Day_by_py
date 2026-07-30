class student:

    Gr_year=2029

    num_std=0

    def __init__ (self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        student.num_std +=1
        
std1=student("Stejin",19,56)
std2=student("Shanic",18,53)

print((f"Roll No:{std1.roll}\n" \
f"Hi I Am {std1.name} and My age is {std1.age}\n I Graduate in the year {student.Gr_year}\n"))


print((f"Roll No:{std2.roll}\n" \
f"Hi I Am {std2.name} and My age is {std2.age}\n I Graduate in the year {student.Gr_year}"))


print ( f"The number of Student in the class : {student.num_std}")


