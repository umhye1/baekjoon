
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 조망권 : 양쪽 모두 거리 2 이상의 공간이 확보될 때
def check_left(x):
    answer = 0
    for i in range(1,3):
        answer = max(answer,graph[x-i])
    
    return answer

def check_right(x):
    answer = 0
    for i in range(1,3):
        answer = max(answer,graph[x+i])

    return answer

for test_case in range(10):
    n = int(input()) # 건물의 개수
    graph = list(map(int, input().split()))
    ngraph = [0] * n
    r = 0

    for i in range(2,n-2):
        left = check_left(i)
        right = check_right(i)

        if left >= graph[i] or right >= graph[i]:
            continue

        else :
            r += ( graph[i] -  max(left, right))



    print(f"#{test_case + 1} {r}")