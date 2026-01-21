n = int(input())
score = {}
score1 = 0
score2 = 0
ans1, ans2 = 0,0
last_time = 0

for _ in range(n):
    team_num , gt = map(str, input().split())
    goal_time = int(gt[:2])*60 + int(gt[3:])
    

    if score1 > score2:
        ans1 += (goal_time - last_time)
    
    if score1 < score2 :
        ans2 += (goal_time - last_time)

    # 팀 점수 반영
    if team_num == "1" :
        score1 += 1

    if team_num == "2":
        score2 += 1

    last_time = goal_time

if score1 > score2:
    ans1 += 48*60 - last_time

if score2 > score1:
    ans2 += 48*60 - last_time

print(f"{ans1//60:02d}:{ans1%60:02d}")
print(f"{ans2//60:02d}:{ans2%60:02d}")