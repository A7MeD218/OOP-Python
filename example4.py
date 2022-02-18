# Class Attribute vs. Instance Attribute

class Person:
    number_of_people = 0  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
        Person.number_of_people += 1


p1 = Person("Ahmed")
print(Person.number_of_people)
print(p1.name)
p2 = Person("Ziyad")
print(Person.number_of_people)
print(p2.name)


#instance attribute:
#An instance attribute is a Python variable belonging to one object.
#This variable is only accessible in the scope of this object
#and it is defined inside the constructor.

#class attribute:
#A class attribute is a Python variable that belongs to a class rather than a particular object.
#It is shared between all the objects of this class
#and it is defined outside the constructor.