# 올리는 위치는 0 내리는 위치는 n-1
# 자료구조는 2n-1 의 deque의 회전
# 내구도 deque도 2n-1 의 A1,A2의 내구도를 가진다
# 내구도가 0일경우 올릴 수 없다
# 로봇이 어떤칸으로 이동하면 이므로 컨베이어 회전은 내구도에 끼치지 않는게 맞는 것 같다

# 1.회전이 먼저다
# 1-1 이 때 내리는 위치에 도달한다면 로봇은 그 즉시 내린다.
# 2.이동할 수 있는지 확인한 후에 이동한다
# 3. 한턴이 끝나기 전에 내구도가 0인 칸이 K이상인지 확인한다

from collections import deque
from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))

dura = deque(A)

con= deque([0 for i in range((2*N)-1)])
robot='r'
answer=0
def rotation():
    dura.rotate(1)
    con.rotate(1)

def is_drop():
    if con[N-1]== robot:
        con[N-1]=0
while(True):
    answer+=1
    #1. 회전을 제일 먼저한다 그리고 드랍되는지 확인
    rotation()
    is_drop()
    #2. 로봇이 전진한 직후에도 드랍할건지 확인
    for i in range(N,-1,-1):
        if con[i]==robot and dura[i+1]>0 and con[i+1]!= robot:
            con[i]=0
            con[i+1]= robot
            dura[i+1]-=1
            is_drop()
            # print(f"전진 : {dura}")

    #3.로봇이 벨트에 없는경우 내구성이 0보다 크다면 로봇을 올린다
    if con[0]!= robot and dura[0]>0:
        con[0]=robot
        dura[0]-=1
        # print(f"올릴 경우 :{dura}")
    count=Counter(dura)
    # print(count)
    if(count[0]>=K):
        print(answer)
        break
    
        
    