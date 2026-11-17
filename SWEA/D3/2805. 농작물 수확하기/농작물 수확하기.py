def solup(n):
    ans = 0
    mid = n//2
    for i in range(mid):
        for j in range(mid-i, mid+i+1):
            ans += graph[i][j]

    return ans
   
def soldown(n):
    ans = 0
    mid = n//2
    for i in range(mid):
        for j in range(mid-i, mid+i+1):
            ans += graph[n-1-i][j]
    return ans

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
   n = int(input())
   graph = [list(map(int,input().strip())) for _ in range(n)]

   # 중간 부분 5//2 =2
   answer = sum(graph[n//2])
   answer += solup(n)
   answer += soldown(n)
   
   print(f"#{test_case} {answer}")

