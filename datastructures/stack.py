def insert(list, val):
    list.append(val)


def remove(list):
    if len(list) > 0:
        return list.pop()
    return None


def gethead(list):
    if len(list) > 0:
        return list[-1]
    return None


stack = []
# Add to stack
insert(stack, 5)
print("head", gethead(stack))
insert(stack, 20)
print("head", gethead(stack))

# Pop from stack
print(remove(stack))
print("head", gethead(stack))
print(remove(stack))
print("head", gethead(stack))
# Underflow
print(remove(stack))
print("head", gethead(stack))
