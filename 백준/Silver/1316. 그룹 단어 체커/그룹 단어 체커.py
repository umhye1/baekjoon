N = int(input())

group=0

for i in range (N) :
    data =list(input())
    count = len(data)

    for i in range(len(data)-1):

        if data[i]==data[i+1] :
            count-=1
    if len(set(data)) == count :
        group+=1

print(group)