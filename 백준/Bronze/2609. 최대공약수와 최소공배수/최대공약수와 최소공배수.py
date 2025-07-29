import sys
import math

n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)

# 최대공약수
# 유클리드 호제법 : 2개의 자연수 a, b에 대해 a를 b로 나눈 나머지를 r이라 하면
#               a와 b 의 최대공약수는 b와 r의 최대공약수와 같음
#               b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복해 나머지가 0이 되었을 때 나누는 수가 최대공약수

def gcd(n,m):
    global gcd_num 
    if n > m :
        a = n
        b = m
    else :
        a = m
        b = n

    r = a % b

    if r == 0 :
        gcd_num = b
        return
    
    gcd(b,r)


# 최소공배수 = 두 자연수의 곱 / 최대공약수
def lcm(n,m):
    global lcm_num
    lcm_num = n*m/gcd_num
    return


gcd(n,m)
print(gcd_num)
lcm(n,m)
print(math.trunc(lcm_num))
