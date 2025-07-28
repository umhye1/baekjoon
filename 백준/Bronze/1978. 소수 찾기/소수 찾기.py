import sys
import math

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
result =0

# 소수 조건
# 1 과 자신만을 약수로 가질 것
# 2부터 해당 수의 제곱근까지 나누어 본다

def prime(number):
    global result
    if number == 1 :
        return False
    
    for i in range(2,int(math.sqrt(number))+1):
        if number % i ==0 :
            return False
        
    result += 1
    return 
    
for i in num:
    prime(i)
print(result)

