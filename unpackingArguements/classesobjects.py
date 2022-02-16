from os import name


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades)/len(self.grades)

stu=Student("Sai", (98,84,96,76,87,76))
print(stu.name)
print(stu.grades)
print(stu.average())

print(Student.average(stu))

stu2=Student("krishna",[98,84,96,76,87,100])
print(stu2.name)
print(stu2.average())


