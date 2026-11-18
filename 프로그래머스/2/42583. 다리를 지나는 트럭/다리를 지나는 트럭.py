# bridge_length : 다리에 올라갈 수 있는 트럭 수
# weight 이하의 무게를 견딜 수 있음

def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 모든 트럭이 다리를 건너려면 몇 초 걸리는지
    total = 0 # 누적 무게 합
    count = 0 # 다리 위에 있는 트럭의 수
    idx = 0 # 다리 위에 있는 가장 오래된 트럭의 인덱스
    
    time = [0] * len(truck_weights) # i번째 트럭이 몇시에 나갈지 확인
    
    for i in range(len(truck_weights)) :
        while True:
            
            answer += 1
        
            # 다리 가장 안쪽에 있는 차의 인덱스 < 현재 들어갈 차의 인덱스
            while idx < i and time[idx] <= answer:
                total -= truck_weights[idx]
                count -= 1
                idx += 1
                
            # 다리에 올리기 
            if count < bridge_length and total + truck_weights[i] <= weight:
                count += 1
                total += truck_weights[i] # 올림
                
                time[i] = answer + bridge_length # 나가는 시간 계산
                break
                
    
    return time[-1]