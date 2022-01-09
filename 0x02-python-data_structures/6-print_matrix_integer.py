#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for total in row:
                if total == row[0]:
                    print("{:d}".format(total), end="")
                else:
                    print(" {:d}".format(total), end="")
            print()
    else:
        print()
