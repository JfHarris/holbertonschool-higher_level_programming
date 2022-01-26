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
# add setter/getter for private attrs
# add type errors for non ints
# add value error for width/height <= 0
# add value error for x/y under 0
