# reduce() = apply a function to an iterable and reduce it toa single cumulative value.
#            performs function on first tow elements and repeats process until 1 value remains
# reduce (function, iterable)

import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x, y,:x + y,letters)
#print(word)

factorials =[5,6,9,8,2,7]
number = functools.reduce(lambda x, y,:x * y,factorials)
print(number)
