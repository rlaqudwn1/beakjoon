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
        
        # 현재 시간(cur_t)까지 도착한 모든 작업을 대기 큐(wait_queue)에 추가
        while job_index < jobs_count and all_tasks[job_index].start_t <= cur_t:
            task = all_tasks[job_index]
            heapq.heappush(wait_queue, task)
            job_index += 1
        # wait_queue 가 남아있으면 디스크 실행
        if not wait_queue:
            if job_index < jobs_count:
                cur_t = all_tasks[job_index].start_t
                continue 
            else:
                break
        
        next_task = heapq.heappop(wait_queue)
        
        finish_time = cur_t + next_task.require_t
        
        response_time = finish_time - next_task.start_t
        total_turnaround_time += response_time
        
        cur_t = finish_time
        
    return total_turnaround_time // jobs_count