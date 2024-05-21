import math

M = int(input())
N = int(input())
sumofDecimal=0
decimalNum=[]

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(M,N+1):
    if prime(i):
        decimalNum.append(i)
        sumofDecimal+=i
    else: 
        continue

if len(decimalNum)==0:
    print("-1")
else:
    print(sumofDecimal)
    print(decimalNum[0])



                


