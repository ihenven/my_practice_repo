class Car:
    """__init__ -  color, engine_type, gas_tank,
and odometer as parameters to initialize the car
"""
    def __init__(self, color, engine_type, gas_tank, odometer): #class method
    #instance variables
        self.color= color
        self.engine_type =engine_type
        self.gas_tank =gas_tank
        self.odometer= odometer

    """_str_: return the color of the car concatenated
with the engine type of the car."""

    def __str__ (self):    #class method
        return f"{self.color}: {self.engine_type}" 

    def drive(self):
        if self.engine_type == "4_cylinder":
            self.gas_tank -=3
            self.odometer +=90
        elif self.engine_type == "V8":
            self.gas_tank -= 4
            self.odometer += 50
    def get_gas_tank(self):
        return self.gas_tank

    def get_odometer(self):
        return self.odometer

#instructions
'''Create a class called Car in a file called car.py
The class Car should have the following instance variables:
• color = this is the color of the car
• engine_type = this is the type of engine the car has
• gas_tank = keeps track of how many gallons of gas are in the tank
• odometer =  keeps track of the car mileage
The Car class should have the following class methods:
• __init__ - the init method should have the color, engine_type, gas_tank,
and odometer as parameters to initialize the car.
• __str__ - the str method should return the color of the car concatenated
with the engine type of the car.
• drive – if the engine type is “4_cylinder” then drive should reduce the
gas_tank by 3 gallons and increase the odometer value by 90 miles. If
the engine type is “V8” then the drive method should reduce the
gas_tank by 4 gallons and increase the odometer by 50 miles.
• get
_gas_tank – returns the number of gallons of gas left in the car.
• get_odomoter – returns the mileage of the car
2. Create a file called car_tester.py that reads in the file cars.txt. The file,
cars.txt contains data on 5 cars. Each line of the file contains the color,
engine type, gas tank, and odometer readings. Each value is separated by a
whitespace. Read in this file and create five car objects. Store the 5 car
objects in a list.
Call the class methods on the first and second cars read from the file and
confirm the results are as expected. The first and second cars are stored in
index 0 and 1 of the list.
Note: the gas tank and odometer readings will be read in as strings. You
should convert those strings to integers before creating the Car object.'''