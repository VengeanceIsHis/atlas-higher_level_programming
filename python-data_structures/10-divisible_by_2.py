#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_list=[False] * len(my_list)
    for i, value in enumerate(my_list):
        if value % 2 == 0:
            true_list[i] = True
        else:
            true_list[i] = False
    return true_list







if __name__ == "__main__":
    main()
