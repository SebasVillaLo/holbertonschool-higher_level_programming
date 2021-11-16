#!/usr/bin/python3
""""
class base
"""
import json


class Base:
    """"init"""
    __nb_objects = 0

    def __init__(self, id=None):
        """"condicional"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """"json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"save"""
        filename = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """"from json"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"create"""
        if cls.__name__ == "Square":
            dummy = cls(8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(8, 8)
        dummy.update(**dictionary)
        return dummy
