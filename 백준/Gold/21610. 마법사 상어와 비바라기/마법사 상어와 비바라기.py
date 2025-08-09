import itertools

N, M = map(int, input().split())

# 물의 양 박스
A = [list(map(int, input().split())) for _ in range(N)]
# 이동 명령 (d, s)
B = [list(map(int, input().split())) for _ in range(M)]

# 구름 박스
C = [[0 for _ in range(N)] for _ in range(N)]
cloud = 'c'
# 8방향
dx = [0,  0, -1, -1, -1, 0,  1,  1,  1]
dy = [0, -1, -1,  0,  1, 1,  1,  0, -1]

# 대각(물복사) 네 방향
diax = [-1, -1, 1,  1]
diay = [-1,  1, -1, 1]

def cloud_create():
    # 초기 구름 4칸 
    C[N-1][0] = cloud
    C[N-1][1] = cloud
    C[N-2][0] = cloud
    C[N-2][1] = cloud

def water_bug(moved_cells):
    
    for x, y in moved_cells:
        cnt = 0
        for k in range(4):
            nx = x + diax[k]
            ny = y + diay[k]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt

def move(d, s):
    # d방향으로 s칸 이동 (동시)
    s %= N  # 원형 최적화

    # 1) 현재 구름 좌표 스냅샷 & 비우기
    clouds = [(i, j) for i in range(N) for j in range(N) if C[i][j] == cloud]
    for i, j in clouds:
        C[i][j] = 0

    # 2) 이동 후 배치 + 비 내림(+1)
    moved = []
    for x, y in clouds:
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        moved.append((nx, ny))
    for x, y in moved:
        C[x][y] = cloud
        A[x][y] += 1

    # 3) 물복사 버그
    water_bug(moved)

    # 4) 기존(이번 턴) 구름 소멸
    for x, y in moved:
        C[x][y] = 0

    # 5) 새 구름 생성
    moved_set = set(moved)
    for i in range(N):
        for j in range(N):
            if (i, j) not in moved_set and A[i][j] >= 2:
                C[i][j] = cloud
                A[i][j] -= 2


# 실행
cloud_create()  
for d, s in B:
    move(d, s)

print(sum(itertools.chain.from_iterable(A)))
