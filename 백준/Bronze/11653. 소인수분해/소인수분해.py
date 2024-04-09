import math

n= int(input())


def prime_factors(n):
    i=2
    while i<n :
        if n%i==0:
            n=n/i
            print(i)
        else : 
            i+=1
    print(int(n))
    
if n!=1:
    factors = prime_factors(n)
