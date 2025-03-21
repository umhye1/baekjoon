# 메모리 제한이 있는 경우, heap, radix, 카운팅 정렬 등을 활용하는 것이 좋음 
# 근데 힙정렬도 반려먹어서 카운팅 정렬 사용
# 힙 정렬 사용 위해서는 heapq import 할 것

import sys

n = int(sys.stdin.readline())
count = [0] * 10001

for i in range(n):
    x = int(sys.stdin.readline())
    count[x] += 1   # 빈도수 저장

for i in range(1,10001):
    if count[i] >= 1:
        for _ in range(count[i]):
            print(i)

