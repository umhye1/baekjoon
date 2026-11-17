def find(x):
    # 가로
    if len(set(graph[x])) != 9:
        return False
        
    # 세로
    cgraph = set()
    for i in range(9):
        cgraph.add(graph[i][x])

    if len(cgraph) != 9:
        return False

    # 3*3
    tgraph = set()
    for i in range(3):
        for j in range(3):
            #row_start = (x // 한_줄의_상자_개수) * 상자_높이
            #col_start = (x % 한_줄의_상자_개수) * 상자_너비
            tgraph.add(graph[(x//3)*3+i][(x%3)*3+j])
    
    if len(tgraph) != 9:
            return False

    return True



T = int(input())
for test_case in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    answer = 1 # 겹치는 숫자가 없을 경우

    for i in range(9):
        if not find(i):
            answer = 0
            break

    print(f"#{test_case} {answer}")