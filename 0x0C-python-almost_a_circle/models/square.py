#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representation of square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init the object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the value"""
        self.width = value
        self.height = value

    def __str__(self):
        """representation of the square
        in print() and str()
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """update the class Rectangle with the new values"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """return a dictionary representation of the obj"""
        return {
            'id': getattr(self, 'id'),
            'x': getattr(self, 'x'),
            'size': getattr(self, 'height'),
            'y': getattr(self, 'y')
            }
