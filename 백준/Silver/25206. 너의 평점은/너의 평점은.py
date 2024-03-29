result =0
total_score=0
count=0
for i in range(20):
    name,score,my_grade = input().split()
    
    # score float형으로 변환
    score= float(score)

    if my_grade =="A+":
        grade = 4.5
    elif my_grade =="A0":
        grade = 4.0
    elif my_grade =="B+":
        grade =3.5
    elif my_grade =="B0":
        grade = 3.0
    elif my_grade =="C+":
        grade = 2.5
    elif my_grade=="C0":
        grade = 2.0
    elif my_grade =="D+":
        grade = 1.5
    elif my_grade =="D0":
        grade = 1.0 
    elif my_grade =="F":
        grade = 0.0
    #p인 경우 계산에서 제외
    else :
        grade=0.0
        score=0.0

    # 전체 학점
    total_score += score
    result += score*grade

my_result = result/total_score
print(my_result)