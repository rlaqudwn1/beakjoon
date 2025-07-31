import sys
input = sys.stdin.readline

def update(i, x):
    while i <= N:
        tree[i] += x
        i += (i & -i)

def prefix_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s

def range_sum(l, r):
    return prefix_sum(r) - prefix_sum(l-1)

N, M, K = map(int, input().split())
tree = [0]*(N+1)

arr = [int(input()) for _ in range(N)]
for i in range(N):
    update(i+1, arr[i])

out = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(b, diff)
    else:  # a == 2
        out.append(str(range_sum(b, c)))

sys.stdout.write('\n'.join(out))
