import sys
from collections import deque

# 입력 속도 개선 및 데이터 파싱
input = sys.stdin.read
data = input().split()

if not data:
    print(-1)
else:
    N = int(data[0])
    M = int(data[1])

    # 맵 데이터 (0: 이동 가능, 1: 벽)
    Map = []
    data_idx = 2
    for i in range(N):
        row = list(data[data_idx + i])
        Map.append([int(x) for x in row])

    # 3차원 방문 배열: visited[r][c][0] (벽X), visited[r][c][1] (벽O)
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    # 상하좌우 이동 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs():
        # 큐: (행 r, 열 c, 벽 부쉈는지 여부 broken)
        queue = deque([(0, 0, 0)])
        visited[0][0][0] = 1  

        while queue:
            r, c, broken = queue.popleft()

            # 목적지 도착 시 최단 거리 반환
            if r == N - 1 and c == M - 1:
                return visited[r][c][broken]

            # 상하좌우 탐색
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 맵 범위 체크
                if 0 <= nr < N and 0 <= nc < M:
                    # 1. 이동할 곳이 벽('1')일 때
                    if Map[nr][nc] == 1:
                        # 아직 벽을 안 부쉈다면 (broken == 0), 벽을 부수고 이동 (broken = 1)
                        if broken == 0 and visited[nr][nc][1] == 0:
                            visited[nr][nc][1] = visited[r][c][0] + 1
                            queue.append((nr, nc, 1))
                    
                    # 2. 이동할 곳이 빈 공간('0')일 때
                    else:
                        # 현재 broken 상태 유지하며 이동. 미방문 칸만 추가
                        if visited[nr][nc][broken] == 0:
                            visited[nr][nc][broken] = visited[r][c][broken] + 1
                            queue.append((nr, nc, broken))
        
        # 도달 불가 시 -1 반환
        return -1
    print(bfs())