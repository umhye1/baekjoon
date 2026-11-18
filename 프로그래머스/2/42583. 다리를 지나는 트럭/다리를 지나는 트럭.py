# bridge_length : 다리에 올라갈 수 있는 트럭 수
# weight 이하의 무게를 견딜 수 있음

def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 모든 트럭이 다리를 건너려면 몇 초 걸리는지
    total = 0 # 누적 무게 합
    count = 0 # 다리 위에 있는 트럭의 수
    idx = 0 # 다리 위에 있는 가장 오래된 트럭의 인덱스
    
    for i in range(len(truck_weights)) :
        while True:
        
    ## 2.
        # count = 1
        # bridge_length = 2
        # total = 7
        # truck_weights[1] = 4
        # weight = 10
        
        # 1 <= 2 and 7 + 4 <= 10 : false
        # total = 
        # answer = 2
        
            # 다리 가장 안쪽에 있는 차의 인덱스 < 현재 들어갈 차의 인덱스
            
            while idx < i :
                total -= truck_weights[idx]
                count -= 1
                idx += 1
                
            if count < bridge_length and total + truck_weights[i] <= weight:
                count += 1
                total += truck_weights[i]

            # 하나 내보낼 조건
            # 1) 다리 무게 초과할 경우
            # 2) 다리 위에 있는 차의 수가 동일할 경우
            if total + truck_weights[i] > weight or count == bridge_length:
                total -= truck_weights[idx] # 가장 오래있었던거 빼야함 - 인덱스로 처리..하기          
                answer += 1
                count -= 1
                idx += 1


            answer += 1
        
    
    return answer