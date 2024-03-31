from collections import deque

q = deque()
q.append('v')
q.append('t')
q.append('u')

print(q)

q.popleft()
q.popleft()
q.popleft()

print(q)