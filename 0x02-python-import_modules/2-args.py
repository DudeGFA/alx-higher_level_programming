#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_arguments = len(sys.argv) - 1
    if no_of_arguments == 0:
        print("0 arguments.")
    elif no_of_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_of_arguments))
    for i in range(no_of_arguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))