#  Every thing in python is an object.
#  Datatypes (str, int, ...) are part of a classes.
#  Whenever you create something in python you are really creating an object which is an instance of a specific class.

#  e.g:
string = "Hello,world!"
x = 1
print(type(string))
#the output is <class 'str'> 

print(type(x))
#the output is <class 'int'> 

#this means the string and the integer are classes in python
#so that every class has a methods

#  e.g of method:
string = "hello, world!"
print(string.upper()) #  {.upper()} is a method in the str class

#so because of that we can't use {.upper()} in int 