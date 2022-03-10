from typing import List


def sort(my_list: List[int], start_index=0) -> List[int]:
    if len(my_list) == 0 or len(my_list) == 1:
        return my_list
    # Check if we are at the end of the list
    if start_index != len(my_list) - 1:
        # current min value
        c_m_v = my_list[start_index]
        # current min index
        c_m_i = start_index
        for i in range(start_index, len(my_list)):
            if my_list[i] <= c_m_v:
                c_m_v = my_list[i]
                c_m_i = i

        # Swap elements
        my_list[start_index], my_list[c_m_i] = my_list[c_m_i], my_list[start_index]

        start_index = start_index + 1
        sort(my_list, start_index)

    return my_list


print(sort([]))
print(sort([1]))
print(sort([5, 3, 2, 1, 6, 7, 4, -9]))
