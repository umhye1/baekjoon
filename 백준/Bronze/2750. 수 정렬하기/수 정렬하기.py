# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())
a=[]

for i in range(n):
    n =int(input())
    a.append(n)

a.sort()

for i in range(len(a)):
    print(a[i])