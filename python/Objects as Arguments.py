class Car:

    color = None

class Motorcycle:

    color = None

def change_color(car,color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"Red")
change_color(car_2,"White")
change_color(car_3,"Blue")
change_color(bike_1,"Black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)