n = int(input())
i = 1
count = 1

while n > 1:
    n -= 6 * i
    i += 1
    count += 1

print(count)
