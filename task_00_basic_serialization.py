#!/usr/bin/env python3
"""
the module adds the  functionality to serialize and deserialize the JSON file
"""


import json


def serialize_and_save_to_file(data, filename):
    """ the function serialize and save data to the specified file """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    pass


def load_and_deserialize(filename):
    """ the function load and deserialize data from the specified file """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
