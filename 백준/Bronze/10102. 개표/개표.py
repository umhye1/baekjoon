v = int(input())
vote = list(input())
count_A=0
count_B=0
for i in range(v):
    if vote[i] == "A":
        count_A +=1
    if vote[i] == "B":
        count_B +=1

if count_A>count_B:
    print("A")
elif count_A<count_B:
    print("B")
else :
    print("Tie")