# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter,unlick,positional arguments
#                     python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="yeasin",middle="+",first="aysha")
#hello("yeasin","+","aysha")