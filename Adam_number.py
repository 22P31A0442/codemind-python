n = int(input())
sq = n**2
q=n
s=0
f=0
while q!=0:
    r=q%10
    s=s*10+r
    q=q//10
sqq = s**2
x=sqq
while x!=0:
    rr=x%10
    f=f*10+rr
    x=x//10
if f==sq:
    print("True")
else:
    print("False")