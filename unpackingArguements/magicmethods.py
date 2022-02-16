class Person:
    def __init__(self,name,age):
       self.name= name
       self.age=age

# to print string names we should use string magic method
    def __str__(self):
        return f"{self.name} is {self.age} of age"


msk=Person("Sai",25)
msk.__repr__()
print(msk)