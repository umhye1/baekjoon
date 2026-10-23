# n : 입국 심사를 기다리는 수 
# times : 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열
# 1,000,000,000명 : 10만개이상 -> 이분탐색, 그리디
    
def solution(n, times):
    answer = 0 # time 최솟값
    
    # 1. 구하고자 하는 대상 : 모든 사람이 심사를 받는데 걸리는 시간의 최솟값 
    # 
    # 2. left : 최하한선 - 1분
    # 3. right : 최상한선 - 1000000000분 / n * times 배열의 최댓값
    left = 1
    right = n * max(times)
    
    
    while left <= right :
        # 4. 중간값 mid = left+right /2  : 총 소요 시간
        mid = (left + right) // 2
        people = 0
        
        # 총 소요시간이 mid일 때, 각 심사관이 몇 명 처리할 수 있을지? - 역산
        for time in times:
            people += (mid // time) # 처리 가능한 사람 수
        
        if people >= n : # 최솟값을 구해야하므로 범위 줄이기
            right = mid - 1
            answer = mid # answer 업데이트
        
        if people < n :
            # 실패, 범위 넓히기
            left = mid + 1
        
                        
    
    return answer