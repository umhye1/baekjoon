import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
n = int(sys.stdin.readline())  # 정렬할 숫자의 개수 입력
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

# 파이썬의 기본 정렬 함수 사용 (O(N log N))
a.sort()

# 정렬된 배열을 출력
for num in a:
    print(num)
