class Person:

    #initializing class variables
    name=""
    age=0

    #constructor, for class that will take 2 paramaters and initialize
    def __init__(self, personName, personAge):
        self.name=personName
        self.age=personAge

    #class methods, for Person
    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

    def calculateSign(self)


#Create an object of Person Class
person1 = Person("Melanie", 21)
person2 = Person("Kenneth", 22)

#This works -- by allowing to print Person1's age
print(person1.age)

#So does this
person1.showAge()
