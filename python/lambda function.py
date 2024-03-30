# lambda function = function written by one line using lambda keyword
#                   accept any number of arguments, but only has one expression
#                   (think of it as a shortcut
#                   useful if needed for a short period of a time, throw-away
#
# lambda parameters : expression

#def double(x):
    #return x * 2

#print(double(5))

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age= lambda age: True if age >= 18 else False
print(age(17))

