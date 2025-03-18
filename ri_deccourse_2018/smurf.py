from collections import deque

n = int(input())
smurfs = list(map(int, input().split()))
dq = deque()

for i in range(n):
    if i % 2 == 0:
        dq.append(smurfs[i])
    else:
        dq.appendleft(smurfs[i])

if (n - 1) % 2 == 0:
    dq.reverse()

print(" ".join(map(str, dq)))
