class Student:
    def __init__(self, name):
        self.name = name          #public
        self._gpa = 3.5           #protected
        self.__password ="1234"   #private

student1 = Student("Assy")
print(student1.name)
print(student1._gpa)
#
# 
# print(student1.__password)



class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

car1 = car("BMW", "red")
car2 = car("Audi", "blue")

print(car1.name, car1.color)
print(car2.name, car2.color)  

