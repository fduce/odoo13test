#Objeto
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

#Herencia
class User(Person):
    def __init__(self, color, name=None, age=None):
        super(User, self).__init__(color)
        self.age = age
        self.name = name
        self.color_pelo = color

user1 = User("Rojo", "Juan", 18)
#user1.age = 19
print(user1)
print(user1.color_pelo, user1.age, user1.name)