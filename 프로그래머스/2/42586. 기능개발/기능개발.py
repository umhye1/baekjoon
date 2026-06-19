# queue로 구현

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0 
    
    # 순서대로 처리하기 위해 인덱스로 접근
    idx = 0
    n = len(progresses)
    
    while idx < n :
        # 기능 개발 완료되었는지 확인
        if (progresses[idx] + time * speeds[idx]) >= 100 :
            count += 1 # 기능 수  += 1
            idx += 1  # 다음 기능으로 이동하기 위해 인덱스 +1 해줌
        
        else : 
            # count를 초기화 하지않고 기능개발 완료,
            # 인덱스 +1 해서 다음 기능으로 넘어갔기 때문에, 
            # 기존에 쌓여있떤 count를 일단 넘겨줘서 배포해야함
            if count > 0 :
                answer.append(count)
                count = 0 # 초기화 (기능 수 )
            
            # 기능 개발 완료 안된 경우 : 시간 +1하기
            time += 1 
    
    # 마지막으로 남은 기능 배포
    answer.append(count)
    
    
    return answer