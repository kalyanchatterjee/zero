# Python list is mutable
a = [1, 2, 3, 4, 5, 6, 7, 'a']

# Last element
print(a[-1])

# Subarray slicing indices are left-inclusive and right-exclusive
# This is a common mistake people make in coding interviews
print(a[0:3]) 
print(a[1:3])

# Remember the shorthands 
print(a[:3])
print(a[1:])

# For loops
for i, num in enumerate(a):
    print(i, num)

for x in a:
    print(x)

# Python doesn't have a built-in LinkedList
# Remember to use Pascal notation to declare a class, no underscores
class LinkedListNode:
    def __init__(self, val, next=None):
        self.value = val
        self.nextNode = next
a = LinkedListNode(1)
b = LinkedListNode(4)
c = LinkedListNode(87)

a.nextNode = b
b.nextNode = c

print("Value of a is", a.value, "which points to ", 
a.nextNode, ", which in turn points to ", 
a.nextNode.nextNode, "that has value", 
a.nextNode.nextNode.value)