n = int(input())
s=0
ss=0
sq = n**2
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
rs=s**2
while rs!=0:
    rr=rs%10
    ss=ss*10+rr
    rs=rs//10
if sq==ss:
    print("True")
else:
    print("False")