from collections import defaultdict, Counter
N, M = map(int, input().split())
answer=[]
can_t_hear = set()
for _ in range(N):
    can_t_hear.add(input())

can_t_see = set()
for _ in range(M):
    can_t_see.add(input())

answer = sorted(list(can_t_hear & can_t_see))

answer= sorted(answer)
print(len(answer))
for name in answer:
    print(name)
