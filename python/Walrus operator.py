# walrus operator :=

# New to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#    food = input("What food do you lick?:")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you lick?: ") != "quit":
    foods.append(food)