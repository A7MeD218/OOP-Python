#Inhertance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("I don't know what I say!")
    
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # we don't need to define the name & the age again because we can use (super()."method") to get it from the parent class (Pet) which we wrote as a parameter in out class.
        self.color = color

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 34)
c.speak()

d = Dog("Jill", 25)
d.speak()

f = Fish("Bubbles", 10)
f.speak()