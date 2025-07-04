from collections import Counter

N, C = map(int, input().split())
nums = list(map(int, input().split()))
counter = Counter(nums)

order = {}
for idx, num in enumerate(nums):
    if num not in order:
        order[num] = idx

unique_nums = list(counter.keys())
unique_nums.sort(key=lambda x: (-counter[x], order[x]))

for num in unique_nums:
    for _ in range(counter[num]):
        print(num, end=' ')
