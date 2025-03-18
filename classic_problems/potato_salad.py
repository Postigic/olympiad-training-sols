n, d = map(int, input().split())
potatoes = list(map(int, input().split()))
print(sum(sorted(potatoes, reverse=True)[:d])) 