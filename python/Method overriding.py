class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating carrot")


rabbit = Rabbit()

rabbit.eat()
