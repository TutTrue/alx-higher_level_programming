#!/usr/bin/python3
class Square:
    """square"""
    def __init__(self, size=0):
        """init
        Args:
            size: size of the square
        """
        self.size = size
    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of a square"""
        return self.__size * self.__size
