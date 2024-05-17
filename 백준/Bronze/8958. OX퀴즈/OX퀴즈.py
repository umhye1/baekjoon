t = int(input())


for i in range(t):
    data =list(input()) 
    count=0
    result=0
    for j in range(len(data)):
        if data[j]=="O":
            count+=1
            result+=count
        elif data[j]=="X":
            count=0
    print(result)
    