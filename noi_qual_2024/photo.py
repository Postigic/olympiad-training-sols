import heapq

n, s = map(int, input().split())
classes = [sorted(list(map(int, input().split()))) for _ in range(n)]

heap = []
for i in range(n):
    heapq.heappush(heap, (classes[i][0], i, 0))

current_max = max(classes[i][0] for i in range(n))

min_diff = float("inf")

while True:
    current_min, class_idx, pointer_idx = heapq.heappop(heap)

    min_diff = min(min_diff, current_max - current_min)

    if pointer_idx + 1 == s:
        break

    next_element = classes[class_idx][pointer_idx + 1]
    heapq.heappush(heap, (next_element, class_idx, pointer_idx + 1))

    current_max = max(current_max, next_element)

print(min_diff)