T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    rotate90 = [[0] * n for _ in range(n)]
    rotate180 = [[0] * n for _ in range(n)]
    rotate270 = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            r_90, c_90 =c, n-1-r
            rotate90[r_90][c_90] = grid[r][c]

            r_180, c_180 = n - 1 - r, n - 1 - c
            rotate180[r_180][c_180] = grid[r][c]

            r_270, c_270 = n - 1 - c, r
            rotate270[r_270][c_270] = grid[r][c]


    print(f"#{test_case}")
    for i in range(n):
        print(*rotate90[i], sep="", end=" ")
        print(*rotate180[i],sep="", end=" ")
        print(*rotate270[i], sep="")



