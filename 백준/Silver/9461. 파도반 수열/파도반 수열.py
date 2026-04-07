t = int(input())

sol= [0]*max(5,101)
sol[0] = 1
sol[1] = 1
sol[2] = 1
sol[3] = 2
sol[4] = 2


for i in range(t):
    n = int(input())
    for i in range(5,n):
        sol[i] = sol[i-5] + sol[i-1]

    print(sol[n-1])
