import copy
from collections import deque
def solution(maps):
    answer=0
    h=len(maps)
    w=len(maps[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visited = copy.deepcopy(maps)
    queue=deque()
    queue.append([0,0,1])
    print(visited)
    visited[0][0]=0

    while(queue):
        cur=queue.popleft()
        if(cur[0]== h-1 and cur[1]== w-1):
            return cur[2]
        x=cur[1]
        y=cur[0]
        score=cur[2]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and visited[ny][nx]==1:
              queue.append([ny,nx,score+1])
              visited[ny][nx]=0     
    return -1
