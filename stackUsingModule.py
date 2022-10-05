# implementing using collections module
import collections
stack = collections.deque()
# append element 
stack.append(11)
stack.append(22)
stack.append(33)
stack.append(44)
#pop element
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# print(stack)

# implement using queue module
import queue 
stack = queue.LifoQueue(5)
#append element 
stack.put(10)
stack.put(20)
#pop element

# stack.get(timeout=1)
stack.get(timeout=1)
#stack size
print(stack.qsize())
#is stack empty
print(stack.empty())
