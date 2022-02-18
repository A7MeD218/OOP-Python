#static method
#static method id bound to a class rather than the objects for the class
#can be called without an object for that class. 

class Math:

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(y):
        return y + 10

    @staticmethod
    def pr():
        print("Hello, world!")

print(Math.add5(2))
print(Math.add10(2))
Math.pr()