from car import Car

car_1 = Car("Chevy","Corvette","2020","Red")
car_2 = Car("Ford","Mustang","2019","Golden")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("\t")
car_1.drive()
car_1.stop()
print("\t")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

print("\t")
car_2.drive()
car_2.stop()