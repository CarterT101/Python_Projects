class name:
    def __init__(self, firstName, lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print("Hello, I am {0} {1}".format(self.firstName, self.lastName))

person=name('Dustin','Smith')
person.printName()
