def solution(name):
    udcount = 0
    lrcount = len(name) - 1
    
    for i in range(len(name)):
        # 상하 : a -> z  / z -> a  중 최솟값 count
        up_count = ord(name[i]) - ord('A')
        down_count = ord('Z') - ord(name[i]) + 1
        udcount += min(up_count, down_count)
        
        # 좌우 : 정 / A 나오는 곳을 기점으로 정 -> 역 / 역 중 최솟값 count
        # 좌우의 경우, 정, 역은 모두 name 길이
    
    
    for i in range(len(name)):
        # A 위치 찾기 
        # A가 연속적으로 나오는 곳을 찾기 - 그만큼 안가도 됨
        idx = i+1   # A 마지막 위치 + 1
        
        while idx < len(name) and name[idx] == 'A':
            idx += 1
            
        forward_count = len(name) - 1   # 정방향, 역방향
        reverse1_count = i * 2 + len(name) - idx    # 정 -> 역 
        reverse2_count = (len(name) - idx ) * 2 + i     # 역 -> 정
        
        # 매번 좌우 이동 값 갱신
        lrcount = min(lrcount, forward_count, reverse1_count, reverse2_count)    
        
        
    
    return udcount + lrcount