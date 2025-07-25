n = int(input())
a = list(map(int, input().split()))
x= int(input())
# 오름차순 정렬
a.sort()
# 투 포인터
left =0
right= len(a)-1
answer=0
while left < right:
    sum = a[left]+a[right]
    # 합이 x보다 낮으면 왼쪽 포인터 오른쪽으로
    if(sum<x):
        left +=1
    ## 합이 x랑 맞을 경우 왼쪽 한칸 오른쪽으로 하고 오른쪽 초기화
    if(sum==x):
        answer +=1
        left+=1
        right-=1
    ## 합이 x보다 커질경우 오른쪽 포인터 -1
    if(sum>x):
        right -=1
print(answer)