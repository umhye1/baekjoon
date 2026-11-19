# bridge_length : 다리에 올라갈 수 있는 트럭 수
# weight 이하의 무게를 견딜 수 있음

def solution(bridge_length, weight, truck_weights):
    
    time = 0 # 현재 시간
    total = 0 # 누적 무게 합
    count = 0 # 다리 위에 있는 트럭의 수
    idx = 0 # 다리 위에 있는 가장 오래된 트럭의 인덱스
    
    times = [0] * len(truck_weights) # i번째 트럭이 몇시에 나갈지 확인
    
    for i in range(len(truck_weights)) :
        while True:
            
            time += 1
            
            # 트럭 퇴장 조건 : 
            # 다리 가장 안쪽에 있는 차의 인덱스(idx) < 현재 들어갈 차의 인덱스(i)
            # idx의 퇴장시간 <= 현재 시간
            while idx < i and times[idx] <= time:
                total -= truck_weights[idx] # 총 무게에서 퇴장할 트럭의 무게 빼기
                count -= 1 # 다리 위에 있는 트럭의 수 하나 감소
                idx += 1 # 다음 트럭 
                
            # 다리에 올라갈 조건 :
            # 현재 트럭의 수 < 다리의 최대 수용 수 
            # 현재 트럭의 무게를 더한 총 무게 <= 다리 최대 수용 무게 
            if count < bridge_length and total + truck_weights[i] <= weight:
                count += 1 # 올리기
                total += truck_weights[i] 
                
                times[i] = time + bridge_length # 나가는 시간 계산 
                break
                
    
    return times[-1]