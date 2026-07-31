class Person:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f"{self.name} can walk")

    def talk(self):
        print(f"{self.name} can talk")
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

    def write_exam(self):
        print(f"{self.name} writes the exam very well")

class AI_Student(Student):
    def build_project(self):
        print(f"{self.name} builds a project.")

    def train_model(self):
        print(f"{self.name} trains a ai model and deploy it")

per1=AI_Student("Stejin Joseph")

per1.walk()
print()
per1.talk()
print()
per1.study()
print()
per1.write_exam()
print()
per1.build_project()
print()
per1.train_model()