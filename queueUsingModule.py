import collections as c
q= c.deque()
#enqueue
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)
#dequeue
q.pop()
print(q)
q.pop()
q.pop()
print(q)

#creating queue using queue module
import queue as q
que = q.Queue(4)
que.put(10)
que.put(20)
#size of the queue
print(que.qsize())
que.put(30)
que.put(40)
#maxsize of queue
print(que.maxsize,"is the maximum size of the Queue")
# que.put_nowait(50)
print(que.get_nowait())
print(que.get_nowait())
print(que.get_nowait())
print(que.get_nowait())
# print(que.get_nowait())
