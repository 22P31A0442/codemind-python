n = int(input())
s=0
if n>0:
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
else:
    x = abs(n)
    while x!=0:
        r=x%10
        s=s*10+r
        x=x//10
    print(-s)