N,M= map(int,input().split())
# 중복 허용 수열

arr=[]
def DFS(depth):
    if(depth==M):
        print(*arr)
        return
    for i in range(1,N+1):
        arr.append(i)
        DFS(depth+1)
        arr.pop()
DFS(0)