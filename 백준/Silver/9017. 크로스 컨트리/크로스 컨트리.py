t = int(input())

for _ in range(t):

    n = int(input())
    team_num = list(map(int, input().split()))

    teams = {}

    # 1️⃣ 팀별 선수 "위치"만 저장 (점수 X)
    for i in range(n):
        team = team_num[i]

        if team not in teams:
            teams[team] = []

        teams[team].append(i)  # i+1 ❌, 위치만 저장

    # 2️⃣ 6명 팀만 선별
    valid = []
    for team in teams:
        if len(teams[team]) == 6:
            valid.append(team)

    # 3️⃣ 유효 팀 선수에게만 점수 재부여
    scores = {team: [] for team in valid}

    score = 1
    for i in range(n):
        team = team_num[i]
        if team in scores:
            scores[team].append(score)
            score += 1

    # 4️⃣ 우승 팀 계산
    winner = -1
    best_score = 10**9
    best_fifth = 10**9

    for team in scores:
        total = sum(scores[team][:4])
        fifth = scores[team][4]

        if total < best_score:
            best_score = total
            best_fifth = fifth
            winner = team
        elif total == best_score and fifth < best_fifth:
            best_fifth = fifth
            winner = team

    print(winner)
