import sys

n, a, b = map(int, sys.stdin.readline().strip().split())
phy = list(map(int, sys.stdin.readline().strip().split()))
bio = list(map(int, sys.stdin.readline().strip().split()))
max_sum = sum(phy)

for i in range(n):
    bio[i] -= phy[i]

bio = sorted(bio, reverse=True)

for i in range(b):
    max_sum += bio[i]

print(max_sum)