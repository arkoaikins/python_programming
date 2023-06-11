#!/usr/bin/python3
"""
imports a function from another file and uses it
"""
from add_0 import add

if __name__ == "__main__":
    """
    prevents the code below to be used when this file is imported
    into any other file

    """
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
