#!/usr/bin/python3
"""
class Rectangle
"""


from models.base import Base
class Rectangle(Base):
    """
    class = Rectangle
    private attrs = width, height, x, and y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        htag = ""
        if self.__width != 0 and self.__width != 0:
            htag += "\n" * self.__y
            for x in range(self.__height):
                htag += " " * self.__x
                htag +=("#" * self.__width)
                if x != self.__height - 1:
                    htag += "\n"
        print(htag)

    def __str__(self):
        id2 = self.id
        x = self.__x
        y = self.__y
        w2 = self.__width
        h2 = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id2, x, y, w2, h2)

    def update(self, *args):
        if len(args) > 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg

