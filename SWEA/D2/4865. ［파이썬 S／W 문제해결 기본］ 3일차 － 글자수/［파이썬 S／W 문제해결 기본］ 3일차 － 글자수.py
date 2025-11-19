T = int(input())
for test_case in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    freq_list = {}
    for i in str2:
        freq_list[i] = freq_list.get(i, 0) + 1

    max_count = 0
    unique_str1 = set(str1)
    for i in unique_str1:
        count = freq_list.get(i, 0)
        if count > max_count:
            max_count = count

    print(f"#{test_case} {max_count}")