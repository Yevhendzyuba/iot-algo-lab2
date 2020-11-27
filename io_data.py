from bst import *
from hmstr import *
import sys


def input_data(file_name):
    try:
        with open(file_name, 'r') as file:
            number_of_hmstr = int(file.readline())
            amount_of_eat= int(file.readline())
            humster_bst = BST(lambda x: (x.avarice, x.daily_norm))
            for line in file.readlines():
                daily_norm, avarice = line.split()
                humster_bst.add(Hamster(int(daily_norm), int(avarice)))
        return number_of_hmstr, amount_of_eat, humster_bst
    except (FileNotFoundError):
        sys.exit(f'file "{file_name} not found')
    except:
        sys.exit(f'check data in "{file_name}"')


def output_data(file_name, value_to_write):
    with open(file_name, 'w') as file:
        file.write(value_to_write)
