T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print(f"#{test_case}")
    triangle = [[1]]

    for i in range(1,n):
        prev = triangle[i-1]
        row = [1]

        for j in range(len(prev)-1):
            row.append(prev[j]+ prev[j+1])

        row.append(1)
        triangle.append(row)
    for i in triangle:
        print(" ".join(map(str, i)))

