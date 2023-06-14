#!/usr/bin/python3
"""
displays all names in a module
except those that start with __
"""
if __name__ == "__main__":
    """this prevents code from been executed whrn imported"""
    import hidden_4
    for i in dir(hidden_4):
        """the dir function gives acces to names in the module"""
        if i[:2] != "__":
            """
            the [:2] makes us to be able to get
            the first two char of the names
             i.e the 0 and 1
            """
            print("{:s}".format(i))
