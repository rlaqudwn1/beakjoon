from itertools import permutations
n = int(input())
m = [i for i in range(1,n+1)]
for p in permutations(m):
    print(*p)