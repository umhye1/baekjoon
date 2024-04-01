#  10진법 수 N과 B

N,B = map(str, input().split())

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B= int(B)
Q = int(N)

result =[]
while Q>0:
    Q1= Q//B 
    R = Q%B
    result.append(num[R])  
     
    if Q1==0 :
        if result[-1]==0:
            result.pop()
        break
    Q=Q1

result.reverse()  # 리스트를 역순으로 변환하여 B진법으로 표현
print(''.join(result))
