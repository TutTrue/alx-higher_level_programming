#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle representaion"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """intialize width and geight"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * self.height + 2 * self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """"which rec is bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    def __str__(self):
        """how the obkect will be printed"""
        if self.width == 0 or self.height == 0:
            return ""
        str_printed = ""
        for i in range(self.height):
            for j in range(self.width):
                str_printed += str(self.print_symbol)
            if i != self.height - 1:
                str_printed += "\n"
        return str_printed

    def __repr__(self):
        """string to recreate the object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """dectractor"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
