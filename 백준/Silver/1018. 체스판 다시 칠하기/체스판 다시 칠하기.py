# 아 이해했다 CNN 처럼 8*8 체스판을 찍어 놓고
# 왼쪽 상단이 W인 경우 B인 경우로 찍어놓고
# 거기서 틀린 값이 가장 작은 경우를 브루트 포스로 제출하면 됨
# 만약에 틀린 값이 없으면 바로 제출
import sys
space = 8
N,M = map(int,input().split())
board =[[]]
board.clear()
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))
Wboard=[[]]
Bboard=[[]]
Wboard.clear()
Bboard.clear()
count=float('inf')
# W로 먼저 시작하는 보드 B로 시작하는 보드 초기화
for i in range(8):
    if(i%2==0):
        Wboard.append(list("WBWBWBWB".strip()))
    else:
        Wboard.append(list("BWBWBWBW".strip()))
for i in range(8):
    if(i%2==0):
        Bboard.append(list("BWBWBWBW".strip()))
    else:
        Bboard.append(list("WBWBWBWB".strip()))

def find():
    global count
    for i in range(N-7):
        for j in range(M-7):
            subboard= [row[j:j+8] for row in board[i:i+8]]
            count=min(count,find2(subboard))
            if(count==0):
                return 0
def find2(board):
    Wcount=0
    Bcount=0
    for i in range(8):
        for j in range(8):
            if(board[i][j]!=Wboard[i][j]):
                Wcount+=1
            if(board[i][j]!=Bboard[i][j]):
                Bcount+=1
    return min(Bcount,Wcount)
find()
print(count)