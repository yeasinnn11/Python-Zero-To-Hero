# Super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Rectangle:

    def __int__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __int__(self, length, width):
        super().__int__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __int__(self, length, width, height):
        super().__int__(length,width)
        self.heigth = height

    def volume(self):
        return self.length*self.width*self.heigth


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())