import sys
input = sys.stdin.readline

N,M = map(int, input().split())
numlist = list(map(int,input().split()))
numlist2=[0]

s= 0

for i in numlist :
    s += i
    numlist2.append(s) 

for i in range(M):
    a,b= map(int, input().split())
    print( numlist2[b]-numlist2[a-1])
