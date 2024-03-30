# Str.format() = optional method that gives users
#                 more control when displaying output

#animal = "Cow"
#item = "Moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped ove the {}".format(animal,item))
#print("The {1} jumped ove the {0}".format(animal,item)) #positional argument
#print("The {item} jumped ove the {animal}".format(animal="Cow",item="Moon")) # keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#name = "yeasin"
#print("Hello my name is {}".format(name))
#print("Hello my name is {:10}. nice to meet you".format(name))
#print("Hello my name is {:<10}. nice to meet you".format(name))
#print("Hello my name is {:>10}. nice to meet you".format(name))
#print("Hello my name is {:^10}. nice to meet you".format(name))


number = 1000

print("The number is in .after {:3f}".format(number))
print("The number is in digit {:,}".format(number))
print("The number is in binnary {:b}".format(number))
print("The number is in octal {:o}".format(number))
print("The number is in hexadesimal {:X}".format(number))
print("The number is in Sciencetific {:E}".format(number))