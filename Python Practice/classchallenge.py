

class Vehicle: #parent class
    model = "Camaro" #adding attributes
    brand = "Chevy"

    def printVehicle(self):
        print("This is a {} {}.".format(self.brand,self.model)) #added method function

carExample = Vehicle() #defined method function variable
carExample.printVehicle() #executed function  

class Car(Vehicle): #created child class
    model= "Corvette" #polymorphism
    wheels = "4"        #added new attributes
    doors = "2"

class Airship(Vehicle):
    brand="Waco Aircraft" #polymorphism
    wings = "2"
    typeofAirship = "Biplane"



