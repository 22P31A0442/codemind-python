n = int(input())
s=0
f=0
x=0
q=n
while q!=0:
    r=q%10
    s=s*10+r
    q=q//10
for i in range(1, n+1):
    if n%i==0:
        f=f+1
for j in range(1, s+1):
    if s%j==0:
        x=x+1
if f==2 and x==2:
    print("circular prime")
elif f==2 and x!=2:
    print("prime but not a circular prime")
else:
    print("not prime")