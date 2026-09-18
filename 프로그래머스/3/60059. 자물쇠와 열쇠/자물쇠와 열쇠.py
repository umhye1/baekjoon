def rotate_key(key): # 90도 회전 함수
    m = len(key)
    new_key = [[0]*m for _ in range(m)]
    
    for r in range(m): # 행
        for c in range(m):
            new_key[c][m-r-1] = key[r][c]
            
    return new_key
        
    
def check(new_board, lock,m):  
    # board에 lock + key 했을 때 모두 1이 나오는지 확인하는 함수 (lock 범위만큼만)
    # m은 key 길이. new_board는 key+lock+key로 되어있기 때문에 row,col은 행이든 열이든 key만큼 더한거에서 시작 
    for row in range(len(lock)):
        for col in range(len(lock)):
            
            if new_board[row+m][col+m] != 1:
                return False
            
            
    return True
    
    

def solution(key, lock):
    answer = True
    
    # 1. 열쇠 회전 미리해두기 
    key_90 = rotate_key(key)
    key_180 = rotate_key(key_90)
    key_270 = rotate_key(key_180)
    
    rotated_keys = [key, key_90, key_180, key_270]
    
    
    # 2. board 따로 두기 -> 크기는 (N + 2*N), 가운데에 lock두기
    board_len = 2*len(key)+len(lock)
    board = [[0]*board_len for _ in range(board_len)]
    for r in range(len(lock)):
        for c in range(len(lock)):
            board[len(key)+r][len(key)+c] = lock[r][c]
    print(board)
    
    
    # 3. 자물쇠 풀리는 조건 - board에 lock범위만큼 lock + key 했을 떄 모든 값이 1이 될 경우 
    for rkey in rotated_keys : # 키회전한것마다
        for r in range(board_len - len(key)): # 새로운 보드 행 시작 위치 : key 배열을 맞춰보는거라 범위를 저렇게 해야함 
            for c in range(board_len - len(key)): # 새로운 보드 열 시작 위치
                
                import copy
                new_board = copy.deepcopy(board)
                
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_board[r+i][c+j] += rkey[i][j]
                
                if check(new_board,lock,len(key)):
                    return True
                else:
                    continue
    
    
    
    return False