#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """representation of Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the values of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of the x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle with # sign"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width, end="")
            print()

    def __str__(self):
        """representation of the rectangle
        in print() and str()
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            "- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update the class Rectangle with the new values"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """return a dictionary representation of the obj"""
        return {
            'x': getattr(self, 'x'),
            'y': getattr(self, 'y'),
            'id': getattr(self, 'id'),
            'height': getattr(self, 'height'),
            'width': getattr(self, 'width')
        }
