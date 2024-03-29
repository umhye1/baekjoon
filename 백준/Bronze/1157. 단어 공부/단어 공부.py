data = list(input().upper())
counts = []
data1 = list(set(data))

for i in range(len(data1)):
    counts.append(data.count(data1[i]))

if counts.count(max(counts)) >= 2:
    print("?")

else:
    idx = counts.index(max(counts))
    print(data1[idx])