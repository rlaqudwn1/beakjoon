# 1.순서를 바꾸지 말고 더하거나 빼서 타겟 넘버를 만든다
# 2. visit은 필요 없으며 numbers를 따라 +1 -1 을 하면서 target과 맞는지 확인해야 함
from collections import deque
answer=0
def DFS(numbers,target,num,current):
    global answer
    if num == len(numbers) and current==target:
        answer+=1
        return
    elif num == len(numbers):
        return
    DFS(numbers,target,num+1,current+numbers[num])
    DFS(numbers,target,num+1,current-numbers[num])
def solution(numbers, target):
    DFS(numbers,target,0,0)
    
    return answer