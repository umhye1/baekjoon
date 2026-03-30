# X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
# X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
# X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
# X의 가운데 행을 X의 주 대각선으로 옮긴다.

T = int(input())

for _ in range(T):
    n,d = map(int, input().split())
    maplist = [list(map(int, input().split())) for i in range(n)]
    maplist2 = [row[:] for row in maplist]

    for _ in range(abs(d//45)):

        if d > 0: # 시계 방향
            for i in range(n):
                maplist2[i][((n+1)//2)-1] = maplist[i][i] 
                maplist2[n-i-1][i] = maplist[n-i-1][((n+1)//2)-1] 
                maplist2[((n+1)//2)-1][i] = maplist[n-i-1][i]
                maplist2[i][i] = maplist[((n+1)//2)-1][i]

        elif d < 0 : # 반 시계 방향

            for i in range(n):
                maplist2[i][i] = maplist[i][((n+1)//2)-1]
                maplist2[n-i-1][((n+1)//2)-1] = maplist[n-i-1][i]
                maplist2[n-i-1][i] = maplist[((n+1)//2)-1][i] 
                maplist2[((n+1)//2)-1][i] = maplist[i][i] 

        maplist = [row[:] for row in maplist2]
        
    
    for rows in maplist2:
        print(*rows)

        
            


