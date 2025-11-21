from collections import deque
T = int(input())

def check(queue):
    length = len(queue)
    count = 0
    if len(queue)%2 == 0:

        for i in range(length//2):
            a = queue.pop()
            b = queue.popleft()

            if a==b :
                count += 1

    else :
        for i in range(length//2):
            a = queue.pop()
            b = queue.popleft()

            if a == b :
                count += 1

    if count == length//2:
        return 1
    else:
        return 0


for test_case in range(1,T+1):
    word = input()

    queue = deque(word)
    result = check(queue)

    print(f"#{test_case} {result}")

