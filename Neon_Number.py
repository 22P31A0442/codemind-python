x = int(input())
f=0
s = x**2
while s!=0:
    r=s%10
    f=f+r
    s=s//10
if f==x:
    print("Neon Number")
else:
    print("Not Neon Number")