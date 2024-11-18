# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.

"""
T1 company
"""

def max_interval_with_one(arr):
    current_interval = 0
    counter_zero = 0
    arr_1_1 = 0
    arr_1_2 = 0
    max_length = 0
    dubble_zero_flag = False


    if 1 not in arr:
        return 0
    elif 0 not in arr and len(arr) == 1:
        return 0

    else:
        for i in range(len(arr)):
            if arr[i] == 1:

                current_interval += 1
                arr_1_1 = current_interval
                max_length = max(max_length, arr_1_1 + arr_1_2)

                if dubble_zero_flag:
                    counter_zero -= 1

            else:
                counter_zero += 1
                if counter_zero > 2:
                    dubble_zero_flag = True
                    counter_zero -= 1
                    continue
                else:
                    if counter_zero % 2 == 0:
                        arr_1_2 = current_interval
                        max_length = max(max_length, arr_1_1 + arr_1_2)
                        current_interval = 0
                        counter_zero = 0
                    else:
                        arr_1_1 = current_interval
                        max_length = max(max_length, arr_1_1 + arr_1_2)
                        current_interval = 0

        max_length = max(max_length, arr_1_1 + arr_1_2)

    return max_length
test_data = [0, 0, 1, 1, 0, 1, 1, 0, 1]
print(max_interval_with_one(test_data))