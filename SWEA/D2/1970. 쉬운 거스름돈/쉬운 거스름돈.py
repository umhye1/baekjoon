T = int(input())
m = [50000,10000,5000,1000,500,100,50,10]
for test_case in range(1,T+1):
    n = int(input())
    l = [0] * 8
    for i in range(len(m)):
        while m[i] <= n:
            n -= m[i]
            l[i] += 1

    print(f"#{test_case}")
    print(*l)