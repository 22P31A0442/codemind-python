n = int(input())
s=0
f=0
x=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
if s<10:
    print(s)
else:
    while s!=0:
        rr = s%10
        f=f+rr
        s=s//10
    if f<10:
        print(f)
    else:
        while f!=0:
            rrr = f%10
            x = x+rrr
            f=f//10
        print(x)