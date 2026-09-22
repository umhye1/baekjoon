from collections import deque

def solution(players, m, k):
    answer = 0 # 서버 최소 몇번 증설?
    cur_server = 0 # 현재 돌아가는 서버 수 
    new_server = 0 # 그 시각에 새로 증설하는 서버 수
    count = deque()
    
    for i in range(len(players)):
        
        while count and count[0][0] + k <= i:
            time, server = count.popleft()
            cur_server -= server # 현재 돌아가는 서버 수 줄이기

        
        # 현재 돌아가는 서버 수가 감당할 수 있는 사용자 수보다 현재 사용자 수가 많을 경우 
        if ( players[i] // m ) > cur_server:
            new_server = (( players[i] // m ) - cur_server) # 서버 on
            cur_server += new_server
            answer += new_server # 새로 생길 때 바로 더하도록 !!1
            count.append((i,new_server)) # 현재 시각이랑 새로 증설된 서버 수를 넣음
        
            
            
    return answer