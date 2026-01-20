n,m = map(int, input().split())
cur = list(map(int, input().split()))
for i in range(m):
    a,b,c = map(int, input().split())
    if a == 1:
        cur[b-1] = c

    else : 
        length = c-b+1
        if a == 2: #  l번째부터 r번째까지의 전구의 상태를 변경한다
            for j in range(length):
                if cur[b+j-1] == 0:
                    cur[b+j-1] = 1
                else :
                    cur[b+j-1] = 0

            
        elif a == 3: #  l번째부터 r번째까지의 전구 끔(0)
            for j in range(length):
                cur[b+j-1] =0


        elif a ==4 : #  l번째부터 r번째까지의 전구 킴(1)
            for j in range(length):
                cur[b+j-1] =1

print(" ".join(map(str,cur)))