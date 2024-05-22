while True:
    a,b,c = map(int,input().split())
    x=[a,b,c]
    
    if a==0 and b==0 and c==0:
        break

    elif max(x)<sum(x)-max(x):
        if a==b and b==c and c==a:
            print("Equilateral")

        elif a==b or b==c or c==a:
            print("Isosceles")

        else:
            print("Scalene")
      
    else:
        print("Invalid")
