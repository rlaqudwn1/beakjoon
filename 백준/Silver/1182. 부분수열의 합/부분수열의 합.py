
N,S = map(int,input().split())
# 다음 단계에서 선택된 후보군이 전 단계의 선택에 영향을 받는가? O
# 
arr = list(map(int, input().split()))
count=0
def dfs(start,current_sum):
    global count
    if(current_sum==S and start!= 0):
        count+=1

    for i in range(start,N):
        dfs(i+1,current_sum+ arr[i])
dfs(0,0)
print(count)