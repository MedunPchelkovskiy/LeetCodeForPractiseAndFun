nums = [2, 7, 11, 15]
target = 9
list_result = []

import time

start_time = time.time()


def two_sums(numbers, target_num):
    number_map = {}
    for indx in range(len(numbers)):
        searched_num = target_num - numbers[indx]
        if searched_num in number_map:
            print([number_map[searched_num], indx])
            break
        number_map[numbers[indx]] = indx


end_time = time.time()
print(end_time - start_time)

two_sums(nums, target)
