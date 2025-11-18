T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    numlist = list(map(int, input().split()))
    numlist.sort()
    r = []
    count  = [0]*(len(numlist)+1)
    # ///////////////////////////////////////////////////////////////////////////////////
    for i in numlist:
        count[i] +=1
    #max구하기 - 2개 이상일 경우, 가장 큰 값
    m = max(count)
    
    for i in range(len(count)):
        if count[i] == m:
            r.append(i)
    result = max(r)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
