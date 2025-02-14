n = int(input())
nums = list(map(int, input().split()))

results = []
available_dolls = []

for i in range(n):
    available_dolls.append(nums[i])
    available_dolls.sort()

    stack_size = 0
    current_size = -float("inf")

    for doll in available_dolls:
        if doll - current_size >= 2:
            stack_size += 1
            current_size = doll

    results.append(stack_size)

print(*results)

# O(n log n)