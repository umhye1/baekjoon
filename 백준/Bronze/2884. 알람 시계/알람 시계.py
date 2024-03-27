H, M = map(int, input().split())

if(H<24)&(M<60):
    if (M<45) :
        if(H==0):
            H = H+23
            M = 60+M-45
            print(H,M)

        else:
            H = H-1
            M = 60+M-45
            print(H,M)
    else :
        if(H==0):
            M = M-45
            print(H,M)
        else:
            M = M-45
            print(H,M)
else:
    print("error")