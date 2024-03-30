import random

x = random.randint(0,9)
y = random.random()

mylist = ["Rock ","paper ", "scissors "]
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)