N,Q = map(int, input().split())
score = list(map(int, input().split()))
fake_num = list(map(int, input().split()))
length = len(score)


def calc(idx):
    # 바뀐 값 계산
    t = 0
    for j in range(idx-3,idx+1):
        t += score[j%length] * score[(j+1)%length] * score[(j+2)%length] * score[(j+3)%length]
   
    return t


total = 0
# 총 점수 구하기
for j in range(length):
    total += score[j] * score[(j+1)%length] * score[(j+2)%length] * score[(j+3)%length]
    

for i in range(len(fake_num)):

    # total에서 옛날 꺼 빼기
    total -= calc(fake_num[i]-1)

    # 부호 바꾸기
    score[fake_num[i]-1] = -score[fake_num[i]-1]

    # 새로운 값 계싼
    total += calc(fake_num[i]-1)
    
    print(total)

