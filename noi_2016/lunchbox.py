import heapq

n, m = map(int, input().split())
requests = []
satisfied = 0

for i in range(m):
    requests.append(int(input()))

heapq.heapify(requests)

while requests:
    if requests[0] <= n:
        n -= heapq.heappop(requests)
        satisfied += 1
    else:
        break

print(satisfied)