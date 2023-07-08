#!/usr/bin/python3
#function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    row_numb = len(matrix)
    colm_numb = len(matrix[0])
    for i in range(row_numb):
        for j in range(colm_numb):
            print("{:d}".format(matrix[i][j]), end="")
            if j < colm_numb - 1:
                print(" ", end="")
        print()
