#!/usr/bin/python3
#function that adds 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    #using list comprehension
    #If a tuple is smaller than 2, use the value 0 for each missing integer
    #If a tuple is bigger than 2, use only the first 2 integers
    list1 = [tuple_a[i] if i < len(tuple_a) else 0 for i in range(2)]
    list2 = [tuple_b[i] if i < len(tuple_b) else 0 for i in range(2)]
    first = list1[0] + list2[0]
    secnd = list1[1] + list2[1]
    new_tuple = (first, secnd)

    return new_tuple
