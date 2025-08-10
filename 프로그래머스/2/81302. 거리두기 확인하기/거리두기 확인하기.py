# 북 동 남 서 (방향은 아무거나 4방이면 OK)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 만들고 나니 안쓰네
def manhetun(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def search_People(y, x, map):
    depth = 0
    queue = []
    visited = [[False]*5 for _ in range(5)]
    queue.append([y, x, depth])
    visited[y][x] = True

# BFS 로 depth=2 라면 맨해튼 거리 2 이므로 더이상 확장하지 않음으로 정의
    while queue:
        cur = queue.pop(0) 
        if cur[2] == 2:    
            continue

        for i in range(4):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]
            nd = cur[2] + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                if map[ny][nx] == 'X':  
                    continue
                if map[ny][nx] == 'P':
                    return False
                visited[ny][nx] = True
                queue.append([ny, nx, nd])

    return True

def solution(places):
    answer = []
    for x in places:          
        ok = True
        for i in range(5):
            for j in range(5):
                if x[i][j] == "P":
                    if not search_People(i, j, x):
                        ok = False
                        break
            if not ok:
                break
        answer.append(1 if ok else 0)
    return answer
