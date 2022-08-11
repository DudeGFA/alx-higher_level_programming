#!/usr/bin/python3
"""defines class Base"""
import json
import csv


class Base:
    """Parent class to other
    classes in this package's modules
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new instance of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts
            Args:
                list_dictionaries (list): List of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
            a list of objects to a file
            Args:
                list_objs (list): list of inherited base instances
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of
            the JSON string representation json_string
            Args:
                json_string (str): A JSON str representaion of a
                list of dicts.
            Returns:
                an empty list - if JSON_string is None or empty.
                else - Th python list represented by te json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a new cls object instantiated
            from a dictionary of attributes.
        Args:
            **dictionaty (dict): dictionary representation of new object
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of cls objects instantiated from
            a file containing JSON strings.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the CSV serialization
            of a list of objects to a file.
            Args:
                list_objs (list): list of subinstances of Base
            """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a new list of classes instantiated from a CSV file.
            returns an empty list if the file doesn't exist
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
        except IOError:
            return []
