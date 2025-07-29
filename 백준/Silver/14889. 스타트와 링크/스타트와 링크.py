import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

# 최솟값을 찾기 위한 초기값. 무한대 의미
min_diff = float('inf')

# 사람 인덱스 리스트
people = [i for i in range(n)]


for team_a in combinations(people, n // 2):
    team_b = [p for p in people if p not in team_a]
    diff = abs(team_score(team_a) - team_score(team_b))
    min_diff = min(min_diff, diff)
    if min_diff == 0:
        break  # 최소값이 0이면 바로 종료

print(min_diff)
