# 시간 초과 -> set() 사용 
# set 자료구조는 탐색, 삽입, 삭제가 O(1)

import sys

n = int(sys.stdin.readline())
result = 0

# 중복 여부 확인
col_set = set() # col
diag1 = set() # row + col
diag2 = set() # row - col

def dfs(row):
    global result
    if row == n : # 퀸 n개 다 사용
        result += 1
        return
    
    for col in range(n):
        if col in col_set or (row + col) in diag1 or (row - col) in diag2:
            continue # 대각선, 열이면 공격당함. 제외시키기
    
         # 퀸 배치
        col_set.add(col)
        diag1.add(row + col)
        diag2.add(row - col)

        dfs(row + 1)

        # 퀸 제거 - 백트래킹
        col_set.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)


dfs(0)
print(result)


    