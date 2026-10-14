# heap
import heapq

# 소요 시간, 요청 시간, 번호 순
# 1) 하드디스크 작업 x
# 2) 대기 큐 작업 x
# -> 우선 순위 가장 높은 것 꺼내서 하드디스크에 작업시키기

# 모든 요청 작업의 반환 시간의 평균의 정수 부분 리턴

def solution(jobs):
    answer = []
    jobs.sort(key = lambda x: x[0]) # 들어오는 순서대로 정렬
    
    count = 0 # 처리한 작업의 수
    time = 0 # 현재 시각
    idx = 0 
    heap = []
    n = len(jobs)
    
    
    while count < n:
        
        # 다 훑지 않았고, 요청 시간 <= 현재 시각이면 우선순위큐에 넣기
        while idx < n and jobs[idx][0] <= time : 
            processing_t = jobs[idx][1] # 소요 시간
            required_t = jobs[idx][0] # 요청 시간
            heapq.heappush(heap,(processing_t, required_t, idx))
            idx += 1 # 번호
            
        
        # 대기큐(heap)에 처리할 거 있다면
        if heap : 
            processing_t, required_t, num = heapq.heappop(heap) # 작업 처리
            # 현재 시간을 time + procesing_t로 업데이트
            time += processing_t # 작업종료시간
            count += 1 
            answer.append(time-required_t) # 반환시간
        
        else :
            time = jobs[idx][0]
            
        
    return sum(answer)//len(answer)