n, x, y = map(int, input().split())
trips = list(map(int, input().split()))
min_cost = []

for i in range(n):
    min_cost.append(min(trips[i] * x, y))

print(sum(min_cost))