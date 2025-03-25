import sys

# 상근이가 가진 숫자 카드 N개의 수 입력
n = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))

# 주어진 M개의 수에 대해 카드가 존재하는지 확인
m = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

# 각 수가 상근이가 가진 카드에 있는지 확인
for x in queries:
    if x in cards:
        print(1,end=" ")
    else:
        print(0,end=" ")