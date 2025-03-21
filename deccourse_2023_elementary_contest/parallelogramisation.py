import sys
from collections import deque

q = int(sys.stdin.readline().strip())
dq = deque()

for i in range(q):
    line = sys.stdin.readline().strip().split()
    query, area = 0, 0

    if(len(line) == 1):
        query = int(line[0])
    else:
        query = int(line[0])
        area = int(line[1])

    if(query == 1):
        dq.append(area)
    elif(query == 2):
        dq.pop()
    else:
        print(dq.popleft())
