import math

def solution(progresses, speeds):
    answer = []
    daylist = []
    
    # 1. 각 기능마다 완료까지 걸리는 일수 계산
    for i in range(len(progresses)):
        # (100 - 현재진도) / 속도 를 올림(ceil)하면 필요한 일수가 나옵니다.
        days = math.ceil((100-progresses[i])/speeds[i])
        daylist.append(days)

        
    # 2. 앞의 기능이 끝날 때 함께 배포될 기능들 그룹화
    # 기준일 (max_day) 초기화 : 첫 배포일
    max_day = daylist[0]
    count = 1    
    
    for i in range(1,len(daylist)):

        # 기준일(max_day)보다 일찍 끝나거나 같은 날 끝나면 함께 배포
        if max_day >= daylist[i]:
            count += 1
        
        # 기준일보다 오래 걸리는 기능을 만나면 (예: 9일)
        else:
            answer.append(count) # 지금까지 모인 기능 배포 
            max_day = daylist[i] # 새로운 기준일을 9일로 갱신
            count = 1
    
    # 루프가 끝난 뒤 마지막으로 남아있던 그룹을 넣어줍니다!
    answer.append(count)
    return answer