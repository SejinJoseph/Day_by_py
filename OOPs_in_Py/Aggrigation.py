class Employ:
    def __init__(self,name,RegNo,departent):

        self.name=name
        self.RegNo=RegNo
        self.departent=departent

class Department:
    def __init__(self,Dep_name,Dep_No):
    
            self.Dep_name=Dep_name
            self.Dep_No=Dep_No

dept=Department("Ai/Ml",234)

emp1=Employ("Stejin",963325,dept)

print("Employ_Name:",emp1.name)
print("Employ_RegNo:",emp1.RegNo)
print("Employ_Department:",emp1.departent.Dep_name)
print("Department_No:",emp1.departent.Dep_No)


