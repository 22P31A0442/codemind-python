n = int(input())
sq = n**2
q=n
s=0
while q!=0:
    r=q%10
    s=s+1
    q=q//10
x = 10**s
rr=sq%x
if rr==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    