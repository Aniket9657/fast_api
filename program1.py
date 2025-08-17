class Dog:
    def bark(self):
        print("woof")


# bark()  # This will raise an error because 'bark' is not defined in this scope
@staticmethod 
def info():
    print("this is a static method")



d1 = Dog()
d1.bark()
Dog.info()

