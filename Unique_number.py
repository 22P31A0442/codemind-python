n = int(input())
s=0
f=0
x = str(n)
for i in x:
    for j in x:
        if i==j:
            s=s+1
    if s==1:
        f=f+1
    s=0
if len(x)==f:
    print("Unique Number")
else:
    print("Not Unique Number")