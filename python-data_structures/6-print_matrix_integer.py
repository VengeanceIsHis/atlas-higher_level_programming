#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in row:
            print("{:d}".format(*row), sep=', ')


if __name__ == "__main__":
    main()
