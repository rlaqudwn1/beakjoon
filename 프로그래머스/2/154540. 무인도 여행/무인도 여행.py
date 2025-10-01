import copy
from collections import deque

def solution(maps):
    # 문자열 지도를 2차원 리스트로 변환 (숫자는 int, 'X'는 str)
    map_list = []
    for row_str in maps:
        map_list.append([int(c) if c != 'X' else 'X' for c in row_str])

    rows = len(map_list)
    cols = len(map_list[0])
    
    # 방문 처리를 위한 지도 복사
    visited_map = copy.deepcopy(map_list) 
    
    # 상하좌우 이동 (델타값)
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1] 
    
    total_food_scores = []

    # 전체 지도 순회
    for r in range(rows):
        for c in range(cols):
            # 방문하지 않은 식량 덩어리('X'가 아닌) 발견 시 BFS 시작
            if visited_map[r][c] != 'X':
                
                current_food_sum = 0
                queue = deque([(r, c)])
                
                # 시작 노드 처리 및 방문 표시
                current_food_sum += visited_map[r][c]
                visited_map[r][c] = 'X'

                # BFS 실행
                while queue:
                    x, y = queue.popleft()
                    
                    # 4방향 탐색
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        # 경계 및 방문하지 않은 식량 확인
                        if 0 <= nx < rows and 0 <= ny < cols and visited_map[nx][ny] != 'X':
                            
                            # 식량 합산
                            current_food_sum += visited_map[nx][ny]
                            
                            # 방문 표시
                            visited_map[nx][ny] = 'X'
                            
                            # 큐에 추가
                            queue.append((nx, ny))
                
                # 하나의 덩어리 탐색 완료, 합계 저장
                total_food_scores.append(current_food_sum)

    # 결과 반환
    if not total_food_scores:
        # 식량 덩어리가 없으면 [-1] 반환
        return [-1]
    else:
        # 오름차순으로 정렬하여 반환
        return sorted(total_food_scores)