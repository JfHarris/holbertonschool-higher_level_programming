#!/usr/bin/python3
"""
class Base
"""


class Base:
    """
    class = Base
    public attr = nb_objects = 0
    """

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects