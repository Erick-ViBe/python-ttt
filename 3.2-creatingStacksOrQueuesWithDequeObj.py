

















from collections import deque

x = deque('abcdef')
print(x)
# deque(['a', 'b', 'c', 'd', 'e', 'f'])

x.append('f')
print(x)
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'f'])

x.appendleft('1')
print(x)
# deque(['1', 'a', 'b', 'c', 'd', 'e', 'f', 'f'])

x.pop()
print(x)
# deque(['1', 'a', 'b', 'c', 'd', 'e', 'f'])

x.popleft()
print(x)
# deque(['a', 'b', 'c', 'd', 'e', 'f'])

print(x[0])
# a

x.rotate(2)
print(x)
# deque(['e', 'f', 'a', 'b', 'c', 'd'])
