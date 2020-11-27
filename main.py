from io_data import *


def main(file_in):
    daily_food, humsters_count, hamsters_bst = input_data(file_in)

    checked_humsters = 0
    total_avarice = 0
    total_daily_norm = 0
    available_food = daily_food

    while checked_humsters < humsters_count:
        current = hamsters_bst.get_min_element()
        total_avarice += current.avarice
        total_daily_norm += current.daily_norm
        checked_humsters += 1

        available_food = daily_food - (total_daily_norm + (checked_humsters - 1) * (total_avarice))

        if available_food < 0:
            checked_humsters -= 1
            break
        checked_humsters += 1
    return checked_humsters;

    # hamsters_bst.remove_min_element()


# print(checked_humsters)
#
# output_data('IO/out/hamster1.out', str(checked_humsters))

if __name__ == "__main__":
    first_file_in = 'IO/in/hamster1.in'
    second_file_in = 'IO/in/hamster2.in'
    third_file_in = 'IO/in/hamster3.in'
    first_file_out = 'IO/out/hamster1.out'
    second_file_out = 'IO/out/hamster2.out'
    third_file_out = 'IO/out/hamster3.out'

    first_result = main(first_file_in)
    second_result = main(second_file_in)
    third_result = main(third_file_in)

    print(f'First hamsters result: {first_result}')
    print(f'Second hamsters result: {second_result}')
    print(f'Third hamsters result: {third_result}')

    output_data(first_file_out, str(first_result))
    output_data(second_file_out, str(second_result))
    output_data(third_file_out, str(third_result))
