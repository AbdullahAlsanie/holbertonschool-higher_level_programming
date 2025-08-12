#!/usr/bin/env python3
"""
 serialize and deserialize custom Python objects using the pickle module.
 """


import pickle


class CustomObject:
    """ custom Python class """

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """ Serialize the current object instance to a file using pickle. """
        with open(filename, 'wb') as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def deserialize(cls, filename: str):
        """ Deserialize a CustomObject instance from a file using pickle. """
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
            return obj
