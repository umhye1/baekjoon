for test_case in range(1,11):

    n = int(input())
    nlist = list(map(int, input().split()))

    count = 0

    for i in range(2,len(nlist)-2):
        if nlist[i]>nlist[i-2] and nlist[i]>nlist[i-1] and nlist[i]>nlist[i+1] and nlist[i]>nlist[i+2]:
            around = [nlist[i-2], nlist[i-1],nlist[i+1], nlist[i+2]]
            max_around = max(around)

            view = nlist[i] - max_around
            count += view

    print(f"#{test_case} {count}")