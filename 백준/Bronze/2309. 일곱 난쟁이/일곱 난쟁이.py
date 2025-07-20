import sys
from itertools import combinations

n = [int(sys.stdin.readline()) for _ in range(9)]
#combinations n에서 7개로의 조합 모든 조합 comb
for comb in combinations(n, 7):
    if sum(comb) == 100:
        for x in sorted(comb):
            print(x)
        break
