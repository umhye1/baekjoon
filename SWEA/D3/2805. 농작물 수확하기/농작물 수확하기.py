T = int(input())

for case in range(1, T + 1):
    N = int(input())
    graphs = [list(map(int, input())) for _ in range(N)]

    answer = 0

    for i in range(N // 2): # 중간 전 까지만 (위와 아래의 범위가 같으니까)
        answer += sum(graphs[i][N // 2 - i : N // 2 + i + 1]) # 위쪽 그래프
        answer += sum(graphs[N - i - 1][N // 2 - i:N // 2 + i + 1]) # 아래쪽 그래프

    print(f"#{case} {answer + sum(graphs[N // 2])}") # graphs[N // 2] 는 한가운데의 값들
