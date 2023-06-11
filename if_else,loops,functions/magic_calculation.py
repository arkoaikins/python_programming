from dis import dis
""" dis helps to view python bytecode"""

def magic_calculation(a, b, c):
    if a < b:
        return (c)
    elif c > b:
        return(a + b)
    return(a * b) - c

dis(magic_calculation)
