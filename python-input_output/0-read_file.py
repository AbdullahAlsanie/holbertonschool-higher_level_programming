#!/usr/bin/python3
""" read a file """


def read_file(filename=""):
    """ read a file """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
