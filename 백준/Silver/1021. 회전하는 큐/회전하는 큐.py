import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
queue = deque([i+1 for i in range(n)])
count = 0
location = list(map(int, sys.stdin.readline().split()))

for i in location :
    # 인덱스 이용해서 위치 구하기
    idx = queue.index(i)
    left = idx
    right = len(queue)-left

    if left < right : # 왼쪽으로 이동
        while queue[0] != i:
            queue.rotate(-1)
            count += 1

    else : # 오른쪽으로 이동
        while queue[0] != i :
            queue.rotate(1)
            count += 1


    if queue[0] == i :
        queue.popleft()
    
    

print(count)