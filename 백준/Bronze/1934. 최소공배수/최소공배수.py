t = int(input())

# 두 수의 최대공약수를 구하는 함수
# 여기서 a와 b는 두 수를 나타냅니다. a는 더 큰 수를, b는 작은 수를 나타냅니다. 그리고 a % b는 a를 b로 나눈 나머지를 계산한 값입니다.

# 이 과정을 통해 b가 0이 되는 순간, 즉 두 수 중 하나가 다른 수로 나누어 떨어지는 경우에는 루프를 종료하고, a에는 최대공약수가 저장됩니다. 이 최대공약수를 반환하여 사용할 수 있게 됩니다.
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 두 수의 최소공배수를 구하는 함수
def LCM(a, b):
    return a * b // GCD(a, b)

for i in range(t):
    a, b = map(int, input().split())
    print(LCM(a, b))
