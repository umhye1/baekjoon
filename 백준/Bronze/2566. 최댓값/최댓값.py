data = []

for i in range(9):
    a = list(input().split())
    data.append(a)

max =0 

for i in range(9):
    for j in range(9):
        if max <= int(data[i][j]) :
            max = int(data[i][j])

print(max)

for i in range(9):
    for j in range(9):
        if max == int(data[i][j]) :
           print(i+1,j+1)
