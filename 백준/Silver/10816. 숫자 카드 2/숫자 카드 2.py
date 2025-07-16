# 딕셔너리 사용

import sys
from collections import Counter #딕셔너리 클래스

# 상근이가 가지고 있는 숫자 카드의 개수 N
n = int(sys.stdin.readline())
# 숫자 카드에 적혀있는 정수
card = list(sys.stdin.readline().split())

# M
m = int(sys.stdin.readline())
# 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수
num_find = list(sys.stdin.readline().split())

counts = Counter(card)
result = [str(counts[x]) for x in num_find]
print(' '.join(result))

