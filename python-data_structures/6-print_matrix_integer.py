#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, value in enumerate(row):
            print("{:d}".format(value), end='')
            if index < len(row) - 1:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
