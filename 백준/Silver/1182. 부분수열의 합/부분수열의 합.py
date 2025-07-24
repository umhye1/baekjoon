# 부분 수열의 합  = itertools의 combinations 아니면 dfs/백트래킹이 적합
import sys

def dfs(idx, current_sum) :
    global count

    # 모든 원소 다 검사했을 때 종료
    if idx == n :
        if s == current_sum :
            count += 1
        return
    
    # 현재값 포함하는 경우
    dfs(idx+1,current_sum + nums[idx])
    
    #현재값 포함 안하는 경우
    dfs(idx+1, current_sum)



n,s = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

count = 0
dfs(0,0)

if s == 0: # 공집합 제거
    count -= 1

print(count)