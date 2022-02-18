#classmethod
class Person:
    number_of_people = 0  #class attribute

    def __init__(self, name):
        self.name = name  #instance attribute
        Person.number_of_people += 1

    @classmethod  #we add this decorator to refers to classmethod
    def number_of_people(cls):
        return cls.number_of_people  #it access the class attribute directly

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1 


p1 = Person("Ahmed")
print(Person.number_of_people)
print(p1.name)
p2 = Person("Ziyad")
print(Person.number_of_people)
print(p2.name)
