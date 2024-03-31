data = list(input())

count = len(data)
i = 0

while i < len(data) - 1:  # 여기서 -1을 추가하여 마지막 인덱스를 초과하지 않도록 합니다.

    if data[i] == "c":
        if data[i + 1] == "=":
            count -= 1
            i += 1  # 조건이 맞을 때에만 인덱스를 증가시킵니다.
        elif data[i + 1] == "-":
            count -= 1
            i += 1

    elif data[i] == "d":
        if data[i + 1] == "z" and i < len(data) - 2:  # i가 len(data)-2보다 작은 경우에만 접근합니다.
            if data[i + 2] == "=":
                count -= 2
                i += 2
        elif data[i + 1] == "-":
            count -= 1
            i += 1

    elif data[i] == "l":
        if data[i + 1] == "j":
            count -= 1
            i += 1

    elif data[i] == "n":
        if data[i + 1] == "j":
            count -= 1
            i += 1

    elif data[i] == "s":
        if data[i + 1] == "=":
            count -= 1
            i += 1

    elif data[i] == "z":
        if data[i + 1] == "=":
            count -= 1
            if i != 0 and data[i - 1] == "d":
                count += 1
            i += 1

    i += 1

print(count)
