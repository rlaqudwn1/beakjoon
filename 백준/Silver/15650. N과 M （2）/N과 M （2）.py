from itertools import permutations

N,M = map(int,input().split())
# 중복 수열 안되며 오름차순으로 표현해야 한다
# 다음 단계에서 선택 가능한 후보들이 이전 단계의 선택에 영향을 받는가?
# 영향이 있다면, 그 정보를 함수 인자로 상태로 넘긴다.


visited = [False] * (N+1)
arr = []
def DFS(depth,start):
    if depth == M:
        print(*arr)
        return

    for i in range(start,N+1):
        if not visited[i]:
            arr.append(i)
            DFS(depth+1,i+1)
            arr.pop()
DFS(0,1)
