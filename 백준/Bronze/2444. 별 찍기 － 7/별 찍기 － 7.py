data = int(input())

for i in range(2*data-1):
    if (i < data):
        for a in range(data-i-1):
            print(" ",end="")

        for j in range(2*i+1):
            print("*", end="")
        print("")

    if (i>=data):
        for b in range(i-data+1):
            print(" ",end="")

        for x in range(4*data-2*i-3):
            print("*", end="")
        print("")   
