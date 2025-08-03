N,M= map(int,input().split())
# 중복 허용 수열
# 비 내림차순으로 시작 수보다 낮은 수로 출발할 수 없다.


arr=[]
def DFS(depth,start):
    if(depth==M):
        print(*arr)
        return
    for i in range(start,N+1):
        arr.append(i)
        DFS(depth+1,i)
        arr.pop()
DFS(0,1)