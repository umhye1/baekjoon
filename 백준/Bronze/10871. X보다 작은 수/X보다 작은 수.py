n,x =map(int,input().split())
a = list(map(int, input().split()))

for i in range(n):
    if (a[i]<x):
        print(a[i], end =" ")

#한 칸씩 띄어쓰도록 만드려면 end = " " 쓰기


