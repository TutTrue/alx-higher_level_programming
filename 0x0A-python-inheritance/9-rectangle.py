#!/usr/bin/pytohn3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """init the height and width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        def area(self):
            return self.__height * self.__width

        def __str__(self):
            return f"[Rectangle] {self.__width:s}/{self.__height:s}"
