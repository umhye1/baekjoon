def solution(n, t, m, timetable):
    
    # 셔틀버스 시간표 
    shuttle = []
    for i in range(n):
        time = i * t + 540  # 9시
        
        hour = time // 60
        minute = time % 60
        shuttle.append(f"{hour:02d}:{minute:02d}")
    
    answer = shuttle[-1]
    print(shuttle)
    
    # timetable 정렬 및 23:59이면 집 보내기
    # timetable = [x for x in timetable if x != "23:59"] 
    timetable.sort()
    print(timetable)
    
    
    for shuttle_time in shuttle:
        count = 0   # 이번 셔틀에 타는 인원 count
        
        # 탈 사람 있는 경우 : timetable에서 pop (탐)
        while timetable and timetable[0] <= shuttle_time and count < m:
            last = timetable.pop(0)
            count += 1
            
        
        # 마지막 셔틀인 경우    
        if shuttle_time >= shuttle[-1] :
            
            # 마지막 사람이 셔틀보다 빨리왔는데, 인원 수 다 찬 경우 : 콘이 1분 빨리와야함
            if count >= m:
                print(count)
                hour,minute = map(int, last.split(":"))
                minute = hour * 60 + minute -1
            
                hour = minute // 60
                minute = minute % 60
    
                answer = f"{hour:02d}:{minute:02d}"
            
            
            # 셔틀버스시간이 타임테이블 시간보다 작은경우 -> 다음 셔틀로 넘어감 
            #  shuttle_time >= time and count == m 콘이 추가로 못 타는 경우 : 콘이 time -1분
            
            
            
                
                
                
                
    
    
    
    return answer