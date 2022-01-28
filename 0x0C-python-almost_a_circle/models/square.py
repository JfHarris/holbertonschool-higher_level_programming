#!/usr/bin/python3
"""
class Square
"""


from models.rectangle import Rectangle
class Square(Rectangle):
    """
    class = Square
    inherits private attrs from Rectangle(height, width, x, y
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id2 = self.id
        x = super().x
        y = super().y
        w2 = super().width
        return "[Square] ({}) {}/{} - {}".format(id2, x, y, w2)