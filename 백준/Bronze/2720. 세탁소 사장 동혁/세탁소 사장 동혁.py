T = int(input())

for i in range(T):
    c = int(input())
    
    q = c//25
    c = c - (q*25)

    d = c//10
    c = c- (d*10)

    n = c//5
    c = c-(n*5)

    p = c//1

    print(q,d,n,p)
