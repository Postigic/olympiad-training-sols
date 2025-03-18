import heapq

n, k = map(int, input().split())
heights = list(map(int, input().split()))

min_heap = []
res = []

for i in range(k):
    heapq.heappush(min_heap, heights[i])

for i in range(k, n):
    heapq.heappush(min_heap, heights[i])

    if len(min_heap) > k:
        heapq.heappop(min_heap)

    res.append(min_heap[0])

res.insert(0, min(heights[:k]))

for result in res:
    print(result)