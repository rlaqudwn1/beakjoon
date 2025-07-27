from collections import deque


#기어 4개 초기화
gears = [deque(map(int, input().strip())) for _ in range(4)]

# 총 회전 함수
# 양 옆을 확인하지만 본인이 맨 끝이면 양 옆이 아닌 한쪽만 회전
def rotate_all(num, dir):
    dirs=[0,0,0,0]
    num -=1
    dirs[num]=dir

    left(num,dirs)
    right(num,dirs)
    for i in range (4):
        rotate(i,dirs[i])


# 기어 회전 함수
def rotate(n,dir):
    gears[n].rotate(dir)
# 기어 회전 왼쪽 오른쪽을 나눠서 정의 한다

# 어떤 톱니바퀴를 회전시킬 지에 대한 정보를 배열에 저장
# 전파를 모두 rotate 할 경우 톱니바퀴가 바뀌고 난 후에 전파됨
# 왼쪽 회전
def left(num,dirs):
    for i in range(num,0,-1):
        #i와 i-1번째 맞물린 톱니 확인
        if(gears[i][6]!=gears[i-1][2]):
            dirs[i-1]=dirs[i]*-1
        else:
            break
# 오른 쪽 회전
def right(num,dirs):
    for i in range(num,3):
        if(gears[i][2]!=gears[i+1][6]):
            dirs[i+1]=-dirs[i]
        else:
            break
# k개의 톱니바퀴 회전 명령 실행
k = int(input())
for i in range(k):
    top, d=map(int, input().split())
    rotate_all(top,d)
# 12시가 N인지 체크
def check(i):
    if(gears[i][0]==1):
        return True
#정답 점수
answer=0
for i in range(4):
    if(check(i)):
        answer+=(2**i)

print(answer)