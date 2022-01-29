#!/usr/bin/python3
"""
class Base
"""
import json
import os


class Base:
    """
    class = Base
    public attr = nb_objects = 0
    """
    @classmethod
    def clear(cls):
        """Sets the variable to 0 for unittesting"""
        Base.__nb_object = 0

    def __init__(self, id=None):
        """
        init method for base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = self.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string of dict
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string to file
        """
        if list_objs is None or list_objs == []:
            lob = []
        else:
            lob = [x.to_dictionary() for x in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(lob))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON string
        """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        list of instances
        """
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except:
            return []
        x = []
        with open(str(cls.__name__) + ".json", "r") as f:
            x = cls.from_json_string(f.read())
        count_inst = len(x)
        inst = []
        for y in range(count_inst):
            inst.append(cls.create(**x[y]))
        return inst
