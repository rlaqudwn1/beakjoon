import sys
n = int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for _ in range(n)]
a.sort()
for num in a:
    print(num)