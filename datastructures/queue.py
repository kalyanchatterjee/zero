# Rather than implementing a circular queue (or deque) yourself,
# use the 'deque' class of the 'collections' module
from collections import deque

queue = deque()
# Add 2 to the end of queue (enqueue)
queue.append(2)
# Add 4 to the beginning of the queue
queue.appendleft(4)
# Print the end of the deque
print(queue[-1])
# Print the front of the queue
print(queue[0])
# Remove the END of the queue (a.k.a dequeue)
queue.pop() 
# Remove the FRONT of the queue
queue.popleft()

