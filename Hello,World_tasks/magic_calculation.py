from dis import dis
"""dis helps to view python bytecode"""

def magic_calculation(a, b):
    return (98 + a ** b)
"""that is the function we want to see its bytecode"""

dis(magic_calculation)
""" this is how to use the dis function to run the bytcode"""
