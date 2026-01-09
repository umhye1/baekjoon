import sys
n, m = map(int, sys.stdin.readline().split())

# 딕셔너리 사용, key = 단어, value = 횟수
count = {}

for _ in range(n):
    w = sys.stdin.readline().rstrip()

    if len(w) >= m:

        if w in count:
            count[w] += 1 # value 1씩 증가

        else:
            count[w] = 1

# 정렬
sorted_words = sorted(
    count.keys(),
    key=lambda x: (-count[x], -len(x), x)
)

print('\n'.join(sorted_words))

    