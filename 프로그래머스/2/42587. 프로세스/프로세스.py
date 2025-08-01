from collections import deque

# 1.실행 대기 큐에서 대기중인 프로세스를 하나 꺼낸다

# 큐
def solution(priorites, location):
    answer =0
    queue = deque(priorites)
    #목표 실행 프로세스 배열 locate
    locate = deque([0 for i in range(len(queue))])
    locate[location] = 1
    while(True):
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣는다
        if(queue[0] is max(queue)):
            queue.popleft()
# 2-2 만약 location 에 있는 원소라면 answer 리턴하고 종료
            if(locate[0]==1):
                answer +=1
                return answer
            locate.popleft()
            answer +=1
        else:
            queue.rotate(-1)
            locate.rotate(-1)

#     print(queue)
print(solution([1, 1, 9, 1, 1, 1],0))

# 3. 만약 꺼낸 프로세스가 가장 크다면 소각시킨다.