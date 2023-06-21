#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    for i in my_list:
        if idx < 0:
            return None
        return my_list[idx]


"""or idx > i:"""
