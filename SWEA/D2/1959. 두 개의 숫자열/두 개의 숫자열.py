from collections import deque
T = int(input())

for test_case in range(1,T+1):
    n,m = map(int, input().split())
    a = deque(map(int,input().split()))
    b = deque(map(int,input().split()))

    if n>m:
        max_len = n
        min_len = m
        max_list = a
        min_list = b

    else:
        max_len = m
        min_len = n
        max_list = b
        min_list = a

    numlist = []
    num_shifts = max_len - min_len + 1

    for i in range(num_shifts):
        num = 0
        for j in range(min_len):
            num += (max_list[j] * min_list[j])

        numlist.append(num)

        if max_len != min_len and i <num_shifts -1 :
            max_list.popleft()

    print(f"#{test_case}", max(numlist))

