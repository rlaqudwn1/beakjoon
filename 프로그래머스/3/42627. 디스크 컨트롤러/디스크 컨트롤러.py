import heapq

def solution(jobs):

    class Disk:
        def __init__(self, index, start_t, require_t):
            self.index = index
            self.start_t = start_t
            self.require_t = require_t
        
        def __lt__(self, other):
            # 1. 작업시간이 빠른것 
            if self.require_t != other.require_t:
                return self.require_t < other.require_t
            # 2. 시작 시간이 빠른 것
            if self.start_t != other.start_t:
                return self.start_t < other.start_t
            # 3. 작업의 번호가 작은 것 
            return self.index < other.index
        
        def __repr__(self):
            return f"Disk(I={self.index}, S={self.start_t}, R={self.require_t})"

    jobs_count = len(jobs)
    
    # disk job을 시작시간 기준으로 오름차순 정렬
    all_tasks = [Disk(i, j[0], j[1]) for i, j in enumerate(jobs)]
    all_tasks.sort(key=lambda task: task.start_t)
    
    cur_t = 0             
    job_index = 0         
    wait_queue = []      
    total_turnaround_time = 0
    
    # 모든 작업이 처리되거나, 미도착 목록과 대기 큐가 모두 빌 때까지 반복
    while job_index < jobs_count or wait_queue:
        
        # A. 현재 시간(cur_t)까지 도착한 모든 작업을 대기 큐(wait_queue/heap)에 추가
        while job_index < jobs_count and all_tasks[job_index].start_t <= cur_t:
            task = all_tasks[job_index]
            heapq.heappush(wait_queue, task)
            job_index += 1
        
        # B. 대기 큐(힙)가 비어있는 경우
        if not wait_queue:
            # 아직 도착하지 않은 작업이 남아 있다면, 다음 작업 도착 시점으로 시간을 점프
            if job_index < jobs_count:
                cur_t = all_tasks[job_index].start_t
                continue # A 단계로 돌아가서 그 시간에 도착한 작업들을 큐에 넣음
            else:
                # 모든 작업이 처리되고 미도착 작업도 없다면 종료
                break
        
        # C. 대기 큐에서 우선순위가 가장 높은 작업 (SJF) 선택
        next_task = heapq.heappop(wait_queue)
        
        # D. 작업 처리 및 시간/결과 업데이트
        
        # 1. 작업 시작 시점: 현재 시간(cur_t)
        # 2. 작업 완료 시점 계산
        finish_time = cur_t + next_task.require_t
        
        # 3. 응답 시간 (Response Time) 계산: (종료 시간) - (요청 시각)
        response_time = finish_time - next_task.start_t
        total_turnaround_time += response_time
        
        # 4. 현재 시간 업데이트: 다음 작업은 이 시점부터 시작 가능
        cur_t = finish_time
        
    # 최종 평균 응답 시간 계산
    return total_turnaround_time // jobs_count