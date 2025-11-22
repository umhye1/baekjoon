from collections import deque
for i in range(10):
    T = int(input()) # testnum
    numlist = deque(map(int, input().split()))

    while numlist[-1] > 0:
        count = 0
        for i in range(5):
            first_num = numlist.popleft()
            count += 1
            if first_num-count <= 0:
                numlist.append(0)
                break

            else :
                numlist.append(first_num-count)


    print(f"#{T}", end=" ")
    print(*numlist)