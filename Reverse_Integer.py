x = int(input())
s=0
if x>0:
    while x!=0:
        r=x%10
        s=s*10+r
        x=x//10
    print(s)
else:
    n=abs(x)
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(-s)