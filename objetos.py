class Person():
    name = "" #Attribute 1
    age = "" #Attribute 2

    #Constructor
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    #Methods
    def get_name(self, name):
        return self.name
    def get_age(self, age):
        return  self.age

p1 = Person("Juan", 18)

print(p1.name, " > ", p1.age)