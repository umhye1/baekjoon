# 5분, 1분, 10초
T = int(input())

A = 300
B = 60
C =10

countA=0
countB=0
countC=0

while T != 0:
    if T<10:
        print("-1")
        break

    elif T<60:
        T-=10
        countC+=1

    elif T>= 60 and T<300:
        T-=60
        countB+=1

    elif T>=300:
        T-=300
        countA+=1
if T==0:
    print(countA,countB,countC)

