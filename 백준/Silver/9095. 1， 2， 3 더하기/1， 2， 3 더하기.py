# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력
import sys
sys.setrecursionlimit(10**6)

def dfs(current_sum, idx):
    global count

    if idx > testcase :
        return

    # 1의 합으로 나타내는 방법의 수
    dfs(current_sum -1, idx+1)
        
    # 2의 합으로 나타내는 방법의 수
    dfs(current_sum -2, idx+1)

    # 3의 합으로 나타내는 방법의 수
    dfs(current_sum -3, idx+1)

    if current_sum == 0 :
        count += 1


n = int(sys.stdin.readline())


for _ in range(n):

    testcase = int(sys.stdin.readline())
    count =0 

    dfs(testcase,0)
    print(count)

