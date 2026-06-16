from collections import deque

def bfs(words, visited, t):
    q = deque()
    q.append(0)
    visited[0] = 0
    
    while q:
        cur_x = q.popleft()
        
        if words[cur_x] == t:
            return visited[cur_x]
        
        for next_x in range(len(words)):
            
            if visited[next_x] == -1: # 방문 조건
                diff_count = 0
                
                # 알파벳이 하나만 다른 경우 count
                for i in range(len(words[0])):
                    if words[cur_x][i] != words[next_x][i]:
                        diff_count += 1

                if diff_count == 1:
                    q.append(next_x) # 다음 인덱스 위치
                    visited[next_x] = visited[cur_x] + 1

    return 0


def solution(begin, target, words):
    answer = 0
    n = len(words)
    
    words.insert(0,begin)
    n = len(words)
    visited = [-1] * n
    
    if target not in words:
        return 0
    
    answer = bfs(words, visited, target)
    
    
    return answer