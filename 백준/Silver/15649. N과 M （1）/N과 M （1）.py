from itertools import permutations
n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
for p in permutations(arr,m):
    print(*p)