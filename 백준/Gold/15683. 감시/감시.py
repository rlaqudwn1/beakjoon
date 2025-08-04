import copy
N, M =map(int, input().split())

# 4방향
dirs=[[-1,0],[0,1],[1,0],[0,-1]]
board=[[]]
board.clear()
for i in range(N):
    board.append(list(map(int, input().split())))

# 맵 복사
copymap= board.copy()

# cctv의 무빙 90도 회전
cctv_dirs = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}
#cctv 배열 담기
cctvs =[]
for y in range(N):
    for x in range(M):
        if board[y][x] in [1,2,3,4,5]:
            cctvs.append((y,x,board[y][x]))
min_counts=100000000
def dfs(depth,board):
    global min_counts
    if depth == len(cctvs):
        counts=count(board)
        # print(f"counts: {counts}")
        min_counts =min(counts,min_counts)
        return min_counts
    y,x,t = cctvs[depth]
    for dirs in cctv_dirs[t]:
        new_board = copy.deepcopy(board)
        simulate(new_board,y,x,dirs)
        dfs(depth+1, new_board)
        
# 사각지대 0 을 세는 함수
def count(board):
    count=0
    for i in range(N):
        for j in range(M):
            if(board[i][j]==0):
                count+=1
    return count

def in_range(board,y,x):
    return 0<=x and x<M and 0<=y and y<N and board[y][x]!=6

# 감시구역 마킹
def simulate(board,y,x,dir):
    nx=x
    ny=y
    for i in dir:
        while(True):
            nx+=dirs[i][1]
            ny+=dirs[i][0]
            if(in_range(board,ny,nx)):
                board[ny][nx]='#'
            else:
                break
        nx=x
        ny=y
    # print(*board)
    return board
dfs(0,board)
print(min_counts)