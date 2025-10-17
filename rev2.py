class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"My name is {self.name}"

class Student(Person):
    def __init__(self, name, program, year):
        super().__init__(name)
        self.program = program
        self.year = year
    def introduce(self):
        return f"My name is {self.name},I am studying {self.program} inyear {self.year}"
        

class Lecturer(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    def introduce(self):
        return f"My name is {self.name},I am a lecturer in the {self.department} department"   

p = Person("Alpha")
s = Student("Abigail", "BSIT", 2)
l = Lecturer("Omega", "BSIT")

print(p.introduce())
print(s.introduce())
print(l.introduce())