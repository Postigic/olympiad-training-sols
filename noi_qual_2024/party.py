n = int(input())
happiness_arr = list(map(int, input().split()))
happiness_arr = [i for i in happiness_arr if i > 0]
available_seats = (n + 1) // 2
print(sum(sorted(happiness_arr, reverse=True)[:available_seats]))