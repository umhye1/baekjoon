T = int(input())

for i in range(T):
    data = list(map(str,input().split()))
    result = float(data[0])


    for j in range (len(data)-1):
        if data[j+1]=="@" :
            result *= 3
        elif data[j+1] == "%":
            result +=5
        elif data[j+1] =="#":
            result-=7
    print(f'{result:0.2f}')


            
