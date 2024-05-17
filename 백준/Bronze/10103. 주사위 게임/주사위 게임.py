T = int(input())
A,B=100,100
for i in range(T):
    a,b=map(int,input().split())
    if a<b : #a가 점수 잃는 경우
        A-=b
        
    elif b<a : #b가 점수 잃는 경우\
        B-=a
    
print(A,B)