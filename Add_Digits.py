n = int(input())
s=0
ss=0
sss=0
while n!=0:
    r=n%10
    s=r+s
    n=n//10
if s<10:
    print(s)
else:
    while s!=0:
        rr=s%10
        ss=rr+ss
        s=s//10
    if ss<10:
        print(ss)
    else:
        while ss!=0:
            rrr=ss%10
            sss=sss+rrr
            ss=ss//10
        print(sss)