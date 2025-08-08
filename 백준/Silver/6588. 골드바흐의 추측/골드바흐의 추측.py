import sys

nums = []
for line in sys.stdin:
    x = int(line)
    if x == 0 :
        break
    nums.append(x)

if not nums:
    sys.exit(0)

m = max(nums)

is_prime = [True] * (m+1)
is_prime[0] = is_prime[1] = False

p = 2

# 에라토스테네스의 체로 소수표 만들기
while p * p <= m:
    if is_prime[p]:
        step = p    # 몇 칸마다 지울 건지(어떤 소수의 배수?)
        start = p * p   # 지우기 시작할 위치
        is_prime[ start : m+1 : step] = [False] * (((m-start)//step)+1) # start부터 MAX까지 step 간격으로 있는 수들을 모두 소수 아님(False) 처리
    p += 1

out = []
for n in nums:
    found = False
    a = 3
    while a <= n // 2 :
        if is_prime[a] and is_prime[n-a]:
            out.append(f"{n} = {a} + {n-a}")
            found = True
            break
        a += 2
    if not found :
        out.append("Goldbach's conjecture is wrong.")

print("\n".join(out))


