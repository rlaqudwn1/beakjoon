from collections import deque

def rotate_board(board, r1, c1, r2, c2):
    path = []

    # 위
    for c in range(c1, c2):
        path.append(board[r1][c])
    # 오른쪽
    for r in range(r1, r2):
        path.append(board[r][c2])
    # 아래
    for c in range(c2, c1, -1):
        path.append(board[r2][c])
    # 왼쪽
    for r in range(r2, r1, -1):
        path.append(board[r][c1])

    dq = deque(path)
    dq.rotate(1)  # 시계 방향 회전

    i = 0
    # 다시 넣기
    for c in range(c1, c2):
        board[r1][c] = dq[i]; i += 1
    for r in range(r1, r2):
        board[r][c2] = dq[i]; i += 1
    for c in range(c2, c1, -1):
        board[r2][c] = dq[i]; i += 1
    for r in range(r2, r1, -1):
        board[r][c1] = dq[i]; i += 1

    return min(dq)

    
    
def solution(rows, columns, queries):
    answer = []
    board = [[r * columns +c + 1 for c in range(columns)] for r in range(rows)]
    for query in queries:
        r1,c1,r2,c2 = [ k-1 for k in query]
        answer.append(rotate_board(board,r1,c1,r2,c2))
        # for row in board:
            # print(row)    
    return answer