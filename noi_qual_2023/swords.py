n = int(input())
swords = []

for _ in range(n):
    i = list(map(int, input().split()))
    swords.append(i)

swords.sort(reverse=True, key=lambda x: (x[0], x[1]))
max_b = -float("inf")
count = 0

for a, b in swords:
    if b > max_b:
        max_b = b
        count += 1

print(count)