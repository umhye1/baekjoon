# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이
# 몸무게 같으면(n) 무조건 시소 짝꿍이니까 빼야함 = nC2 만큼 답에 더하기
    

from collections import Counter


def solution(weights):
    
    answer = 0 # 시소짝꿍 수
    chook = [2,3,4]
    
    # 몸무게 같은 사람 수 체크
    counter = Counter(weights)
    # 몸무게 중복 없는 리스트
    no_same_weights = list(counter.keys())
    print(no_same_weights)
    
    
    # 시소 짝꿍 수 구하기  - 몸무게 같을 경우
    for i in counter.values():    
        if i >= 2:
            answer += (i*(i-1))//2
            

    # 시소 짝꿍 수 구하기 - 몸무게 다를 경우.. 4중 포문..?
    for i in range(len(no_same_weights)):
        for j in range(i+1, len(no_same_weights)):
            
            is_same = False 
            for a in chook:
                for b in chook:
                    if no_same_weights[i]*a == no_same_weights[j]*b:
                        is_same = True # 다른 축 돌아볼 필요 없음
                        break
                
                if is_same == True: 
                    break  
                    
            if is_same == True:
                answer += counter[no_same_weights[i]] * counter[no_same_weights[j]]
                
            
        
    
    
    return answer