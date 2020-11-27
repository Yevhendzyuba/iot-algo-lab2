from io_data import *

daily_food, humsters_count, hamsters_bst = input_data('IO/hamster.in')

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

    hamsters_bst.remove_min_element()

print(checked_humsters)

output_data('IO/hamster.out', str(checked_humsters))
