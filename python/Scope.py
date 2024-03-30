# scope = The region that a veriable is recognized
#         A veriable is only available from inside that region it is created.
#         a global and locally scoped versions of a variable can be created

name = "yeasin" # global scope (available inside & outside functions)

def display_name():
    name = "arafat"  # local scope (available only inside this function)
    print(name)

display_name()
print(name)