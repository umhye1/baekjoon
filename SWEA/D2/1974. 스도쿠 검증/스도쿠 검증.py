T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def check_rows(graph):

    for i in range(9):
        rowlist = set(graph[i])

        if len(rowlist)!=9:
            return 0

    return 1


def check_cols(graph):
    for j in range(9):
        collist = []
        for i in range(9):
            collist.append(graph[i][j])

        colset =  set(collist)
        if len(colset) != 9:
            return 0

    return 1



def check_three(graph):
    for row_start in range(0,9,3):
        for col_start in range(0,9,3):
            boxlist= []
            for j in range(3):
                for i in range(3):
                    boxlist.append(graph[row_start+i][col_start+j])

            boxset = set(boxlist)
            if len(boxset) != 9:
                return 0

    return 1

for test_case in range(1, T + 1):

    x, y = 0, 0
    graph = [list(map(int, input().split())) for _ in range(9)]
    # ///////////////////////////////////////////////////////////////////////////////////

    if check_rows(graph) and check_cols(graph) and check_three(graph):
        print(f"#{test_case} 1")

    else:
        print(f"#{test_case} 0")

