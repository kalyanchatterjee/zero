# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def has_duplicates(str):
    if len(str) == 0 or len(str) == 1:
        return False

    str = str.lower()
    for i in range(0, len(str)):
        left_sub_string = str[:i]
        right_sub_string = str[i + 1 :]

        if str[i] in left_sub_string:
            return True

        if str[i] in right_sub_string:
            return True

    return False


print(has_duplicates("Hello"))
print(has_duplicates(""))
print(has_duplicates("App"))
print(has_duplicates("A"))
