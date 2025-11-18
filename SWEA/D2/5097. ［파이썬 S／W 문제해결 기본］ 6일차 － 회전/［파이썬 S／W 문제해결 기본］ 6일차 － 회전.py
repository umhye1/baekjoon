T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    numlist = list(map(int,input().split()))
    M = M % N
    for _ in range(M):
        f = numlist.pop(0)
        numlist.append(f)
 
    # ///////////////////////////////////////////////////////////////////////////////////
    print(f"#{test_case} {numlist[0]}")
    # ///////////////////////////////////////////////////////////////////////////////////
