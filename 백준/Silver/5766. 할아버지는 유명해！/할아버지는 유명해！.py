

while True:
    N,M = map(int,input().split())

    if N == 0 and M == 0:
        exit()

    rank = [0]*10001
    for i in range(N): # N주동안
        nlist = list(map(int, input().split()))
        for j in nlist:
            rank[j] += 1

    max_score = max(rank)
    second_score = 0

    for j in rank:
        if j < max_score:
            second_score = max(second_score, j) # 2등 점수 찾기

    count_second = []

    for j in range(len(rank)):
        if second_score == rank[j]:
            count_second.append(j)
    print(*count_second)
    
