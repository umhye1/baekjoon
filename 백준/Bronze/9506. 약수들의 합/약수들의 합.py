import math

def divisor(a):
    divNum = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            divNum.append(i)
            if i != a // i and i != 1:  # i가 a의 제곱근이 아닌 경우 쌍으로 추가
                divNum.append(a // i)
    return divNum

def perfectNumber(a):
    divisors = divisor(a)
    sum_of_divisors = sum(divisors)
    return sum_of_divisors == a

n = int(input())

while n != -1:
    if perfectNumber(n):
        divisors = divisor(n)
        print(f"{n} = {' + '.join(map(str, sorted(divisors)))}")
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())  # 다음 숫자를 입력받아 n 업데이트
