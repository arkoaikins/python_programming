#!/usr/bin/python3
"""
functio that does the same as python
bytecode
"""


from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return (sub(a, b))

from dis import dis
dis(magic_calculation)
