from typing import List


def sort(unsorted_list: List[int]) -> List[int]:
    if len(unsorted_list) == 0 or len(unsorted_list) == 1:
        return unsorted_list

    for i in range(1, len(unsorted_list)):
        k = i
        while k > 0:
            if unsorted_list[k] < unsorted_list[k - 1]:
                unsorted_list[k - 1], unsorted_list[k] = (
                    unsorted_list[k],
                    unsorted_list[k - 1],
                )
            k = k - 1

    return unsorted_list


print(sort([]))
print(sort([1]))
print(sort([5, 3, 2, 1, 6, 7, 4, -9]))

# Time complexity is O(n^2)
# Space complexity is O(1)
