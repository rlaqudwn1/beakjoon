import sys
from collections import deque

# 표준 입력을 빠르게 처리하기 위한 설정
input = sys.stdin.readline

# 공간의 크기 N 입력
n = int(input())

# 공간 정보 입력 받기
space = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어의 초기 상태
shark_x, shark_y, shark_size = 0, 0, 2
# 초기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0 # 상어가 있던 자리는 빈칸으로 처리

# BFS를 통해 먹을 수 있는 물고기를 찾는 함수
def bfs(x, y, current_size):
    # (거리, x좌표, y좌표)를 저장할 큐
    q = deque([(0, x, y)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    
    # 먹을 수 있는 물고기들의 정보를 저장할 리스트
    eatable_fishes = []

    while q:
        dist, cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 1. 공간을 벗어나지 않고, 2. 방문하지 않았으며, 3. 상어보다 크거나 같은 물고기가 아닌 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and space[nx][ny] <= current_size:
                visited[nx][ny] = True
                q.append((dist + 1, nx, ny))
                
                # 먹을 수 있는 물고기인 경우 (0보다 크고 상어보다 작음)
                if 0 < space[nx][ny] < current_size:
                    eatable_fishes.append((dist + 1, nx, ny))
    
    # 거리 -> 행 -> 열 순으로 정렬하여 반환
    eatable_fishes.sort()
    return eatable_fishes

total_time = 0
eat_count = 0

# 메인 시뮬레이션 루프
while True:
    # 1. 현재 상어 위치에서 먹을 수 있는 물고기 찾기
    fishes = bfs(shark_x, shark_y, shark_size)

    # 2. 먹을 물고기가 없으면 종료
    if not fishes:
        break

    # 3. 가장 우선순위 높은 물고기 선택 (정렬 후 첫 번째)
    dist, fish_x, fish_y = fishes[0]

    # 4. 상태 업데이트
    total_time += dist # 시간 추가
    eat_count += 1
    
    space[fish_x][fish_y] = 0 # 물고기 먹기
    shark_x, shark_y = fish_x, fish_y # 상어 위치 이동

    # 5. 상어 성장 확인
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

# 최종 결과 출력
print(total_time)