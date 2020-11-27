from bst import *
from hmstr import *


def input_data(file_name):
    with open(file_name, 'r') as file:
        S = int(file.readline())
        C = int(file.readline())
        humster_bst = BST(lambda x: (x.daily_norm, x.avarice))
        for line in file.readlines():
            line_1, line_2 = line.split()
            humster_bst.add(Hamster(int(line_1), int(line_2)))

    return S, C, humster_bst


def output_data(file_name, value_to_write):
    with open(file_name, 'w') as file:
        file.write(value_to_write)
