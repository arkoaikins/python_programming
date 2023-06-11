#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argument = len(argv)

    if argument == 1:
        print("{} arguments.".format(argument - 1))
    elif argument == 2:
        print("{} argument:".format(argument - 1))
    else:
        print("{} arguments:".format(argument - 1))
    for i in range(1, argument):
        print("{}: {}".format(i, argv[i]))

