n = int(input())
s=0
f=0
x=0
q=n
for i in range(1, n+1):
    if n%i==0:
        s=s+1
if s==2:
    while q!=0:
        r = q%10
        if r!=1:
            for j in range(1, r+1):
                if r%j==0:
                    f=f+1
            if f==2:
                x=x+1
            f=0
        q=q//10
    if len(str(n))==x:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")