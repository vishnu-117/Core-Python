# from queue import Queue
from queue import Queue
q = Queue(maxsize=3)

q.put('v')
q.put('t')
q.put('u')

print(q)
print(q.empty(), 'is_empty')
print(q.full())

print(q.get())
print(q.get())
print(q.get())

print(q.empty())

