# A deque is a double-ended queue. 
# It can be used to add or remove elements from both ends.
#
# Deques support thread safe, memory efficient appends and pops from either side of the deque 
# with approximately the same  performance in either direction.

# >>> from collections import deque

# >>> d = deque()
# >>> d.append(1)
# >>> print d
# deque([1])
# >>> d.appendleft(2)
# >>> print d
# deque([2, 1])
# >>> d.clear()
# >>> print d
# deque([])
# >>> d.extend('1')
# >>> print d
# deque(['1'])
# >>> d.extendleft('234')
# >>> print d
# deque(['4', '3', '2', '1'])
# >>> d.count('1')
# 1
# >>> d.pop()
# '1'
# >>> print d
# deque(['4', '3', '2'])
# >>> d.popleft()
# '4'
# >>> print d
# deque(['3', '2'])
# >>> d.extend('7896')
# >>> print d
# deque(['3', '2', '7', '8', '9', '6'])
# >>> d.remove('2')
# >>> print d
# deque(['3', '7', '8', '9', '6'])
# >>> d.reverse()
# >>> print d
# deque(['6', '9', '8', '7', '3'])
# >>> d.rotate(3)
# >>> print d
# deque(['8', '7', '3', '6', '9'])


# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()

n = int(input())

for c in range(0,n):
    comm = input().split(" ")
    if comm[0] == "append" :
        d.append(comm[1])
    elif comm[0] == "appendleft" :
        d.appendleft(comm[1])
    elif comm[0] == "pop" :
        d.pop()
    elif comm[0] == "popleft" :
        d.popleft()
    else :
        continue
print(" ".join(list(d)))

