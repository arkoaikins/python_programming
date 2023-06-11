#!/usr/bin/python3

"""
program that prints the result of the addition of all arguments
usage:
    ./infinet_add 3 4
    7

"""
if __name__ == "__main__":
    from sys import argv
    sum = 0
    counter = len(argv)
    for i in range(1, counter):
        sum += int(argv[i])
    print("{}".format(sum))
