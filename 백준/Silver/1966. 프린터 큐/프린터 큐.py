import sys
from collections import deque

# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 문서의 중요도와 인덱스(위치) 를 같이 저장

num = int(sys.stdin.readline()) # test case num

for _ in range(num):
    # n : 문서의 개수
    # m : 큐에서 몇 번째에 놓여있는지를 나타내는 정수
    n,m = map(int, sys.stdin.readline().split())
    important_list = list(map(int,sys.stdin.readline().split()))
    
    # (문서의 인덱스, 중요도) 튜플로 저장
    # enumerate() : 리스트나 튜플 등 반복 가능한 객체에서 각요소의 인덱스 값을 동시에 꺼내는 내장함수
    # enumerate(iterable, start = 0 ) 
    # -> iterable : 반복 가능한 자료형(리스트, 문자열 등)
    # -> start : 인덱스 어디서부터 시작할지 나타냄
    result = deque((i,p) for i,p in enumerate(important_list))
    count = 0
    
    while result :

        idx, val = result.popleft()

        # 더 높은 중요도가 남아있다면 뒤로 보냄
        if any(val < other[1] for other in result):
            result.append((idx,val))
        else :
            count += 1
            if idx == m :
                print(count)
                break 
    