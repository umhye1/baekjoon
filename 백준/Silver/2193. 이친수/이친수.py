# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
# 재귀 쓰지 말고 메모이제이션 쓰기
N = int(input())

sol = [0]*max(3, N+1)

sol[1] = 1
sol[2] = 1

for i in range(3,N+1):
    sol[i] = sol[i-1]+ sol[i-2]

print(sol[N])



