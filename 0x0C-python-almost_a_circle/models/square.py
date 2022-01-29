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
        """
        init for Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns description of square
        """
        id2 = self.id
        x = super().x
        y = super().y
        w2 = super().width
        return "[Square] ({}) {}/{} - {}".format(id2, x, y, w2)

    @property
    def size(self):
        """
        getter for size
        """
        return super().width

    @size.setter
    def size(self, size):
        """
        setter for size
        """
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)

    def update(self, *args, **kwargs):
        """
        assigns args to Square attrs
        """
        if len(args) > 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    super(Square, type(self)).width.fset(self, arg)
                    super(Square, type(self)).height.fset(self, arg)
                elif count == 2:
                    super(Square, type(self)).x.fset(self, arg)
                elif count == 3:
                    super(Square, type(self)).y.fset(self, arg)
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.fset(self, kwargs["size"])
                super(Square, type(self)).height.fset(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.fset(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.fset(self, kwargs["y"])

    def to_dictionary(self):
        """
        Dict of square
        """
        id2 = self.id
        x = super().x
        y = super().y
        w2 = super().width
        return {"x": x, "y": y, "id": id2, "size": w2}
