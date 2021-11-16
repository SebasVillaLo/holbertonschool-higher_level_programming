#!/usr/bin/python3
""""
class studen
"""


class Student:
    """"
    def init
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dic = {}
        for count in attrs:
            try:
                new_dic[count] = self.__dict__[count]
            except:
                pass
        return new_dic

    def reload_from_json(self, json):
        if len(json) != 0:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
