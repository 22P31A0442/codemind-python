n = int(input())
s=0
f=1
while n!=0:
    r=n%10
    s=s+r
    f=f*r
    n=n//10
print(abs(s-f))