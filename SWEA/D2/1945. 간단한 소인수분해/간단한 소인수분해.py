T = int(input())
s = [2,3,5,7,11]

for test_case in range(1,T+1):
    numlist = int(input())
    count = [0] * 5
    for i in range(5):
        while True:
            if numlist % s[i] == 0:
                numlist //= s[i]
                count[i] += 1
            else:
                break

    print(f"#{test_case}",*count, sep=" ")
