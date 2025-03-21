import sys
import bisect

n = int(sys.stdin.readline().strip())
dolls = list(map(int, sys.stdin.readline().strip().split()))

freq = {}
sorted_keys = []

def insert_doll(x):
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
        bisect.insort(sorted_keys, x)

def compute_chain():
    chain_length = 0
    last = -float("inf")
    for size in sorted_keys:
        if size >= last + 2:
            chain_length += 1
            last = size
    return chain_length

results = []

for doll in dolls:
    insert_doll(doll)
    results.append(compute_chain())

print(" ".join(map(str, results)))

# WHUIAUHRAUIHR UIHADH AR IWOHROISAHRHIOARIOHARHIOARH OIRAHOIROIRA nothing is working i'm WASHED