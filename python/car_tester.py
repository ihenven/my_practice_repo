#car tester
##########always remember the class and the import
from car import Car
cars= []

with open("cars.txt") as file:
    for line in file:
        color, engine_type, gas_tank, odometer = line.split()
        gas_tank = int(gas_tank)
        odometer = int(odometer)
        cars.append(Car(color, engine_type, gas_tank, odometer))
       
#call class methods on the first and second cars
first_car = cars[0]
second_car = cars[1]

print("First Car:", first_car)
first_car.drive()
print("Gas Tank:", first_car.get_gas_tank())
print("Odometer:", first_car.get_odometer())

print("Second Car:", second_car)
second_car.drive()
print("Gas Tank:", second_car.get_gas_tank())
print("Odometer:", second_car.get_odometer())