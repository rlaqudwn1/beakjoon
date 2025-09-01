import heapq
def solution(scoville, K):
    one =0
    two =0
    heapq.heapify(scoville)
    answer=0
    # 틀린 코드 런타임 에러가 발생하는 이유 추측 
    while(True):
        if scoville[0]>=K:
            return answer
        elif len(scoville)<=1:
            return -1
        one=heapq.heappop(scoville)
        two=heapq.heappop(scoville)
        new_scoville=one+(two*2)
        heapq.heappush(scoville, new_scoville)
        
        one=0
        two=0
        answer+=1
    
    return answer